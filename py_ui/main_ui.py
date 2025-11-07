# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui tddrYUGJbE.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QVBoxLayout,
    QWidget)
import py_ui.resources_rc

class Ui_main_widget(object):
    def setupUi(self, main_widget):
        if not main_widget.objectName():
            main_widget.setObjectName(u"main_widget")
        main_widget.resize(1270, 753)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_widget.sizePolicy().hasHeightForWidth())
        main_widget.setSizePolicy(sizePolicy)
        main_widget.setMinimumSize(QSize(0, 0))
        main_widget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(main_widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.side_widget = QWidget(main_widget)
        self.side_widget.setObjectName(u"side_widget")
        self.side_widget.setStyleSheet(u"QWidget{background-color:\n"
"rgb(0, 0, 0);}")
        self.verticalLayout_2 = QVBoxLayout(self.side_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_button = QPushButton(self.side_widget)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setEnabled(True)
        self.home_button.setAutoFillBackground(False)
        self.home_button.setStyleSheet(u"QPushButton:checked {\n"
"    background-color: rgb(83, 83, 83);}")
        icon = QIcon()
        icon.addFile(u":/icons/Icons/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.home_button.setIcon(icon)
        self.home_button.setIconSize(QSize(40, 40))
        self.home_button.setCheckable(True)
        self.home_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_button)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.movies_button = QPushButton(self.side_widget)
        self.movies_button.setObjectName(u"movies_button")
        self.movies_button.setAutoFillBackground(False)
        self.movies_button.setStyleSheet(u"QPushButton:checked {\n"
"    background-color: rgb(83, 83, 83);}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/movies.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.movies_button.setIcon(icon1)
        self.movies_button.setIconSize(QSize(50, 50))
        self.movies_button.setCheckable(True)
        self.movies_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.movies_button)

        self.games_button = QPushButton(self.side_widget)
        self.games_button.setObjectName(u"games_button")
        self.games_button.setEnabled(True)
        self.games_button.setAutoFillBackground(False)
        self.games_button.setStyleSheet(u"QPushButton:checked {\n"
"    background-color: rgb(83, 83, 83);}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/games.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.games_button.setIcon(icon2)
        self.games_button.setIconSize(QSize(40, 40))
        self.games_button.setCheckable(True)
        self.games_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.games_button)

        self.books_button = QPushButton(self.side_widget)
        self.books_button.setObjectName(u"books_button")
        self.books_button.setEnabled(True)
        self.books_button.setAutoFillBackground(False)
        self.books_button.setStyleSheet(u"QPushButton:checked {\n"
"    background-color: rgb(83, 83, 83);}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/books.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.books_button.setIcon(icon3)
        self.books_button.setIconSize(QSize(40, 40))
        self.books_button.setCheckable(True)
        self.books_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.books_button)

        self.comics_button = QPushButton(self.side_widget)
        self.comics_button.setObjectName(u"comics_button")
        self.comics_button.setEnabled(True)
        self.comics_button.setAutoFillBackground(False)
        self.comics_button.setStyleSheet(u"QPushButton:checked {\n"
"    background-color: rgb(83, 83, 83);}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/comics.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.comics_button.setIcon(icon4)
        self.comics_button.setIconSize(QSize(40, 40))
        self.comics_button.setCheckable(True)
        self.comics_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.comics_button)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.setting_button = QPushButton(self.side_widget)
        self.setting_button.setObjectName(u"setting_button")
        self.setting_button.setEnabled(True)
        self.setting_button.setAutoFillBackground(False)
        self.setting_button.setStyleSheet(u"QPushButton:checked {\n"
"    background-color: rgb(83, 83, 83);}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setting_button.setIcon(icon5)
        self.setting_button.setIconSize(QSize(50, 50))
        self.setting_button.setCheckable(True)
        self.setting_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.setting_button)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.side_widget, 0, 0, 1, 1)

        self.main_body_widget = QWidget(main_widget)
        self.main_body_widget.setObjectName(u"main_body_widget")
        sizePolicy.setHeightForWidth(self.main_body_widget.sizePolicy().hasHeightForWidth())
        self.main_body_widget.setSizePolicy(sizePolicy)
        self.main_body_widget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.main_body_widget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stacked_body_Widget = QStackedWidget(self.main_body_widget)
        self.stacked_body_Widget.setObjectName(u"stacked_body_Widget")
        self.stacked_body_Widget.setEnabled(True)
        self.stacked_body_Widget.setStyleSheet(u"QStackedWidget {\n"
"    background-color: rgb(128, 128, 128);\n"
"}\n"
"")
        self.welcome_section = QWidget()
        self.welcome_section.setObjectName(u"welcome_section")
        self.welcome_section.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.gridLayout_3 = QGridLayout(self.welcome_section)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.welcome_section)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.label = QLabel(self.welcome_section)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial Rounded MT"])
        font.setPointSize(36)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.TextFormat.RichText)
        self.label.setScaledContents(False)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.stacked_body_Widget.addWidget(self.welcome_section)
        self.movies_section = QWidget()
        self.movies_section.setObjectName(u"movies_section")
        self.movies_section.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.gridLayout_7 = QGridLayout(self.movies_section)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.movies_label = QLabel(self.movies_section)
        self.movies_label.setObjectName(u"movies_label")
        self.movies_label.setFont(font)

        self.horizontalLayout_2.addWidget(self.movies_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.movies_add_botton = QPushButton(self.movies_section)
        self.movies_add_botton.setObjectName(u"movies_add_botton")
        self.movies_add_botton.setMinimumSize(QSize(100, 0))
        self.movies_add_botton.setMaximumSize(QSize(50, 16777215))
        self.movies_add_botton.setAutoFillBackground(False)
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/Add icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.movies_add_botton.setIcon(icon6)
        self.movies_add_botton.setIconSize(QSize(60, 60))
        self.movies_add_botton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.movies_add_botton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.movies_tap_widget = QTabWidget(self.movies_section)
        self.movies_tap_widget.setObjectName(u"movies_tap_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.movies_tap_widget.sizePolicy().hasHeightForWidth())
        self.movies_tap_widget.setSizePolicy(sizePolicy1)
        self.movies_tap_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.movies_tap_widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.movies_tap_widget.setAutoFillBackground(False)
        self.movies_tap_widget.setStyleSheet(u"QTabWidget::pane {\n"
"    border: none;\n"
"    background: #f0f0f0;  /* light clean background */\n"
"}\n"
"\n"
"QTabBar {\n"
"    qproperty-drawBase: 0;\n"
"    alignment: center;  /* center the tabs */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: transparent;\n"
"    color: #444;\n"
"    padding: 10px 25px;\n"
"    margin: 0px 5px;\n"
"    font: 13pt \"Segoe UI\";\n"
"    border-bottom: 3px solid transparent;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    color: #0078d7;  /* accent blue */\n"
"    border-bottom: 3px solid #0078d7;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    color: #005a9e;\n"
"}\n"
"")
        self.movies_tap_widget.setTabPosition(QTabWidget.TabPosition.North)
        self.movies_tap_widget.setTabShape(QTabWidget.TabShape.Rounded)
        self.movies_tap_widget.setElideMode(Qt.TextElideMode.ElideNone)
        self.movies_tap_widget.setDocumentMode(True)
        self.movies_tap_widget.setTabsClosable(False)
        self.movies_tap_widget.setMovable(False)
        self.movies_tap_widget.setTabBarAutoHide(False)
        self.movies_watching = QWidget()
        self.movies_watching.setObjectName(u"movies_watching")
        self.gridLayout_13 = QGridLayout(self.movies_watching)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 10, -1)
        self.watching_search = QLineEdit(self.movies_watching)
        self.watching_search.setObjectName(u"watching_search")
        self.watching_search.setMaximumSize(QSize(200, 30))
        self.watching_search.setStyleSheet(u"QLineEdit {\n"
"    color: rgb(0, 0, 0);\n"
"    font-size: 14px;\n"
"    background-color: transparent;\n"
"    padding: 6px;\n"
"    border: none;\n"
"    border-bottom: 1px solid rgba(221, 221, 221, 100); /* \u0642\u0628\u0644 \u0627\u0644\u062a\u0631\u0643\u064a\u0632 */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgba(73, 133, 224, 0.12); /* \u0632\u064a input-hovered-color */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    outline: none;\n"
"    border-bottom: 2px solid #5891ff; /* \u0628\u0639\u062f \u0627\u0644\u062a\u0631\u0643\u064a\u0632 */\n"
"}\n"
"")
        self.watching_search.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.watching_search)

        self.line_2 = QFrame(self.movies_watching)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_2)

        self.watching_random_button = QPushButton(self.movies_watching)
        self.watching_random_button.setObjectName(u"watching_random_button")
        self.watching_random_button.setAutoFillBackground(False)
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/random.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.watching_random_button.setIcon(icon7)
        self.watching_random_button.setIconSize(QSize(50, 30))
        self.watching_random_button.setFlat(True)

        self.horizontalLayout_5.addWidget(self.watching_random_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.line = QFrame(self.movies_watching)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line)

        self.wahtching_sort_box = QComboBox(self.movies_watching)
        self.wahtching_sort_box.setObjectName(u"wahtching_sort_box")
        self.wahtching_sort_box.setFrame(False)
        self.wahtching_sort_box.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_5.addWidget(self.wahtching_sort_box)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.watching_list = QListWidget(self.movies_watching)
        self.watching_list.setObjectName(u"watching_list")

        self.verticalLayout_8.addWidget(self.watching_list)


        self.gridLayout_13.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.movies_tap_widget.addTab(self.movies_watching, "")
        self.movies_want_to_watch = QWidget()
        self.movies_want_to_watch.setObjectName(u"movies_want_to_watch")
        self.gridLayout_12 = QGridLayout(self.movies_want_to_watch)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, 10, -1)
        self.want_to_watch_search = QLineEdit(self.movies_want_to_watch)
        self.want_to_watch_search.setObjectName(u"want_to_watch_search")
        self.want_to_watch_search.setMaximumSize(QSize(200, 30))
        self.want_to_watch_search.setStyleSheet(u"QLineEdit {\n"
"    color: rgb(0, 0, 0);\n"
"    font-size: 14px;\n"
"    background-color: transparent;\n"
"    padding: 6px;\n"
"    border: none;\n"
"    border-bottom: 1px solid rgba(221, 221, 221, 100); /* \u0642\u0628\u0644 \u0627\u0644\u062a\u0631\u0643\u064a\u0632 */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgba(73, 133, 224, 0.12); /* \u0632\u064a input-hovered-color */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    outline: none;\n"
"    border-bottom: 2px solid #5891ff; /* \u0628\u0639\u062f \u0627\u0644\u062a\u0631\u0643\u064a\u0632 */\n"
"}\n"
"")
        self.want_to_watch_search.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.want_to_watch_search)

        self.line_5 = QFrame(self.movies_want_to_watch)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_5)

        self.want_to_watch_random_button = QPushButton(self.movies_want_to_watch)
        self.want_to_watch_random_button.setObjectName(u"want_to_watch_random_button")
        self.want_to_watch_random_button.setAutoFillBackground(False)
        self.want_to_watch_random_button.setIcon(icon7)
        self.want_to_watch_random_button.setIconSize(QSize(50, 30))
        self.want_to_watch_random_button.setFlat(True)

        self.horizontalLayout_8.addWidget(self.want_to_watch_random_button)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.line_6 = QFrame(self.movies_want_to_watch)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_6)

        self.want_to_watch_sort_by = QComboBox(self.movies_want_to_watch)
        self.want_to_watch_sort_by.setObjectName(u"want_to_watch_sort_by")
        self.want_to_watch_sort_by.setFrame(False)
        self.want_to_watch_sort_by.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_8.addWidget(self.want_to_watch_sort_by)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.want_to_watch_list = QListWidget(self.movies_want_to_watch)
        self.want_to_watch_list.setObjectName(u"want_to_watch_list")

        self.verticalLayout_10.addWidget(self.want_to_watch_list)


        self.gridLayout_12.addLayout(self.verticalLayout_10, 0, 0, 1, 1)

        self.movies_tap_widget.addTab(self.movies_want_to_watch, "")
        self.movies_continue_later = QWidget()
        self.movies_continue_later.setObjectName(u"movies_continue_later")
        self.gridLayout_9 = QGridLayout(self.movies_continue_later)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 9, 0, 0)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, 10, -1)
        self.continue_later_search = QLineEdit(self.movies_continue_later)
        self.continue_later_search.setObjectName(u"continue_later_search")
        self.continue_later_search.setMaximumSize(QSize(200, 30))
        self.continue_later_search.setStyleSheet(u"QLineEdit {\n"
"    color: rgb(0, 0, 0);\n"
"    font-size: 14px;\n"
"    background-color: transparent;\n"
"    padding: 6px;\n"
"    border: none;\n"
"    border-bottom: 1px solid rgba(221, 221, 221, 100); /* \u0642\u0628\u0644 \u0627\u0644\u062a\u0631\u0643\u064a\u0632 */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgba(73, 133, 224, 0.12); /* \u0632\u064a input-hovered-color */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    outline: none;\n"
"    border-bottom: 2px solid #5891ff; /* \u0628\u0639\u062f \u0627\u0644\u062a\u0631\u0643\u064a\u0632 */\n"
"}\n"
"")
        self.continue_later_search.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.continue_later_search)

        self.line_7 = QFrame(self.movies_continue_later)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_9.addWidget(self.line_7)

        self.continue_later_random_button = QPushButton(self.movies_continue_later)
        self.continue_later_random_button.setObjectName(u"continue_later_random_button")
        self.continue_later_random_button.setAutoFillBackground(False)
        self.continue_later_random_button.setIcon(icon7)
        self.continue_later_random_button.setIconSize(QSize(50, 30))
        self.continue_later_random_button.setFlat(True)

        self.horizontalLayout_9.addWidget(self.continue_later_random_button)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.line_8 = QFrame(self.movies_continue_later)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_9.addWidget(self.line_8)

        self.continue_later_sort_by = QComboBox(self.movies_continue_later)
        self.continue_later_sort_by.setObjectName(u"continue_later_sort_by")
        self.continue_later_sort_by.setFrame(False)
        self.continue_later_sort_by.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_9.addWidget(self.continue_later_sort_by)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.continue_later_list = QListWidget(self.movies_continue_later)
        self.continue_later_list.setObjectName(u"continue_later_list")

        self.verticalLayout_11.addWidget(self.continue_later_list)


        self.gridLayout_9.addLayout(self.verticalLayout_11, 0, 0, 1, 1)

        self.movies_tap_widget.addTab(self.movies_continue_later, "")
        self.movies_dont_want_to_watch = QWidget()
        self.movies_dont_want_to_watch.setObjectName(u"movies_dont_want_to_watch")
        self.gridLayout_10 = QGridLayout(self.movies_dont_want_to_watch)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, 10, -1)
        self.dont_want_to_continue_search = QLineEdit(self.movies_dont_want_to_watch)
        self.dont_want_to_continue_search.setObjectName(u"dont_want_to_continue_search")
        self.dont_want_to_continue_search.setMaximumSize(QSize(200, 30))
        self.dont_want_to_continue_search.setStyleSheet(u"QLineEdit {\n"
"    color: rgb(0, 0, 0);\n"
"    font-size: 14px;\n"
"    background-color: transparent;\n"
"    padding: 6px;\n"
"    border: none;\n"
"    border-bottom: 1px solid rgba(221, 221, 221, 100); /* \u0642\u0628\u0644 \u0627\u0644\u062a\u0631\u0643\u064a\u0632 */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgba(73, 133, 224, 0.12); /* \u0632\u064a input-hovered-color */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    outline: none;\n"
"    border-bottom: 2px solid #5891ff; /* \u0628\u0639\u062f \u0627\u0644\u062a\u0631\u0643\u064a\u0632 */\n"
"}\n"
"")
        self.dont_want_to_continue_search.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.dont_want_to_continue_search)

        self.line_9 = QFrame(self.movies_dont_want_to_watch)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_10.addWidget(self.line_9)

        self.dont_want_to_continue_random_button = QPushButton(self.movies_dont_want_to_watch)
        self.dont_want_to_continue_random_button.setObjectName(u"dont_want_to_continue_random_button")
        self.dont_want_to_continue_random_button.setAutoFillBackground(False)
        self.dont_want_to_continue_random_button.setIcon(icon7)
        self.dont_want_to_continue_random_button.setIconSize(QSize(50, 30))
        self.dont_want_to_continue_random_button.setFlat(True)

        self.horizontalLayout_10.addWidget(self.dont_want_to_continue_random_button)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.line_10 = QFrame(self.movies_dont_want_to_watch)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_10.addWidget(self.line_10)

        self.dont_want_to_continue_sort_by = QComboBox(self.movies_dont_want_to_watch)
        self.dont_want_to_continue_sort_by.setObjectName(u"dont_want_to_continue_sort_by")
        self.dont_want_to_continue_sort_by.setFrame(False)
        self.dont_want_to_continue_sort_by.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_10.addWidget(self.dont_want_to_continue_sort_by)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)

        self.dont_want_to_continue_list = QListWidget(self.movies_dont_want_to_watch)
        self.dont_want_to_continue_list.setObjectName(u"dont_want_to_continue_list")

        self.verticalLayout_12.addWidget(self.dont_want_to_continue_list)


        self.gridLayout_10.addLayout(self.verticalLayout_12, 0, 0, 1, 1)

        self.movies_tap_widget.addTab(self.movies_dont_want_to_watch, "")
        self.movies_ended = QWidget()
        self.movies_ended.setObjectName(u"movies_ended")
        self.gridLayout_11 = QGridLayout(self.movies_ended)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, 10, -1)
        self.watched_search = QLineEdit(self.movies_ended)
        self.watched_search.setObjectName(u"watched_search")
        self.watched_search.setMaximumSize(QSize(200, 30))
        self.watched_search.setStyleSheet(u"QLineEdit {\n"
"    color: rgb(0, 0, 0);\n"
"    font-size: 14px;\n"
"    background-color: transparent;\n"
"    padding: 6px;\n"
"    border: none;\n"
"    border-bottom: 1px solid rgba(221, 221, 221, 100); /* \u0642\u0628\u0644 \u0627\u0644\u062a\u0631\u0643\u064a\u0632 */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgba(73, 133, 224, 0.12); /* \u0632\u064a input-hovered-color */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    outline: none;\n"
"    border-bottom: 2px solid #5891ff; /* \u0628\u0639\u062f \u0627\u0644\u062a\u0631\u0643\u064a\u0632 */\n"
"}\n"
"")
        self.watched_search.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.watched_search)

        self.line_11 = QFrame(self.movies_ended)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.line_11)

        self.watched_random_button = QPushButton(self.movies_ended)
        self.watched_random_button.setObjectName(u"watched_random_button")
        self.watched_random_button.setAutoFillBackground(False)
        self.watched_random_button.setIcon(icon7)
        self.watched_random_button.setIconSize(QSize(50, 30))
        self.watched_random_button.setFlat(True)

        self.horizontalLayout_11.addWidget(self.watched_random_button)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)

        self.line_12 = QFrame(self.movies_ended)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.VLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.line_12)

        self.watched_sort_by = QComboBox(self.movies_ended)
        self.watched_sort_by.setObjectName(u"watched_sort_by")
        self.watched_sort_by.setFrame(False)
        self.watched_sort_by.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_11.addWidget(self.watched_sort_by)


        self.verticalLayout_13.addLayout(self.horizontalLayout_11)

        self.watched_list = QListWidget(self.movies_ended)
        self.watched_list.setObjectName(u"watched_list")

        self.verticalLayout_13.addWidget(self.watched_list)


        self.gridLayout_11.addLayout(self.verticalLayout_13, 0, 0, 1, 1)

        self.movies_tap_widget.addTab(self.movies_ended, "")

        self.verticalLayout_3.addWidget(self.movies_tap_widget)


        self.gridLayout_7.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.stacked_body_Widget.addWidget(self.movies_section)
        self.games_section = QWidget()
        self.games_section.setObjectName(u"games_section")
        self.games_section.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.gridLayout_6 = QGridLayout(self.games_section)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(820)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.games_section)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)

        self.pushButton_8 = QPushButton(self.games_section)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setIcon(icon6)
        self.pushButton_8.setIconSize(QSize(60, 60))
        self.pushButton_8.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_8)


        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.movies_tab_Widget_2 = QTabWidget(self.games_section)
        self.movies_tab_Widget_2.setObjectName(u"movies_tab_Widget_2")
        sizePolicy1.setHeightForWidth(self.movies_tab_Widget_2.sizePolicy().hasHeightForWidth())
        self.movies_tab_Widget_2.setSizePolicy(sizePolicy1)
        self.movies_tab_Widget_2.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.movies_tab_Widget_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.movies_tab_Widget_2.setAutoFillBackground(False)
        self.movies_tab_Widget_2.setStyleSheet(u"QTabWidget::pane {\n"
"    border: none;\n"
"    background: #f0f0f0;  /* light clean background */\n"
"}\n"
"\n"
"QTabBar {\n"
"    qproperty-drawBase: 0;\n"
"    alignment: center;  /* center the tabs */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: transparent;\n"
"    color: #444;\n"
"    padding: 10px 25px;\n"
"    margin: 0px 5px;\n"
"    font: 13pt \"Segoe UI\";\n"
"    border-bottom: 3px solid transparent;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    color: #0078d7;  /* accent blue */\n"
"    border-bottom: 3px solid #0078d7;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    color: #005a9e;\n"
"}\n"
"")
        self.movies_tab_Widget_2.setTabPosition(QTabWidget.TabPosition.North)
        self.movies_tab_Widget_2.setTabShape(QTabWidget.TabShape.Rounded)
        self.movies_tab_Widget_2.setElideMode(Qt.TextElideMode.ElideNone)
        self.movies_tab_Widget_2.setTabsClosable(False)
        self.movies_tab_Widget_2.setMovable(False)
        self.movies_tab_Widget_2.setTabBarAutoHide(False)
        self.games_playing = QWidget()
        self.games_playing.setObjectName(u"games_playing")
        self.scrollArea_5 = QScrollArea(self.games_playing)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setGeometry(QRect(0, 0, 1201, 741))
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 1199, 739))
        self.gridLayoutWidget_6 = QWidget(self.scrollAreaWidgetContents_6)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(-10, 0, 1211, 741))
        self.games_grid_1 = QGridLayout(self.gridLayoutWidget_6)
        self.games_grid_1.setObjectName(u"games_grid_1")
        self.games_grid_1.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_6)
        self.movies_tab_Widget_2.addTab(self.games_playing, "")
        self.playing_want_to_play = QWidget()
        self.playing_want_to_play.setObjectName(u"playing_want_to_play")
        self.want_to_do_scrollArea_2 = QScrollArea(self.playing_want_to_play)
        self.want_to_do_scrollArea_2.setObjectName(u"want_to_do_scrollArea_2")
        self.want_to_do_scrollArea_2.setGeometry(QRect(0, 0, 1201, 741))
        self.want_to_do_scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 1199, 739))
        self.gridLayoutWidget_7 = QWidget(self.scrollAreaWidgetContents_7)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(0, 0, 1201, 741))
        self.games_grid_2 = QGridLayout(self.gridLayoutWidget_7)
        self.games_grid_2.setObjectName(u"games_grid_2")
        self.games_grid_2.setContentsMargins(0, 0, 0, 0)
        self.want_to_do_scrollArea_2.setWidget(self.scrollAreaWidgetContents_7)
        self.movies_tab_Widget_2.addTab(self.playing_want_to_play, "")
        self.games_continue_later = QWidget()
        self.games_continue_later.setObjectName(u"games_continue_later")
        self.scrollArea_6 = QScrollArea(self.games_continue_later)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setGeometry(QRect(0, 0, 1201, 741))
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 1199, 739))
        self.gridLayoutWidget_8 = QWidget(self.scrollAreaWidgetContents_8)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(0, 0, 1201, 741))
        self.games_grid_3 = QGridLayout(self.gridLayoutWidget_8)
        self.games_grid_3.setObjectName(u"games_grid_3")
        self.games_grid_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_8)
        self.movies_tab_Widget_2.addTab(self.games_continue_later, "")
        self.playing_dont_want_to_play = QWidget()
        self.playing_dont_want_to_play.setObjectName(u"playing_dont_want_to_play")
        self.scrollArea_7 = QScrollArea(self.playing_dont_want_to_play)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setGeometry(QRect(0, 0, 1201, 741))
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 1199, 739))
        self.gridLayoutWidget_9 = QWidget(self.scrollAreaWidgetContents_9)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(0, 0, 1211, 731))
        self.games_grid_4 = QGridLayout(self.gridLayoutWidget_9)
        self.games_grid_4.setObjectName(u"games_grid_4")
        self.games_grid_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_9)
        self.movies_tab_Widget_2.addTab(self.playing_dont_want_to_play, "")
        self.playing_ended = QWidget()
        self.playing_ended.setObjectName(u"playing_ended")
        self.scrollArea_8 = QScrollArea(self.playing_ended)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setGeometry(QRect(0, 0, 1201, 741))
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 1199, 739))
        self.gridLayoutWidget_10 = QWidget(self.scrollAreaWidgetContents_10)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(0, 0, 1201, 741))
        self.games_grid_5 = QGridLayout(self.gridLayoutWidget_10)
        self.games_grid_5.setObjectName(u"games_grid_5")
        self.games_grid_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_10)
        self.movies_tab_Widget_2.addTab(self.playing_ended, "")

        self.gridLayout_6.addWidget(self.movies_tab_Widget_2, 1, 0, 1, 1)

        self.stacked_body_Widget.addWidget(self.games_section)
        self.books_section = QWidget()
        self.books_section.setObjectName(u"books_section")
        self.books_section.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.gridLayout_5 = QGridLayout(self.books_section)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(870)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.books_section)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.pushButton_9 = QPushButton(self.books_section)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setIcon(icon6)
        self.pushButton_9.setIconSize(QSize(60, 60))
        self.pushButton_9.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_9)


        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.movies_tab_Widget_3 = QTabWidget(self.books_section)
        self.movies_tab_Widget_3.setObjectName(u"movies_tab_Widget_3")
        sizePolicy1.setHeightForWidth(self.movies_tab_Widget_3.sizePolicy().hasHeightForWidth())
        self.movies_tab_Widget_3.setSizePolicy(sizePolicy1)
        self.movies_tab_Widget_3.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.movies_tab_Widget_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.movies_tab_Widget_3.setAutoFillBackground(False)
        self.movies_tab_Widget_3.setStyleSheet(u"QTabWidget::pane {\n"
"    border: none;\n"
"    background: #f0f0f0;  /* light clean background */\n"
"}\n"
"\n"
"QTabBar {\n"
"    qproperty-drawBase: 0;\n"
"    alignment: center;  /* center the tabs */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: transparent;\n"
"    color: #444;\n"
"    padding: 10px 25px;\n"
"    margin: 0px 5px;\n"
"    font: 13pt \"Segoe UI\";\n"
"    border-bottom: 3px solid transparent;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    color: #0078d7;  /* accent blue */\n"
"    border-bottom: 3px solid #0078d7;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    color: #005a9e;\n"
"}\n"
"")
        self.movies_tab_Widget_3.setTabPosition(QTabWidget.TabPosition.North)
        self.movies_tab_Widget_3.setTabShape(QTabWidget.TabShape.Rounded)
        self.movies_tab_Widget_3.setElideMode(Qt.TextElideMode.ElideNone)
        self.movies_tab_Widget_3.setTabsClosable(False)
        self.movies_tab_Widget_3.setMovable(False)
        self.movies_tab_Widget_3.setTabBarAutoHide(False)
        self.books_reading = QWidget()
        self.books_reading.setObjectName(u"books_reading")
        self.scrollArea_9 = QScrollArea(self.books_reading)
        self.scrollArea_9.setObjectName(u"scrollArea_9")
        self.scrollArea_9.setGeometry(QRect(0, 0, 1201, 741))
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 1199, 739))
        self.gridLayoutWidget_11 = QWidget(self.scrollAreaWidgetContents_11)
        self.gridLayoutWidget_11.setObjectName(u"gridLayoutWidget_11")
        self.gridLayoutWidget_11.setGeometry(QRect(-10, 0, 1211, 741))
        self.books_grid_1 = QGridLayout(self.gridLayoutWidget_11)
        self.books_grid_1.setObjectName(u"books_grid_1")
        self.books_grid_1.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_11)
        self.movies_tab_Widget_3.addTab(self.books_reading, "")
        self.books_want_to_read = QWidget()
        self.books_want_to_read.setObjectName(u"books_want_to_read")
        self.want_to_do_scrollArea_3 = QScrollArea(self.books_want_to_read)
        self.want_to_do_scrollArea_3.setObjectName(u"want_to_do_scrollArea_3")
        self.want_to_do_scrollArea_3.setGeometry(QRect(0, 0, 1201, 741))
        self.want_to_do_scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_12 = QWidget()
        self.scrollAreaWidgetContents_12.setObjectName(u"scrollAreaWidgetContents_12")
        self.scrollAreaWidgetContents_12.setGeometry(QRect(0, 0, 1199, 739))
        self.gridLayoutWidget_12 = QWidget(self.scrollAreaWidgetContents_12)
        self.gridLayoutWidget_12.setObjectName(u"gridLayoutWidget_12")
        self.gridLayoutWidget_12.setGeometry(QRect(0, 0, 1201, 741))
        self.books_grid_2 = QGridLayout(self.gridLayoutWidget_12)
        self.books_grid_2.setObjectName(u"books_grid_2")
        self.books_grid_2.setContentsMargins(0, 0, 0, 0)
        self.want_to_do_scrollArea_3.setWidget(self.scrollAreaWidgetContents_12)
        self.movies_tab_Widget_3.addTab(self.books_want_to_read, "")
        self.books_continue_later = QWidget()
        self.books_continue_later.setObjectName(u"books_continue_later")
        self.scrollArea_10 = QScrollArea(self.books_continue_later)
        self.scrollArea_10.setObjectName(u"scrollArea_10")
        self.scrollArea_10.setGeometry(QRect(0, 0, 1201, 741))
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollAreaWidgetContents_13 = QWidget()
        self.scrollAreaWidgetContents_13.setObjectName(u"scrollAreaWidgetContents_13")
        self.scrollAreaWidgetContents_13.setGeometry(QRect(0, 0, 1199, 739))
        self.gridLayoutWidget_13 = QWidget(self.scrollAreaWidgetContents_13)
        self.gridLayoutWidget_13.setObjectName(u"gridLayoutWidget_13")
        self.gridLayoutWidget_13.setGeometry(QRect(0, 0, 1201, 741))
        self.books_grid_3 = QGridLayout(self.gridLayoutWidget_13)
        self.books_grid_3.setObjectName(u"books_grid_3")
        self.books_grid_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_13)
        self.movies_tab_Widget_3.addTab(self.books_continue_later, "")
        self.books_dont_want_to_read = QWidget()
        self.books_dont_want_to_read.setObjectName(u"books_dont_want_to_read")
        self.books_dont_want_to_read.setStyleSheet(u"QStackedWidget {\n"
"    background-color: rgb(128, 128, 128);\n"
"}\n"
"")
        self.scrollArea_11 = QScrollArea(self.books_dont_want_to_read)
        self.scrollArea_11.setObjectName(u"scrollArea_11")
        self.scrollArea_11.setGeometry(QRect(0, 0, 1201, 741))
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollAreaWidgetContents_14 = QWidget()
        self.scrollAreaWidgetContents_14.setObjectName(u"scrollAreaWidgetContents_14")
        self.scrollAreaWidgetContents_14.setGeometry(QRect(0, 0, 1199, 739))
        self.gridLayoutWidget_14 = QWidget(self.scrollAreaWidgetContents_14)
        self.gridLayoutWidget_14.setObjectName(u"gridLayoutWidget_14")
        self.gridLayoutWidget_14.setGeometry(QRect(0, 0, 1201, 751))
        self.books_grid_4 = QGridLayout(self.gridLayoutWidget_14)
        self.books_grid_4.setObjectName(u"books_grid_4")
        self.books_grid_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_14)
        self.movies_tab_Widget_3.addTab(self.books_dont_want_to_read, "")
        self.books_ended = QWidget()
        self.books_ended.setObjectName(u"books_ended")
        self.scrollArea_12 = QScrollArea(self.books_ended)
        self.scrollArea_12.setObjectName(u"scrollArea_12")
        self.scrollArea_12.setGeometry(QRect(0, 0, 1201, 741))
        self.scrollArea_12.setWidgetResizable(True)
        self.scrollAreaWidgetContents_15 = QWidget()
        self.scrollAreaWidgetContents_15.setObjectName(u"scrollAreaWidgetContents_15")
        self.scrollAreaWidgetContents_15.setGeometry(QRect(0, 0, 1199, 739))
        self.gridLayoutWidget_15 = QWidget(self.scrollAreaWidgetContents_15)
        self.gridLayoutWidget_15.setObjectName(u"gridLayoutWidget_15")
        self.gridLayoutWidget_15.setGeometry(QRect(0, 0, 1201, 741))
        self.books_grid_5 = QGridLayout(self.gridLayoutWidget_15)
        self.books_grid_5.setObjectName(u"books_grid_5")
        self.books_grid_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_12.setWidget(self.scrollAreaWidgetContents_15)
        self.movies_tab_Widget_3.addTab(self.books_ended, "")

        self.gridLayout_5.addWidget(self.movies_tab_Widget_3, 1, 0, 1, 1)

        self.stacked_body_Widget.addWidget(self.books_section)
        self.comics_section = QWidget()
        self.comics_section.setObjectName(u"comics_section")
        self.comics_section.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.gridLayout_4 = QGridLayout(self.comics_section)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(920)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.comics_section)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.pushButton_10 = QPushButton(self.comics_section)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setAutoFillBackground(False)
        self.pushButton_10.setIcon(icon6)
        self.pushButton_10.setIconSize(QSize(60, 60))
        self.pushButton_10.setFlat(True)

        self.horizontalLayout_4.addWidget(self.pushButton_10)


        self.gridLayout_4.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.movies_tab_Widget_4 = QTabWidget(self.comics_section)
        self.movies_tab_Widget_4.setObjectName(u"movies_tab_Widget_4")
        sizePolicy1.setHeightForWidth(self.movies_tab_Widget_4.sizePolicy().hasHeightForWidth())
        self.movies_tab_Widget_4.setSizePolicy(sizePolicy1)
        self.movies_tab_Widget_4.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.movies_tab_Widget_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.movies_tab_Widget_4.setAutoFillBackground(False)
        self.movies_tab_Widget_4.setStyleSheet(u"QTabWidget::pane {\n"
"    border: none;\n"
"    background: #f0f0f0;  /* light clean background */\n"
"}\n"
"\n"
"QTabBar {\n"
"    qproperty-drawBase: 0;\n"
"    alignment: center;  /* center the tabs */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: transparent;\n"
"    color: #444;\n"
"    padding: 10px 25px;\n"
"    margin: 0px 5px;\n"
"    font: 13pt \"Segoe UI\";\n"
"    border-bottom: 3px solid transparent;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    color: #0078d7;  /* accent blue */\n"
"    border-bottom: 3px solid #0078d7;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    color: #005a9e;\n"
"}\n"
"")
        self.movies_tab_Widget_4.setTabPosition(QTabWidget.TabPosition.North)
        self.movies_tab_Widget_4.setTabShape(QTabWidget.TabShape.Rounded)
        self.movies_tab_Widget_4.setElideMode(Qt.TextElideMode.ElideNone)
        self.movies_tab_Widget_4.setTabsClosable(False)
        self.movies_tab_Widget_4.setMovable(False)
        self.movies_tab_Widget_4.setTabBarAutoHide(False)
        self.comics_reading = QWidget()
        self.comics_reading.setObjectName(u"comics_reading")
        self.scrollArea_13 = QScrollArea(self.comics_reading)
        self.scrollArea_13.setObjectName(u"scrollArea_13")
        self.scrollArea_13.setGeometry(QRect(0, 0, 1201, 741))
        self.scrollArea_13.setWidgetResizable(True)
        self.scrollAreaWidgetContents_16 = QWidget()
        self.scrollAreaWidgetContents_16.setObjectName(u"scrollAreaWidgetContents_16")
        self.scrollAreaWidgetContents_16.setGeometry(QRect(0, 0, 1199, 739))
        self.gridLayoutWidget_16 = QWidget(self.scrollAreaWidgetContents_16)
        self.gridLayoutWidget_16.setObjectName(u"gridLayoutWidget_16")
        self.gridLayoutWidget_16.setGeometry(QRect(-10, 0, 1211, 741))
        self.comics_grid_1 = QGridLayout(self.gridLayoutWidget_16)
        self.comics_grid_1.setObjectName(u"comics_grid_1")
        self.comics_grid_1.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_13.setWidget(self.scrollAreaWidgetContents_16)
        self.movies_tab_Widget_4.addTab(self.comics_reading, "")
        self.comics_want_to_read = QWidget()
        self.comics_want_to_read.setObjectName(u"comics_want_to_read")
        self.want_to_do_scrollArea_4 = QScrollArea(self.comics_want_to_read)
        self.want_to_do_scrollArea_4.setObjectName(u"want_to_do_scrollArea_4")
        self.want_to_do_scrollArea_4.setGeometry(QRect(0, 0, 1201, 741))
        self.want_to_do_scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_17 = QWidget()
        self.scrollAreaWidgetContents_17.setObjectName(u"scrollAreaWidgetContents_17")
        self.scrollAreaWidgetContents_17.setGeometry(QRect(0, 0, 1199, 739))
        self.gridLayoutWidget_17 = QWidget(self.scrollAreaWidgetContents_17)
        self.gridLayoutWidget_17.setObjectName(u"gridLayoutWidget_17")
        self.gridLayoutWidget_17.setGeometry(QRect(0, 0, 1201, 741))
        self.comics_grid_2 = QGridLayout(self.gridLayoutWidget_17)
        self.comics_grid_2.setObjectName(u"comics_grid_2")
        self.comics_grid_2.setContentsMargins(0, 0, 0, 0)
        self.want_to_do_scrollArea_4.setWidget(self.scrollAreaWidgetContents_17)
        self.movies_tab_Widget_4.addTab(self.comics_want_to_read, "")
        self.comics_continue_later = QWidget()
        self.comics_continue_later.setObjectName(u"comics_continue_later")
        self.scrollArea_14 = QScrollArea(self.comics_continue_later)
        self.scrollArea_14.setObjectName(u"scrollArea_14")
        self.scrollArea_14.setGeometry(QRect(0, 0, 1201, 741))
        self.scrollArea_14.setWidgetResizable(True)
        self.scrollAreaWidgetContents_18 = QWidget()
        self.scrollAreaWidgetContents_18.setObjectName(u"scrollAreaWidgetContents_18")
        self.scrollAreaWidgetContents_18.setGeometry(QRect(0, 0, 1199, 739))
        self.gridLayoutWidget_18 = QWidget(self.scrollAreaWidgetContents_18)
        self.gridLayoutWidget_18.setObjectName(u"gridLayoutWidget_18")
        self.gridLayoutWidget_18.setGeometry(QRect(0, 0, 1201, 741))
        self.comics_grid_3 = QGridLayout(self.gridLayoutWidget_18)
        self.comics_grid_3.setObjectName(u"comics_grid_3")
        self.comics_grid_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_14.setWidget(self.scrollAreaWidgetContents_18)
        self.movies_tab_Widget_4.addTab(self.comics_continue_later, "")
        self.comics_dont_want_to_read = QWidget()
        self.comics_dont_want_to_read.setObjectName(u"comics_dont_want_to_read")
        self.scrollArea_15 = QScrollArea(self.comics_dont_want_to_read)
        self.scrollArea_15.setObjectName(u"scrollArea_15")
        self.scrollArea_15.setGeometry(QRect(0, 0, 1201, 741))
        self.scrollArea_15.setWidgetResizable(True)
        self.scrollAreaWidgetContents_19 = QWidget()
        self.scrollAreaWidgetContents_19.setObjectName(u"scrollAreaWidgetContents_19")
        self.scrollAreaWidgetContents_19.setGeometry(QRect(0, 0, 1199, 739))
        self.gridLayoutWidget_19 = QWidget(self.scrollAreaWidgetContents_19)
        self.gridLayoutWidget_19.setObjectName(u"gridLayoutWidget_19")
        self.gridLayoutWidget_19.setGeometry(QRect(0, 0, 1201, 751))
        self.comics_grid_4 = QGridLayout(self.gridLayoutWidget_19)
        self.comics_grid_4.setObjectName(u"comics_grid_4")
        self.comics_grid_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_15.setWidget(self.scrollAreaWidgetContents_19)
        self.movies_tab_Widget_4.addTab(self.comics_dont_want_to_read, "")
        self.comics_ended = QWidget()
        self.comics_ended.setObjectName(u"comics_ended")
        self.scrollArea_16 = QScrollArea(self.comics_ended)
        self.scrollArea_16.setObjectName(u"scrollArea_16")
        self.scrollArea_16.setGeometry(QRect(0, 0, 1201, 741))
        self.scrollArea_16.setWidgetResizable(True)
        self.scrollAreaWidgetContents_20 = QWidget()
        self.scrollAreaWidgetContents_20.setObjectName(u"scrollAreaWidgetContents_20")
        self.scrollAreaWidgetContents_20.setGeometry(QRect(0, 0, 1199, 739))
        self.gridLayoutWidget_20 = QWidget(self.scrollAreaWidgetContents_20)
        self.gridLayoutWidget_20.setObjectName(u"gridLayoutWidget_20")
        self.gridLayoutWidget_20.setGeometry(QRect(0, 0, 1201, 741))
        self.comics_grid_5 = QGridLayout(self.gridLayoutWidget_20)
        self.comics_grid_5.setObjectName(u"comics_grid_5")
        self.comics_grid_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_16.setWidget(self.scrollAreaWidgetContents_20)
        self.movies_tab_Widget_4.addTab(self.comics_ended, "")

        self.gridLayout_4.addWidget(self.movies_tab_Widget_4, 1, 0, 1, 1)

        self.stacked_body_Widget.addWidget(self.comics_section)
        self.setting_section = QWidget()
        self.setting_section.setObjectName(u"setting_section")
        self.setting_section.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.gridLayout_8 = QGridLayout(self.setting_section)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_6 = QLabel(self.setting_section)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.stacked_body_Widget.addWidget(self.setting_section)

        self.gridLayout_2.addWidget(self.stacked_body_Widget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.main_body_widget, 0, 1, 1, 1)

        QWidget.setTabOrder(self.home_button, self.movies_button)
        QWidget.setTabOrder(self.movies_button, self.games_button)
        QWidget.setTabOrder(self.games_button, self.books_button)
        QWidget.setTabOrder(self.books_button, self.comics_button)
        QWidget.setTabOrder(self.comics_button, self.setting_button)

        self.retranslateUi(main_widget)

        self.stacked_body_Widget.setCurrentIndex(0)
        self.movies_tap_widget.setCurrentIndex(0)
        self.movies_tab_Widget_2.setCurrentIndex(0)
        self.movies_tab_Widget_3.setCurrentIndex(0)
        self.movies_tab_Widget_4.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main_widget)
    # setupUi

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QCoreApplication.translate("main_widget", u"Form", None))
        self.home_button.setText("")
        self.movies_button.setText("")
        self.games_button.setText("")
        self.books_button.setText("")
        self.comics_button.setText("")
        self.setting_button.setText("")
        self.label_2.setText(QCoreApplication.translate("main_widget", u"This app is designed to be your perfect library for (movies, series, games, etc.)", None))
        self.label.setText(QCoreApplication.translate("main_widget", u"Welcome, to your libirary", None))
        self.movies_label.setText(QCoreApplication.translate("main_widget", u" Movies", None))
#if QT_CONFIG(tooltip)
        self.movies_add_botton.setToolTip(QCoreApplication.translate("main_widget", u"Add a new movie", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.movies_add_botton.setStatusTip(QCoreApplication.translate("main_widget", u"Add a new movie", None))
#endif // QT_CONFIG(statustip)
        self.movies_add_botton.setText("")
#if QT_CONFIG(shortcut)
        self.movies_add_botton.setShortcut(QCoreApplication.translate("main_widget", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.watching_search.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
        self.watching_random_button.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.wahtching_sort_box.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort by", None))
        self.movies_tap_widget.setTabText(self.movies_tap_widget.indexOf(self.movies_watching), QCoreApplication.translate("main_widget", u"       Watching        ", None))
        self.want_to_watch_search.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
        self.want_to_watch_random_button.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.want_to_watch_sort_by.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort by", None))
        self.movies_tap_widget.setTabText(self.movies_tap_widget.indexOf(self.movies_want_to_watch), QCoreApplication.translate("main_widget", u"  Want To Watch ", None))
        self.continue_later_search.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
        self.continue_later_random_button.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.continue_later_sort_by.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort by", None))
        self.movies_tap_widget.setTabText(self.movies_tap_widget.indexOf(self.movies_continue_later), QCoreApplication.translate("main_widget", u"    Continue Later   ", None))
        self.dont_want_to_continue_search.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
        self.dont_want_to_continue_random_button.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.dont_want_to_continue_sort_by.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort by", None))
        self.movies_tap_widget.setTabText(self.movies_tap_widget.indexOf(self.movies_dont_want_to_watch), QCoreApplication.translate("main_widget", u"    Dont Wnat To Continue ", None))
        self.watched_search.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
        self.watched_random_button.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.watched_sort_by.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort by", None))
        self.movies_tap_widget.setTabText(self.movies_tap_widget.indexOf(self.movies_ended), QCoreApplication.translate("main_widget", u"       Watched        ", None))
        self.label_3.setText(QCoreApplication.translate("main_widget", u"Games", None))
#if QT_CONFIG(tooltip)
        self.pushButton_8.setToolTip(QCoreApplication.translate("main_widget", u"Add a new movie or serie", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_8.setStatusTip(QCoreApplication.translate("main_widget", u"Add a new movie or serie", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_8.setText("")
        self.movies_tab_Widget_2.setTabText(self.movies_tab_Widget_2.indexOf(self.games_playing), QCoreApplication.translate("main_widget", u"       Playing        ", None))
        self.movies_tab_Widget_2.setTabText(self.movies_tab_Widget_2.indexOf(self.playing_want_to_play), QCoreApplication.translate("main_widget", u"  Want to play  ", None))
        self.movies_tab_Widget_2.setTabText(self.movies_tab_Widget_2.indexOf(self.games_continue_later), QCoreApplication.translate("main_widget", u"    Continue Later   ", None))
        self.movies_tab_Widget_2.setTabText(self.movies_tab_Widget_2.indexOf(self.playing_dont_want_to_play), QCoreApplication.translate("main_widget", u"    Dont wnat to play ", None))
        self.movies_tab_Widget_2.setTabText(self.movies_tab_Widget_2.indexOf(self.playing_ended), QCoreApplication.translate("main_widget", u"       ended        ", None))
        self.label_4.setText(QCoreApplication.translate("main_widget", u"Books", None))
#if QT_CONFIG(tooltip)
        self.pushButton_9.setToolTip(QCoreApplication.translate("main_widget", u"Add a new movie or serie", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_9.setStatusTip(QCoreApplication.translate("main_widget", u"Add a new movie or serie", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_9.setText("")
        self.movies_tab_Widget_3.setTabText(self.movies_tab_Widget_3.indexOf(self.books_reading), QCoreApplication.translate("main_widget", u"       Reading        ", None))
        self.movies_tab_Widget_3.setTabText(self.movies_tab_Widget_3.indexOf(self.books_want_to_read), QCoreApplication.translate("main_widget", u"  Want to read  ", None))
        self.movies_tab_Widget_3.setTabText(self.movies_tab_Widget_3.indexOf(self.books_continue_later), QCoreApplication.translate("main_widget", u"    Continue Later   ", None))
        self.movies_tab_Widget_3.setTabText(self.movies_tab_Widget_3.indexOf(self.books_dont_want_to_read), QCoreApplication.translate("main_widget", u"    Dont wnat to read ", None))
        self.movies_tab_Widget_3.setTabText(self.movies_tab_Widget_3.indexOf(self.books_ended), QCoreApplication.translate("main_widget", u"       Ended        ", None))
        self.label_5.setText(QCoreApplication.translate("main_widget", u"Comics", None))
#if QT_CONFIG(tooltip)
        self.pushButton_10.setToolTip(QCoreApplication.translate("main_widget", u"Add a new movie or serie", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_10.setStatusTip(QCoreApplication.translate("main_widget", u"Add a new movie or serie", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_10.setText("")
        self.movies_tab_Widget_4.setTabText(self.movies_tab_Widget_4.indexOf(self.comics_reading), QCoreApplication.translate("main_widget", u"       reading        ", None))
        self.movies_tab_Widget_4.setTabText(self.movies_tab_Widget_4.indexOf(self.comics_want_to_read), QCoreApplication.translate("main_widget", u"  Want to read  ", None))
        self.movies_tab_Widget_4.setTabText(self.movies_tab_Widget_4.indexOf(self.comics_continue_later), QCoreApplication.translate("main_widget", u"    countinu Later   ", None))
        self.movies_tab_Widget_4.setTabText(self.movies_tab_Widget_4.indexOf(self.comics_dont_want_to_read), QCoreApplication.translate("main_widget", u"    Dont wnat to read ", None))
        self.movies_tab_Widget_4.setTabText(self.movies_tab_Widget_4.indexOf(self.comics_ended), QCoreApplication.translate("main_widget", u"       ended        ", None))
        self.label_6.setText(QCoreApplication.translate("main_widget", u"Setting", None))
    # retranslateUi

