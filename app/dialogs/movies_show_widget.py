from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor 
from py_ui.movies_show import Ui_show
from PySide6.QtWidgets import QDialog , QMessageBox, QComboBox
from app.db.db import load_movies , move_movie,save_movies ,delete_movie,upadate_imdb_rating
from app.utils.my_functions import link_to_image , get_selected_section,resize_combo_box_to_contents
from app.utils.info_from_APIs import update_imdb_info_if_old


class ShowMovieWindow(QDialog): # Inherit from QDialog for modal behavior
    def __init__(self,section,id, parent=None): # Optional parent parameter
        super().__init__(parent) # Call the parent constructor
        self.data = load_movies()
        self.ui = Ui_show() # Create an instance of the UI class
        self.ui.setupUi(self) # Set up the UI
        self.setWindowTitle("Movie Details")

        self.section = section 
        self.id = id

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
        self.comboBox(exccept= section)


    # Slotss:-
    def move_to(self):
        "Move selected movie to another section"
        try:
            if self.ui.move_to_combobox.currentIndex() != -1: 
                move_movie(self.section, get_selected_section(self.ui.move_to_combobox), self.id)

        except Exception as e:
            print("Error while moving movie:", e)

        self.close()

    def comboBox(self,exccept):
        "Fill combobox with all sections except the given one"
        sections = self.data
        list_of_sections = list(sections.keys())
        for section in list_of_sections:
            if section == exccept:
                continue
            else:
                self.ui.move_to_combobox.addItem(section.replace("_"," ").capitalize())

    def get_info(self):
            "Get movie info by its ID"
            data = self.data

            for movie in data[self.section]:
                if movie["id"] == self.id:
                    return movie 
            return None

    def show_plot(self, event):
        "Show movie plot in a message box"
        plot = self.get_info().get("plot", "No description available.")
        QMessageBox.information(self, "Movie Plot", plot)


    def show_info(self):
        "Display movie info and poster in the UI"
        movie= self.get_info()

        updated_movie = upadate_imdb_rating(movie, self.section, self.id)
        if updated_movie:
            movie = updated_movie
  
        self.ui.show_name_lable.setText(movie.get("Name", "N/A"))
        self.ui.show_time_lable.setText(movie.get("Runtime", "N/A"))
        self.ui.show_label.setText(movie.get("Released", "N/A"))
        self.ui.show_gener_lable.setText(", ".join(movie.get("Genres", [])))
        self.original_image_url = movie.get("Image", "")

        self.ui.show_imdb_rate_lable.setText(movie.get("Rating","N/A"))
        self.ui.show_user_rate_lable.setText(movie.get("User_rating","N/A"))

        self.ui.show_plot_lable.setText("Plotℹ️")
        self.ui.show_plot_lable.setToolTip("Click to see full plot")
        self.ui.show_plot_lable.setCursor(QCursor(Qt.PointingHandCursor))
        self.ui.show_plot_lable.mousePressEvent = self.show_plot

        link_to_image(path=movie["Image"],label=self.ui.show_image_lable,x=180,y=270)


    def delete_current_movie(self):
        """Ask for confirmation, delete the movie, and close the window."""
        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            "Are you sure you want to delete this movie?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            from_section = self.section
            success = delete_movie(from_section, self.id)
            if success:
                QMessageBox.information(self, "Deleted", "Movie deleted successfully.")
                self.close()
            else:
                QMessageBox.warning(self, "Error", "Failed to delete movie.")
    
    def edit(self):
        "Load movie data into edit fields and display its poster"
        movie= self.get_info()
        self.ui.show_edit_name_line.setText(movie.get("Name", "N/A"))
        self.ui.show_edit_time_line.setText(movie.get("Runtime", "N/A"))
        self.ui.show_edit_date_line.setText(movie.get("Released", "N/A"))
        self.ui.show_edit_gener_line.setText(", ".join(movie.get("Genres", [])))

        self.ui.show_edit_plot_line.setText(movie.get("plot", "No description available."))

        self.ui.show_edit_imdb_rate_line.setText(movie.get("Rating", "N/A"))
        self.ui.show_edit_user_rate_line.setText(movie.get("User_rating", "N/A"))

        link_to_image(path=movie["Image"],label=self.ui.show_edit_image_label,x=180,y=270)
             
    def apply_edit(self):
        """Apply changes only if user modified something"""
        data = self.data
        movies = data.get(self.section, [])

        for movie in movies:
                if movie.get("id") == self.id:

                    # ✅ Collect the new data from UI
                    new_name = self.ui.show_edit_name_line.text().strip()
                    new_runtime = self.ui.show_edit_time_line.text().strip()
                    new_released = self.ui.show_edit_date_line.text().strip()
                    new_plot = self.ui.show_edit_plot_line.text().strip()
                    new_imdb_rate = self.ui.show_edit_imdb_rate_line.text().strip()
                    new_user_rate = self.ui.show_edit_user_rate_line.text().strip()
                    new_genres = [g.strip() for g in self.ui.show_edit_gener_line.text().split(",")]
                    new_image_path = self.ui.show_edit_image_url.text().strip()
                    if new_image_path == "":
                        new_image_path = self.original_image_url
                    # ✅ Compare old vs new values

                    changed = False

                    if new_name != movie["Name"]:
                        movie["Name"] = new_name
                        changed = True
                    if new_runtime != movie["Runtime"]:
                        movie["Runtime"] = new_runtime
                        changed = True
                    if new_released != movie["Released"]:
                        movie["Released"] = new_released
                        changed = True
                    if new_plot != movie["plot"]:
                        movie["plot"] = new_plot
                        changed = True
                    if new_imdb_rate != movie["Rating"]:
                        movie["Rating"] = new_imdb_rate
                        changed = True
                    if new_user_rate != movie["User_rating"]:
                        movie["User_rating"] = new_user_rate
                        changed = True
                    if new_genres != movie["Genres"]:
                        movie["Genres"] = new_genres
                        changed = True

                    if new_image_path != movie["Image"]:
                        movie["Image"] = new_image_path
                        changed = True

                    # ✅ Save only if something changed
                    if changed:
                        save_movies(data)
                        self.show_info()
                        print("✅ Movie updated successfully!")
                    else:
                        print("⚙️ No changes detected, skipping save.")
                    self.ui.stackedWidget.setCurrentIndex(0)


    def preview_or_restore_image(self):
        """Preview new image on Enter, or restore old one if field empty."""
        url = self.ui.show_edit_image_url.text().strip()
        label = self.ui.show_edit_image_label

        # If the field is empty → restore the old poster
        if not url:
            if hasattr(self, "original_image_url") and self.original_image_url:
                link_to_image(self.original_image_url, label, 150, 220)
            else:
                label.setText("No Image URL")
                label.setAlignment(Qt.AlignCenter)
                label.setStyleSheet("color: gray;")
            return

        # Try to load the new image as preview
        label.setText("Loading preview...")
        label.setAlignment(Qt.AlignCenter)
        link_to_image(url, label, 150, 220)
