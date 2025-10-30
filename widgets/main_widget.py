from PySide6.QtCore import Qt, QSettings
from PySide6.QtWidgets import QWidget ,QMainWindow ,QListWidgetItem ,QMessageBox
import random
from gui.main_ui import Ui_main_widget
from widgets.movies_add_widget import AddMovieWindow
from widgets.movie_list_widget import MovieListItemWidget
from widgets.movies_show_widget import ShowMovieWindow
from db import db


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__() # Initialize the parent class
         
        self.ui = Ui_main_widget()
        self.ui.setupUi(self) # Set up the UI from the imported class

        self.setWindowTitle("My Library") # set the window title
        self.settings = QSettings("MyCompany", "MyApp") # learn about it then see

        # ✅ Create a helper object to handle movie list logic
        self.movie_helper = MovieListItemWidget(0, "", "", "", "", "", "")

        #✅ Connect the database save signal to refresh all sections
        db.on_movies_saved = self.refresh_all_sections 


        # section with its content
        self.sections = {
            "watching": {
                "list": self.ui.watching_list,
                "search": self.ui.watching_search,
                "combobox": self.ui.wahtching_sort_box,
                "random_button": self.ui.watching_random_button,
            },
            "want_to_watch": {
                "list": self.ui.want_to_watch_list,
                "search": self.ui.want_to_watch_search,
                "combobox": self.ui.want_to_watch_sort_by,
                "random_button": self.ui.want_to_watch_random_button,
            },
            "continue_later": {
                "list": self.ui.continue_later_list,
                "search": self.ui.continue_later_search,
                "combobox" : self.ui.continue_later_sort_by,
                "random_button": self.ui.continue_later_random_button,
            },
            "dont_want_to_continue": {
                "list": self.ui.dont_want_to_continue_list,
                "search": self.ui.dont_want_to_continue_search,
                "combobox": self.ui.dont_want_to_continue_sort_by,
                "random_button": self.ui.dont_want_to_continue_random_button,
            },
            "watched": {
                "list": self.ui.watched_list,
                "search": self.ui.watched_search,
                "combobox": self.ui.watched_sort_by,
                "random_button": self.ui.watched_random_button,
            },
            
        }


        # set up  widget:-
        self.ui.stacked_body_Widget.setCurrentIndex(0) # Home page

        #---------------------------- Set up buttons and shortcuts ----------------------

        self.ui.home_button.setChecked(True) # Home button is checked by default
        self.ui.home_button.clicked.connect(self.show_home)
        self.ui.home_button.setShortcut("0")
    
        self.ui.movies_button.clicked.connect(self.show_movies)
        self.ui.movies_button.setShortcut("1")

        self.ui.games_button.clicked.connect(self.show_games)
        self.ui.games_button.setShortcut("2")

        self.ui.books_button.clicked.connect(self.show_books)
        self.ui.books_button.setShortcut("3")

        self.ui.comics_button.clicked.connect(self.show_comics)
        self.ui.comics_button.setShortcut("4")

        self.ui.setting_button.clicked.connect(self.show_setting)
        self.ui.setting_button.setShortcut("5")

        self.ui.movies_add_botton.clicked.connect(self.open_add_movie_window)
        self.ui.movies_add_botton.setShortcut("+")

        # make search bars not focus until it gets clicked
        for section_name, section_data in self.sections.items():
            search_widget = section_data["search"]
            search_widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        # Load movies data at startup
        for section_name, section_data in self.sections.items():
            list_widget = section_data["list"]
            self.movie_helper.load_from_db(section_name, list_widget)

        # Show item info on click 
        for section_name, section_data in self.sections.items():
            list_widget = section_data["list"]
            list_widget.itemClicked.connect(
            lambda item, section=section_name: self.on_item_clicked(item, section) # When Qt emits itemClicked, it passes the clicked item — that becomes item.
            )

        #-------------------------- Setup Random buttons -------------------------------
        for section_name, section_data in self.sections.items():
            list_widget = section_data["list"]
            random_button = section_data["random_button"]
            random_button.clicked.connect(lambda checked=False, lw=list_widget: self.pick_random_movie(lw))

        #-------------------------- Setup Search buttons -------------------------------

        for section_name, section_data in self.sections.items():
            list_widget = section_data["list"]
            search_line = section_data["search"]
            search_line.textChanged.connect(lambda text, lw=list_widget: self.filter_list(text, lw))

        #-------------------------------Setup Sort_by box -------------------------------------------

        # Define the combo box options once
        options = [
            "Name (A-Z)",
            "Name (Z-A)",
            "Year (Newest-Oldest)",
            "Year (Oldest-Newest)",
            "IMDB Rating (High-Low)",
            "IMDB Rating (Low-High)",
            "User Rating (High-Low)",
            "User Rating (Low-High)"
        ]

        # Configure all combo boxes in one loop
        for section_name, section_data in self.sections.items():
            combo_widget = section_data["combobox"]
            combo_widget.blockSignals(True)  # Prevent triggering signal while setting up # learn about it

            combo_widget.clear()
            combo_widget.addItems(options)

            # Restore saved sort option (if exists)
            saved_text = self.settings.value(f"{section_name}_sort_by_text")
            if saved_text:
                combo_widget.setCurrentText(saved_text)
            else:
                combo_widget.setCurrentIndex(-1)

            combo_widget.blockSignals(False)  # Re-enable signals

            # Connect the signal AFTER setup
            combo_widget.currentTextChanged.connect(
                lambda text, section=section_name: self.on_sort_changed(section, text)
            )


    # Slots:-----------------------------------------------------------------

    # set up side buttons:-
    def show_home(self):
        self.ui.stacked_body_Widget.setCurrentIndex(0)
    def show_movies(self):
        self.ui.stacked_body_Widget.setCurrentIndex(1)
    def show_games(self):
        self.ui.stacked_body_Widget.setCurrentIndex(2)
    def show_books(self):
        self.ui.stacked_body_Widget.setCurrentIndex(3)
    def show_comics(self):
        self.ui.stacked_body_Widget.setCurrentIndex(4)
    def show_setting(self):
        self.ui.stacked_body_Widget.setCurrentIndex(5)

    
    def open_add_movie_window(self):
        # Open the Add Movie window as a modal dialog
        self.add_window = AddMovieWindow()  # Create a separate standalone window
        self.add_window.exec()              # Use exec() for QDialog to make it modal( blocks interaction with other windows).
        # self.add_window.show()


    def on_item_clicked(self, item,section):
            # Open the movie info window for the selected item
            self.selected_id = item.data(Qt.UserRole)
            self.show_movie_window = ShowMovieWindow(section= section, id=self.selected_id)
            self.show_movie_window.show_info() 
            self.show_movie_window.exec()
            
    def filter_list(self, text , list_widget):
        # Filter movies in the list based on the entered text
        text = text.strip().lower()
        for i in range(list_widget.count()):
            item = list_widget.item(i)
            movie = item.data(Qt.UserRole + 1)  # full dict

            # Merge all movie info into one searchable string
            search_text = " ".join([
                str(movie.get("Name", "")),
                str(movie.get("Released", ""))
                ]).lower()

            item.setHidden(text not in search_text)



    def pick_random_movie(self, list_widget):
        "Picks a random movie frome the given list"
        count = list_widget.count()
        if count == 0:
            QMessageBox.information(self, "No Movies", "This list is empty!")
            return
        
        # Pick a random index
        random_index = random.randint(0, count - 1)
        item = list_widget.item(random_index)

        # Scroll to and highlight the random movie
        list_widget.scrollToItem(item)
        item.setSelected(True)

        # If you have item widgets, you can also retrieve their data:
        movie_data = item.data(Qt.UserRole + 1)
        if movie_data:
            print(f"🎬 Random movie: {movie_data.get('Name', 'Unknown')}")

        # Optional: show a popup
        QMessageBox.information(
            self,
            "Random Pick",
            f"🎬 Your random movie is:\n\n{movie_data.get('Name', 'Unknown')}"
        )



    def on_sort_changed(self, section, sort_by):
        "Sort movies in the selected section based on the chosen criteria"        
        if sort_by == "Name (A-Z)":
            sort_key, reverse = "Name", False
        elif sort_by == "Name (Z-A)":
            sort_key, reverse = "Name", True
        elif sort_by == "Year (Newest-Oldest)":
            sort_key, reverse = "Released", True
        elif sort_by == "Year (Oldest-Newest)":
            sort_key, reverse = "Released", False
        elif sort_by == "IMDB Rating (High-Low)":
            sort_key, reverse = "Rating", True
        elif sort_by == "IMDB Rating (Low-High)":
            sort_key, reverse = "Rating", False
        elif sort_by == "User Rating (High-Low)":
            sort_key, reverse = "User_rating", True
        elif sort_by == "User Rating (Low-High)":
            sort_key, reverse = "User_rating", False
        else:
    
            return  # unknown option

        # Save user preference
        self.settings.setValue(f"{section}_sort_by_text", sort_by)
        self.settings.setValue(f"{section}_sort_by", sort_key)
        self.settings.setValue(f"{section}_sort_by_reverse", reverse)

        # Reload the list
        self.refresh_one_section(section , self.sections[section]["list"])




    def refresh_all_sections(self):
        "refres all list widgets"
        for section_name, section_data in self.sections.items():
            self.movie_helper.load_from_db(section_name, section_data["list"])


    def refresh_one_section(self, section , list):
        "refres one list widgets"
        self.movie_helper.load_from_db(section,list)
        


    



















