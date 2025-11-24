from PySide6.QtWidgets import QListWidget, QListWidgetItem, QListView
from PySide6.QtCore import Qt, QSettings, QSize
from app.models.movie import Movie
from app.utils.my_functions import link_to_image
from app.db.movies_db import list_movies
from py_ui.movie_list_widget import MovieListItemWidget
from py_ui.movie_grid_widget import MovieGridItemWidget
from PySide6.QtGui import QShortcut, QKeySequence

class MovieListLoader:
    """Handles loading movies into a QListWidget with dual view modes."""

    def __init__(self, list_widget: QListWidget):
        self.list_widget = list_widget
        self.settings = QSettings("MyCompany", "MyApp")
        self.current_view = self.settings.value("movie_view_mode", "list")  # Default to list view
        self.current_movies = []  # Track current movies
        self.current_section = None  # Track current section
        
        self.setup_view_mode()

    def setup_view_mode(self):
        """Configure the list widget based on current view mode."""
        if self.current_view == "grid":
            self.list_widget.setViewMode(QListView.IconMode)
            self.list_widget.setFlow(QListView.LeftToRight)
            self.list_widget.setWrapping(True)
            self.list_widget.setResizeMode(QListView.Adjust)
            self.list_widget.setGridSize(QSize(170, 300))
            self.list_widget.setSpacing(10)
            self.list_widget.setMovement(QListView.Static)
        else:  # list view
            self.list_widget.setViewMode(QListView.ListMode)
            self.list_widget.setFlow(QListView.TopToBottom)
            self.list_widget.setWrapping(False)
            self.list_widget.setResizeMode(QListView.Adjust)
            self.list_widget.setGridSize(QSize())  # Reset grid size
            self.list_widget.setSpacing(5)

    def set_view_mode(self, view_mode: str):
        """Switch between list and grid views."""
        self.current_view = view_mode
        self.settings.setValue("movie_view_mode", view_mode)
        self.setup_view_mode()
        
        # Reload current movies if we have any
        if self.current_movies:
            self.load_movies(self.current_movies)
         # Or reload from current section if available
        elif self.current_section:
            self.load_from_section(self.current_section)

    def load_movies(self, movies: list[Movie]):
        """Populate the QListWidget with appropriate widget based on view mode."""
        self.list_widget.clear()
        self.current_movies = movies  # Store current movies

        for index, movie in enumerate(movies, start=1):
            # Choose the right widget type based on view mode
            if self.current_view == "grid":
                item_widget = MovieGridItemWidget(movie, index=index)
                item_size = QSize(170, 300)  # Grid item size
            else:
                item_widget = MovieListItemWidget(movie, index=index)
                item_size = item_widget.sizeHint()  # List item uses natural size
            
            item = QListWidgetItem(self.list_widget)
            item.setSizeHint(item_size)
            
            # Store movie object for later retrieval
            item.setData(Qt.UserRole, movie)

            # Disable selection if needed
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsSelectable)

            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, item_widget)

    def load_from_section(self, section: str, order_by="title", descending=False):
        """Fetch movies from DB by section and load them."""
        sort_key = self.settings.value(f"{section}_sort_by", "title")
        reverse = self.settings.value(f"{section}_sort_by_reverse", False, type=bool)
        descending = bool(reverse)

        movies = list_movies(section=section, order_by=sort_key, descending=descending)
        self.current_section = section  # Track current section
        self.load_movies(movies)
