# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui_1jqPrpZ.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QVBoxLayout, QWidget)
import gui.resources_rc

class Ui_main_widget(object):
    def setupUi(self, main_widget):
        if not main_widget.objectName():
            main_widget.setObjectName(u"main_widget")
        main_widget.resize(1278, 850)
        main_widget.setMinimumSize(QSize(1278, 850))
        main_widget.setMaximumSize(QSize(1278, 16777215))
        self.main_body_widget = QWidget(main_widget)
        self.main_body_widget.setObjectName(u"main_body_widget")
        self.main_body_widget.setGeometry(QRect(79, -10, 1201, 861))
        self.main_body_widget.setStyleSheet(u"")
        self.stacked_body_Widget = QStackedWidget(self.main_body_widget)
        self.stacked_body_Widget.setObjectName(u"stacked_body_Widget")
        self.stacked_body_Widget.setEnabled(True)
        self.stacked_body_Widget.setGeometry(QRect(0, 10, 1201, 851))
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
        self.label = QLabel(self.welcome_section)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 601, 71))
        font = QFont()
        font.setFamilies([u"Arial Rounded MT"])
        font.setPointSize(36)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.TextFormat.RichText)
        self.label.setScaledContents(False)
        self.stacked_body_Widget.addWidget(self.welcome_section)
        self.movies_section = QWidget()
        self.movies_section.setObjectName(u"movies_section")
        self.movies_section.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.movies_tab_Widget = QTabWidget(self.movies_section)
        self.movies_tab_Widget.setObjectName(u"movies_tab_Widget")
        self.movies_tab_Widget.setGeometry(QRect(0, 70, 1201, 781))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.movies_tab_Widget.sizePolicy().hasHeightForWidth())
        self.movies_tab_Widget.setSizePolicy(sizePolicy)
        self.movies_tab_Widget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.movies_tab_Widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.movies_tab_Widget.setAutoFillBackground(False)
        self.movies_tab_Widget.setStyleSheet(u"QTabWidget::pane {\n"
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
        self.movies_tab_Widget.setTabPosition(QTabWidget.TabPosition.North)
        self.movies_tab_Widget.setTabShape(QTabWidget.TabShape.Rounded)
        self.movies_tab_Widget.setElideMode(Qt.TextElideMode.ElideNone)
        self.movies_tab_Widget.setTabsClosable(False)
        self.movies_tab_Widget.setMovable(False)
        self.movies_tab_Widget.setTabBarAutoHide(False)
        self.movies_watching = QWidget()
        self.movies_watching.setObjectName(u"movies_watching")
        self.listWidget = QListWidget(self.movies_watching)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 1, 1201, 741))
        self.movies_tab_Widget.addTab(self.movies_watching, "")
        self.movies_want_to_watch = QWidget()
        self.movies_want_to_watch.setObjectName(u"movies_want_to_watch")
        self.listWidget_2 = QListWidget(self.movies_want_to_watch)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(0, 0, 1201, 741))
        self.movies_tab_Widget.addTab(self.movies_want_to_watch, "")
        self.movies_continue_later = QWidget()
        self.movies_continue_later.setObjectName(u"movies_continue_later")
        self.listWidget_3 = QListWidget(self.movies_continue_later)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setGeometry(QRect(0, 1, 1201, 741))
        self.movies_tab_Widget.addTab(self.movies_continue_later, "")
        self.movies_dont_want_to_watch = QWidget()
        self.movies_dont_want_to_watch.setObjectName(u"movies_dont_want_to_watch")
        self.listWidget_4 = QListWidget(self.movies_dont_want_to_watch)
        self.listWidget_4.setObjectName(u"listWidget_4")
        self.listWidget_4.setGeometry(QRect(0, 1, 1201, 741))
        self.movies_tab_Widget.addTab(self.movies_dont_want_to_watch, "")
        self.movies_ended = QWidget()
        self.movies_ended.setObjectName(u"movies_ended")
        self.listWidget_5 = QListWidget(self.movies_ended)
        self.listWidget_5.setObjectName(u"listWidget_5")
        self.listWidget_5.setGeometry(QRect(0, 0, 1201, 741))
        self.movies_tab_Widget.addTab(self.movies_ended, "")
        self.layoutWidget = QWidget(self.movies_section)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 1298, 70))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setSpacing(600)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.movies_label = QLabel(self.layoutWidget)
        self.movies_label.setObjectName(u"movies_label")
        self.movies_label.setFont(font)

        self.horizontalLayout_2.addWidget(self.movies_label)

        self.movies_add_botton = QPushButton(self.layoutWidget)
        self.movies_add_botton.setObjectName(u"movies_add_botton")
        self.movies_add_botton.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/icons/Icons/Add icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.movies_add_botton.setIcon(icon)
        self.movies_add_botton.setIconSize(QSize(60, 60))
        self.movies_add_botton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.movies_add_botton)

        self.stacked_body_Widget.addWidget(self.movies_section)
        self.games_section = QWidget()
        self.games_section.setObjectName(u"games_section")
        self.games_section.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.movies_tab_Widget_2 = QTabWidget(self.games_section)
        self.movies_tab_Widget_2.setObjectName(u"movies_tab_Widget_2")
        self.movies_tab_Widget_2.setGeometry(QRect(0, 70, 1201, 781))
        sizePolicy.setHeightForWidth(self.movies_tab_Widget_2.sizePolicy().hasHeightForWidth())
        self.movies_tab_Widget_2.setSizePolicy(sizePolicy)
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
        self.layoutWidget1 = QWidget(self.games_section)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 0, 1239, 70))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setSpacing(820)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)

        self.pushButton_8 = QPushButton(self.layoutWidget1)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QSize(60, 60))
        self.pushButton_8.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_8)

        self.stacked_body_Widget.addWidget(self.games_section)
        self.books_section = QWidget()
        self.books_section.setObjectName(u"books_section")
        self.books_section.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.movies_tab_Widget_3 = QTabWidget(self.books_section)
        self.movies_tab_Widget_3.setObjectName(u"movies_tab_Widget_3")
        self.movies_tab_Widget_3.setGeometry(QRect(0, 70, 1201, 781))
        sizePolicy.setHeightForWidth(self.movies_tab_Widget_3.sizePolicy().hasHeightForWidth())
        self.movies_tab_Widget_3.setSizePolicy(sizePolicy)
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
        self.layoutWidget2 = QWidget(self.books_section)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 0, 1219, 70))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setSpacing(870)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.pushButton_9 = QPushButton(self.layoutWidget2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setIconSize(QSize(60, 60))
        self.pushButton_9.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_9)

        self.stacked_body_Widget.addWidget(self.books_section)
        self.comics_section = QWidget()
        self.comics_section.setObjectName(u"comics_section")
        self.comics_section.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.movies_tab_Widget_4 = QTabWidget(self.comics_section)
        self.movies_tab_Widget_4.setObjectName(u"movies_tab_Widget_4")
        self.movies_tab_Widget_4.setGeometry(QRect(0, 70, 1201, 781))
        sizePolicy.setHeightForWidth(self.movies_tab_Widget_4.sizePolicy().hasHeightForWidth())
        self.movies_tab_Widget_4.setSizePolicy(sizePolicy)
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
        self.layoutWidget3 = QWidget(self.comics_section)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 0, 1170, 70))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setSpacing(920)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.pushButton_10 = QPushButton(self.layoutWidget3)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setAutoFillBackground(False)
        self.pushButton_10.setIcon(icon)
        self.pushButton_10.setIconSize(QSize(60, 60))
        self.pushButton_10.setFlat(True)

        self.horizontalLayout_4.addWidget(self.pushButton_10)

        self.stacked_body_Widget.addWidget(self.comics_section)
        self.setting_section = QWidget()
        self.setting_section.setObjectName(u"setting_section")
        self.setting_section.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.label_6 = QLabel(self.setting_section)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 0, 391, 71))
        self.label_6.setFont(font)
        self.stacked_body_Widget.addWidget(self.setting_section)
        self.side_widget = QWidget(main_widget)
        self.side_widget.setObjectName(u"side_widget")
        self.side_widget.setGeometry(QRect(0, 0, 82, 851))
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.home_button.setIcon(icon1)
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/movies.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.movies_button.setIcon(icon2)
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
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/games.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.games_button.setIcon(icon3)
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
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/books.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.books_button.setIcon(icon4)
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/comics.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.comics_button.setIcon(icon5)
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
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setting_button.setIcon(icon6)
        self.setting_button.setIconSize(QSize(50, 50))
        self.setting_button.setCheckable(True)
        self.setting_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.setting_button)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        QWidget.setTabOrder(self.home_button, self.movies_button)
        QWidget.setTabOrder(self.movies_button, self.games_button)
        QWidget.setTabOrder(self.games_button, self.books_button)
        QWidget.setTabOrder(self.books_button, self.comics_button)
        QWidget.setTabOrder(self.comics_button, self.setting_button)

        self.retranslateUi(main_widget)

        self.stacked_body_Widget.setCurrentIndex(0)
        self.movies_tab_Widget.setCurrentIndex(0)
        self.movies_tab_Widget_2.setCurrentIndex(0)
        self.movies_tab_Widget_3.setCurrentIndex(0)
        self.movies_tab_Widget_4.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main_widget)
    # setupUi

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QCoreApplication.translate("main_widget", u"Form", None))
        self.label.setText(QCoreApplication.translate("main_widget", u"Welcome, to your libirary", None))
        self.movies_tab_Widget.setTabText(self.movies_tab_Widget.indexOf(self.movies_watching), QCoreApplication.translate("main_widget", u"       Watching        ", None))
        self.movies_tab_Widget.setTabText(self.movies_tab_Widget.indexOf(self.movies_want_to_watch), QCoreApplication.translate("main_widget", u"  Want to Watching  ", None))
        self.movies_tab_Widget.setTabText(self.movies_tab_Widget.indexOf(self.movies_continue_later), QCoreApplication.translate("main_widget", u"    Continue Later   ", None))
        self.movies_tab_Widget.setTabText(self.movies_tab_Widget.indexOf(self.movies_dont_want_to_watch), QCoreApplication.translate("main_widget", u"    Dont wnat to watch ", None))
        self.movies_tab_Widget.setTabText(self.movies_tab_Widget.indexOf(self.movies_ended), QCoreApplication.translate("main_widget", u"       ended        ", None))
        self.movies_label.setText(QCoreApplication.translate("main_widget", u"Movies", None))
#if QT_CONFIG(tooltip)
        self.movies_add_botton.setToolTip(QCoreApplication.translate("main_widget", u"Add a new movie or serie", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.movies_add_botton.setStatusTip(QCoreApplication.translate("main_widget", u"Add a new movie or serie", None))
#endif // QT_CONFIG(statustip)
        self.movies_add_botton.setText("")
        self.movies_tab_Widget_2.setTabText(self.movies_tab_Widget_2.indexOf(self.games_playing), QCoreApplication.translate("main_widget", u"       Playing        ", None))
        self.movies_tab_Widget_2.setTabText(self.movies_tab_Widget_2.indexOf(self.playing_want_to_play), QCoreApplication.translate("main_widget", u"  Want to play  ", None))
        self.movies_tab_Widget_2.setTabText(self.movies_tab_Widget_2.indexOf(self.games_continue_later), QCoreApplication.translate("main_widget", u"    Continue Later   ", None))
        self.movies_tab_Widget_2.setTabText(self.movies_tab_Widget_2.indexOf(self.playing_dont_want_to_play), QCoreApplication.translate("main_widget", u"    Dont wnat to play ", None))
        self.movies_tab_Widget_2.setTabText(self.movies_tab_Widget_2.indexOf(self.playing_ended), QCoreApplication.translate("main_widget", u"       ended        ", None))
        self.label_3.setText(QCoreApplication.translate("main_widget", u"Games", None))
#if QT_CONFIG(tooltip)
        self.pushButton_8.setToolTip(QCoreApplication.translate("main_widget", u"Add a new movie or serie", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_8.setStatusTip(QCoreApplication.translate("main_widget", u"Add a new movie or serie", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_8.setText("")
        self.movies_tab_Widget_3.setTabText(self.movies_tab_Widget_3.indexOf(self.books_reading), QCoreApplication.translate("main_widget", u"       Reading        ", None))
        self.movies_tab_Widget_3.setTabText(self.movies_tab_Widget_3.indexOf(self.books_want_to_read), QCoreApplication.translate("main_widget", u"  Want to read  ", None))
        self.movies_tab_Widget_3.setTabText(self.movies_tab_Widget_3.indexOf(self.books_continue_later), QCoreApplication.translate("main_widget", u"    Continue Later   ", None))
        self.movies_tab_Widget_3.setTabText(self.movies_tab_Widget_3.indexOf(self.books_dont_want_to_read), QCoreApplication.translate("main_widget", u"    Dont wnat to read ", None))
        self.movies_tab_Widget_3.setTabText(self.movies_tab_Widget_3.indexOf(self.books_ended), QCoreApplication.translate("main_widget", u"       Ended        ", None))
        self.label_4.setText(QCoreApplication.translate("main_widget", u"Books", None))
#if QT_CONFIG(tooltip)
        self.pushButton_9.setToolTip(QCoreApplication.translate("main_widget", u"Add a new movie or serie", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_9.setStatusTip(QCoreApplication.translate("main_widget", u"Add a new movie or serie", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_9.setText("")
        self.movies_tab_Widget_4.setTabText(self.movies_tab_Widget_4.indexOf(self.comics_reading), QCoreApplication.translate("main_widget", u"       reading        ", None))
        self.movies_tab_Widget_4.setTabText(self.movies_tab_Widget_4.indexOf(self.comics_want_to_read), QCoreApplication.translate("main_widget", u"  Want to read  ", None))
        self.movies_tab_Widget_4.setTabText(self.movies_tab_Widget_4.indexOf(self.comics_continue_later), QCoreApplication.translate("main_widget", u"    countinu Later   ", None))
        self.movies_tab_Widget_4.setTabText(self.movies_tab_Widget_4.indexOf(self.comics_dont_want_to_read), QCoreApplication.translate("main_widget", u"    Dont wnat to read ", None))
        self.movies_tab_Widget_4.setTabText(self.movies_tab_Widget_4.indexOf(self.comics_ended), QCoreApplication.translate("main_widget", u"       ended        ", None))
        self.label_5.setText(QCoreApplication.translate("main_widget", u"Comics", None))
#if QT_CONFIG(tooltip)
        self.pushButton_10.setToolTip(QCoreApplication.translate("main_widget", u"Add a new movie or serie", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_10.setStatusTip(QCoreApplication.translate("main_widget", u"Add a new movie or serie", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_10.setText("")
        self.label_6.setText(QCoreApplication.translate("main_widget", u"Setting", None))
        self.home_button.setText("")
        self.movies_button.setText("")
        self.games_button.setText("")
        self.books_button.setText("")
        self.comics_button.setText("")
        self.setting_button.setText("")
    # retranslateUi

