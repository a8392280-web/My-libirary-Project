from PySide6.QtCore import Qt,Signal
from PySide6.QtGui import QCursor 
from py_ui.movies_show import Ui_show
from PySide6.QtWidgets import QDialog , QMessageBox, QComboBox
from app.db.sqlite_manger import get_movie_by_id, update_movie, delete_movie, move_movie_section
from app.utils.my_functions import link_to_image , get_selected_section,resize_combo_box_to_contents
from app.utils.info_from_APIs import update_imdb_info_if_old


class ShowMovieWindow(QDialog): # Inherit from QDialog for modal behavior
    movie_deleted = Signal()
    movie_moved = Signal()


    def __init__(self,section,id, parent=None): # Optional parent parameter
        super().__init__(parent) # Call the parent constructor

        self.ui = Ui_show() # Create an instance of the UI class
        self.ui.setupUi(self) # Set up the UI
        self.setWindowTitle("Movie Details")

        self.section = section 
        self.id = id
        self.movie = None

        self.show_info()

        self.ui.show_edit_image_url.returnPressed.connect(self.preview_or_restore_image) # Preview or restore image when Enter is pressed

        #------------------------- Setup widget -----------------------------

        self.ui.stackedWidget.setCurrentIndex(0) # Show the first page by default
        

        #------------------------- Setup Buttons -----------------------------

        self.ui.show_delete_button.clicked.connect(self.delete_current_movie)
        self.ui.show_delete_button.setShortcut("del")

        self.ui.show_edit_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.show_edit_button.clicked.connect(self.edit)
        self.ui.show_edit_button.setShortcut("e")

        self.ui.show_cancel_button.clicked.connect(self.close)
        self.ui.show_apply_button.clicked.connect(self.move_to)     
        self.ui.show_edit_apply_button.clicked.connect(self.apply_edit)
         
        self.ui.show_edit_cancel_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0)) 
        # This would not work, because setCurrentIndex expects an argument, but the clicked signal doesn't provide one.so we use lambda.

        #----------------------Setup combobox(move_to) ------------------------

        # make the long text in the combobox seen
        self.ui.move_to_combobox.showPopup = lambda: (resize_combo_box_to_contents(self.ui.move_to_combobox),
                                                      QComboBox.showPopup(self.ui.move_to_combobox))
        self.comboBox(section)


    # Slotss:-
    def move_to(self):
        "Move selected movie to another section"
        try:
            if self.ui.move_to_combobox.currentIndex() != -1: 
                new_section = get_selected_section(self.ui.move_to_combobox)
                success = move_movie_section(self.id, new_section)
                if success:
                    self.movie_moved.emit()  # Emit signal
                    print(f"✅ Movie moved to {new_section}")
                else:
                    print("❌ Failed to move movie")
                self.close()

        except Exception as e:
            print("Error while moving movie:", e)
            QMessageBox.critical(self, "Error", f"Failed to move movie: {str(e)}")



    def comboBox(self, except_section):
        "Fill combobox with all sections except the given one"
        sections = ["watching", "want_to_watch", "continue_later", "dont_want_to_continue", "watched"]
        for section in sections:
            if section == except_section:
                continue
            else:
                self.ui.move_to_combobox.addItem(section.replace("_"," ").capitalize())


    def get_info(self):
        "Get movie info by its ID"
        if not self.movie:
            self.movie = get_movie_by_id(self.id)
        return self.movie


    def show_plot(self, event):
        "Show movie plot in a message box"
        movie = self.get_info()
        if movie and movie.plot:
            QMessageBox.information(self, "Movie Plot", movie.plot)
        else:
            QMessageBox.information(self, "Movie Plot", "No description available.")

    def show_info(self):
        "Display movie info and poster in the UI"
        movie = self.get_info()
        if not movie:
            QMessageBox.critical(self, "Error", "Movie not found!")
            self.close()
            return

        print(f"DEBUG: Movie data - Title: {movie.title}, Year: {movie.year}")  # Debug

        # Set movie data to labels
        self.ui.show_name_lable.setText(movie.title or "No title")
        self.ui.show_time_lable.setText(f"{movie.runtime} min" if movie.runtime else "Runtime not available")
        self.ui.show_label.setText(str(movie.year) if movie.year else "Year not available")
        self.ui.show_gener_lable.setText(", ".join(movie.genres) if movie.genres else "No genres")
        self.original_image_url = movie.poster_path or ""

        self.ui.show_imdb_rate_lable.setText(str(movie.rating) if movie.rating else "No rating")
        self.ui.show_user_rate_lable.setText(str(movie.user_rating) if movie.user_rating else "No user rating")

        # Setup plot label
        self.ui.show_plot_lable.setText("Plotℹ️")
        self.ui.show_plot_lable.setToolTip("Click to see full plot")
        self.ui.show_plot_lable.setCursor(QCursor(Qt.PointingHandCursor))
        self.ui.show_plot_lable.mousePressEvent = self.show_plot

        # Load image
        if movie.poster_path:
            link_to_image(path=movie.poster_path, label=self.ui.show_image_lable, x=180, y=270)
        else:
            self.ui.show_image_lable.setText("No Image Available")
            self.ui.show_image_lable.setAlignment(Qt.AlignCenter)
            self.ui.show_image_lable.setStyleSheet("color: gray;")

    def delete_current_movie(self):
        """Ask for confirmation, delete the movie, and close the window."""
        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            "Are you sure you want to delete this movie?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            success = delete_movie(self.id)
            if success:
                self.close()
                self.movie_deleted.emit()  # Emit signal
                QMessageBox.information(self, "Deleted", "Movie deleted successfully.")
                
            else:
                QMessageBox.warning(self, "Error", "Failed to delete movie.")
    
    def edit(self):
        "Load movie data into edit fields and display its poster"
        movie = self.get_info()
        if not movie:
            return

        self.ui.show_edit_name_line.setText(movie.title or "")
        self.ui.show_edit_time_line.setText(str(movie.runtime) if movie.runtime else "")
        self.ui.show_edit_date_line.setText(str(movie.year) if movie.year else "")
        self.ui.show_edit_gener_line.setText(", ".join(movie.genres) if movie.genres else "")

        self.ui.show_edit_plot_line.setText(movie.plot or "")

        self.ui.show_edit_imdb_rate_line.setText(str(movie.rating) if movie.rating else "")
        self.ui.show_edit_user_rate_line.setText(str(movie.user_rating) if movie.user_rating else "")

        if movie.poster_path:
            link_to_image(path=movie.poster_path, label=self.ui.show_edit_image_label, x=180, y=270)
        else:
            self.ui.show_edit_image_label.setText("No Image")
            self.ui.show_edit_image_label.setAlignment(Qt.AlignCenter)
             
    def apply_edit(self):
        """Apply changes to the movie in database"""
        movie = self.get_info()
        if not movie:
            QMessageBox.critical(self, "Error", "Movie not found!")
            return

        # Collect the new data from UI
        new_title = self.ui.show_edit_name_line.text().strip()
        new_runtime = self.ui.show_edit_time_line.text().strip()
        new_year = self.ui.show_edit_date_line.text().strip()
        new_plot = self.ui.show_edit_plot_line.text().strip()
        new_rating = self.ui.show_edit_imdb_rate_line.text().strip()
        new_user_rating = self.ui.show_edit_user_rate_line.text().strip()
        new_genres = [g.strip() for g in self.ui.show_edit_gener_line.text().split(",") if g.strip()]
        new_image_path = self.ui.show_edit_image_url.text().strip()

        # Update movie object
        changed = False

        if new_title != movie.title:
            movie.title = new_title
            changed = True

        if new_runtime and new_runtime != str(movie.runtime or ""):
            try:
                movie.runtime = int(new_runtime)
                changed = True
            except ValueError:
                QMessageBox.warning(self, "Invalid Runtime", "Runtime must be a number")
                return

        if new_year and new_year != str(movie.year or ""):
            try:
                movie.year = int(new_year)
                changed = True
            except ValueError:
                QMessageBox.warning(self, "Invalid Year", "Year must be a number")
                return

        if new_plot != (movie.plot or ""):
            movie.plot = new_plot
            changed = True

        if new_rating and new_rating != str(movie.rating or ""):
            try:
                movie.rating = float(new_rating)
                changed = True
            except ValueError:
                QMessageBox.warning(self, "Invalid Rating", "IMDB Rating must be a number")
                return

        if new_user_rating and new_user_rating != str(movie.user_rating or ""):
            try:
                movie.user_rating = float(new_user_rating)
                changed = True
            except ValueError:
                QMessageBox.warning(self, "Invalid Rating", "User Rating must be a number")
                return

        if new_genres != (movie.genres or []):
            movie.genres = new_genres
            changed = True

        if new_image_path and new_image_path != (movie.poster_path or ""):
            movie.poster_path = new_image_path
            changed = True

        # Save only if something changed
        if changed:
            try:
                update_movie(movie)
                self.movie = movie  # Update cached movie
                self.show_info()  # Refresh display
                QMessageBox.information(self, "Success", "Movie updated successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to update movie: {str(e)}")
        else:
            QMessageBox.information(self, "No Changes", "No changes were made.")

        self.ui.stackedWidget.setCurrentIndex(0)


    def preview_or_restore_image(self):
        """Preview new image on Enter, or restore old one if field empty."""
        url = self.ui.show_edit_image_url.text().strip()
        label = self.ui.show_edit_image_label

        # If the field is empty → restore the old poster
        if not url:
            movie = self.get_info()
            if movie and movie.poster_path:
                link_to_image(movie.poster_path, label, 180, 270)
            else:
                label.setText("No Image")
                label.setAlignment(Qt.AlignCenter)
                label.setStyleSheet("color: gray;")
            return

        # Try to load the new image as preview
        label.setText("Loading preview...")
        label.setAlignment(Qt.AlignCenter)
        link_to_image(url, label, 180, 270)