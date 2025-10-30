from PySide6.QtCore import Qt,QSettings
from PySide6.QtWidgets import QListWidgetItem, QWidget, QHBoxLayout, QVBoxLayout, QLabel,QListWidget
from PySide6.QtGui import QPixmap
from db.db import load_movies
from widgets.my_functions import link_to_image
import re
class MovieListItemWidget(QWidget):
    def __init__(self, db_id, title, year, rating, poster_path, user_rating, runtime,index=1, parent=None):
        super().__init__(parent)
        self.settings = QSettings("MyCompany", "MyApp")

        self.db_id = db_id  # ID from your DB
        self.title = title
        self.year = year
        self.rating = rating
        self.user_rating = user_rating
        self.poster_path = poster_path
        self.runtime = runtime  # New runtime parameter
        self.index = index
        self.setup_ui()
        
    def setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 10, 15, 10)
        # index Label - Changed color from yellow to a lighter gray
        index_label = QLabel(f"{self.index }-")
        index_label.setFixedWidth(50)
        index_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        index_label.setStyleSheet("""
            QLabel {
                font-weight: bold;
                font-size: 18px;
                color: #aaaaaa;  
            }
        """)
        
        #---------------------------- Movie poster (from online link) ----------------------
        self.poster_label = QLabel()
        self.poster_label.setFixedSize(60, 90)
        self.poster_label.setAlignment(Qt.AlignCenter)
        self.poster_label.setStyleSheet("background-color: #222; border: 1px solid #555; color: gray;")
        link_to_image(self.poster_path,self.poster_label,60,90)

        # -------------------------------- Movie info -----------------------------------
        info_widget = QWidget()
        info_layout = QVBoxLayout(info_widget)
        info_layout.setContentsMargins(15, 0, 0, 0)
        info_layout.setSpacing(2)  # Reduced spacing between info elements
        
        # ------------------------------ movie title --------------------------------------
        title_label = QLabel(self.title)
        title_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        
        # ---------------------------- year,runtime widget -----------------------------------
        year_runtime_widget = QWidget()
        year_runtime_layout = QHBoxLayout(year_runtime_widget)
        year_runtime_layout.setContentsMargins(0, 0, 0, 0)
        year_runtime_layout.setSpacing(10)


        # ---------------------------------- Year ----------------------------------------------
        year_label = QLabel(f"({self.year})")
        year_label.setStyleSheet("color: #666; font-size: 14px;")
        


        
        
        #----------------------------------- Runtime -------------------------------------------
        

        # Normalize input (lowercase, remove extra spaces)
        time_str = self.runtime.lower().strip()

        # Extract hours and minutes using regex
        hours_match = re.search(r'(\d+)\s*(h|hour|hours)', time_str)
        minutes_match = re.search(r'(\d+)\s*(m|min|mins|minute|minutes)', time_str)

        total_minutes = 0

        # If there are hours, convert to minutes
        if hours_match:
            total_minutes += int(hours_match.group(1)) * 60

        # If there are minutes, add them
        if minutes_match:
            total_minutes += int(minutes_match.group(1))
        
        # If only a number (like "150") is given
        if not hours_match and not minutes_match and time_str.isdigit():
            total_minutes = int(time_str)

        # Convert total minutes to hours + minutes
        hours = total_minutes // 60
        remaining_minutes = total_minutes % 60

        runtime_label = QLabel(f"⏱️ {hours}h {remaining_minutes}min")
        runtime_label.setStyleSheet("color: #666; font-size: 14px;")
        

        # ------------------- Layout --------------------------------

        year_runtime_layout.addWidget(year_label)
        year_runtime_layout.addWidget(runtime_label)
        year_runtime_layout.addStretch()
        
        info_layout.addWidget(title_label)
        info_layout.addWidget(year_runtime_widget)
        info_layout.addStretch()
        
        #------------------------ Rating-------------------------------

        # IMDb-like rating (yellow stars)
        rating_widget = self.create_rating_widget(self.rating, color="#aca13e",label_text="IMDB:-")

        # User rating (blue stars)
        user_rating_widget = self.create_rating_widget(self.user_rating, color="#2a418b",label_text="My Rating:-")

        # Combine both vertically
        all_rating_widget = QWidget()
        all_rating = QVBoxLayout(all_rating_widget)
        all_rating.setContentsMargins(0, 0, 0, 0)
        all_rating.addWidget(rating_widget)
        all_rating.addSpacing(4)
        all_rating.addWidget(user_rating_widget)

        #----------------------------- Add all widgets to main layout --------------------------------------

        layout.addWidget(index_label)  # Add index label first
        layout.addWidget(self.poster_label)
        layout.addWidget(info_widget)
        layout.addStretch()
        layout.addWidget(all_rating_widget)
        
        # Set hover effect and border
        self.setFixedHeight(100)
        self.setStyleSheet("""
            MovieListItemWidget {
                border: 1px solid #333;
                border-radius: 4px;
                background-color: #1a1a1a;
            }
            MovieListItemWidget:hover {
                background-color: #2a2a2a;
                border: 1px solid #555;
            }
        """)


    #----------------------------------- Functions --------------------------------------- 
    
    def create_rating_widget(self, value, color="#B1BB1F", icon_path=None, label_text=None):
        """Create a star rating widget with optional icon and text label."""
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setAlignment(Qt.AlignRight)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)  # small gap between items

        # Optional icon (like IMDb or user icon)
        if icon_path:
            icon_label = QLabel()
            pixmap = QPixmap(icon_path)
            icon_label.setPixmap(pixmap.scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            layout.addWidget(icon_label)

        # Optional text beside icon (e.g. "IMDb" or "My Rate")
        if label_text:
            text_label = QLabel(label_text)
            text_label.setStyleSheet("font-weight: bold; font-size: 15px; color: #156919")
            layout.addWidget(text_label)

        # Handle missing or invalid rating values safely
        try:
            rating_value = float(value)
        except (ValueError, TypeError):
            rating_value = 0.0

        # Convert rating to star count (0–5 scale)
        stars_count = int(rating_value) if rating_value > 0 else 0
        stars_label = QLabel("★" * stars_count)
        stars_label.setStyleSheet(f"color: {color}; font-size: 20px;")

        # Numeric rating or "N/A"
        value_label = QLabel(str(value) if value else "N/A")
        value_label.setStyleSheet("font-weight: bold; font-size: 16px; color: #aaa;")

        layout.addWidget(stars_label)
        layout.addWidget(value_label)

        return widget
    
     
    def load_from_db(self, section, section_list_widget):
        "Load movies for the given section and display them in the list"
        self.section = section
        self.section_list_widget = section_list_widget
        self.refresh_list()

    def refresh_list(self, sort_by= None, reverse=None):
        "Refresh and display the movie list with sorting and styling"
        if not hasattr(self, "section") or not hasattr(self, "section_list_widget"):
            return  # nothing to refresh ye
        """data = list of dicts from your DB"""
        data = load_movies() # Load full JSON structure
        movie_list = data[self.section] 

        # ✅ Sort movies before displaying
        sort_by = self.settings.value(f"{self.section}_sort_by", "Name")
        reverse = self.settings.value(f"{self.section}_sort_by_reverse", "false").lower() == "true"


        if sort_by:
            movie_list = sorted(
                movie_list,
                key=lambda x: str(x.get(sort_by, "")).strip().lower(),
                reverse=reverse
            )

        # Disable selection highlight for the list widget
        self.section_list_widget.setSelectionMode(QListWidget.SelectionMode.NoSelection)
        self.section_list_widget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        
        # Custom style to remove selection highlighting
        self.section_list_widget.setStyleSheet("""
            QListWidget {
                outline: 0;
                border: none;
                background-color: transparent;
            }
            QListWidget::item {
                border: none;
                background-color: transparent;
            }
            QListWidget::item:selected {
                background-color: transparent;
            }
        """)
        
        self.section_list_widget.clear()

        for index, movie in enumerate(movie_list, start=1):
            item_widget = MovieListItemWidget(
            db_id=movie.get("id", 0),
            title=movie.get("Name", "Unknown"),
            year=movie.get("Released", "N/A"),
            rating=movie.get("Rating", "N/A"),
            poster_path=movie.get("Image", ""),
            user_rating=movie.get("User_rating", "N/A"),
            runtime=movie.get("Runtime", "N/A"),
                index=index   # 👈 pass index here
            )
            
            item = QListWidgetItem(self.section_list_widget)
            item.setSizeHint(item_widget.sizeHint())
            
            # ✅ Store the movie ID in the QListWidgetItem
            item.setData(Qt.UserRole, movie["id"])


            # ✅ Store the ENTIRE movie dict for reuse or filtering
            item.setData(Qt.UserRole + 1, movie)

            # Disable selection for individual items
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsSelectable)

            

            self.section_list_widget.addItem(item)
            self.section_list_widget.setItemWidget(item, item_widget)


           