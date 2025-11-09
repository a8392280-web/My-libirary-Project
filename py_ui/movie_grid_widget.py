# movie_list_widget.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from app.utils.my_functions import link_to_image
from app.models.movie import Movie

class MovieGridItemWidget(QWidget):
    """Widget for grid view (Netflix style)."""

    def __init__(self, movie: Movie, index: int = 1, parent=None):
        super().__init__(parent)
        self.movie = movie
        self.index = index
        self.setup_ui()

    def setup_ui(self):
        m = self.movie
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(8)
        layout.setAlignment(Qt.AlignTop)

        # Poster (larger for grid view)
        self.poster_label = QLabel()
        self.poster_label.setFixedSize(150, 225)
        self.poster_label.setAlignment(Qt.AlignCenter)
        self.poster_label.setStyleSheet("""
            QLabel {
                background-color: #222; 
                border: 1px solid #555; 
                border-radius: 4px;
            }
        """)
        link_to_image(m.poster_path, self.poster_label, 150, 225)

        # Title only
        title_label = QLabel(m.title)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            QLabel {
                color: #000000;
                font-size: 14px;
                font-weight: bold;
            }
        """)
        title_label.setWordWrap(True)
        title_label.setMaximumHeight(40)

        # Year and rating
        info_label = QLabel(f"({m.year}) • ⭐ {m.rating if m.rating else 'N/A'}")
        info_label.setAlignment(Qt.AlignCenter)
        info_label.setStyleSheet("color: #aaa; font-size: 12px;")

        layout.addWidget(self.poster_label)
        layout.addWidget(title_label)
        layout.addWidget(info_label)

        # Grid item styling
        self.setFixedSize(170, 300)
        self.setStyleSheet("""
            MovieGridItemWidget {
                background-color: #1a1a1a;
                border: 1px solid #333;
                border-radius: 8px;
            }
            MovieGridItemWidget:hover {
                background-color: #2a2a2a;
                border: 1px solid #555;
            }
        """)