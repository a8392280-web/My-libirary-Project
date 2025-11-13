# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'movies_showFVFRkv.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import py_ui.resources_rc

class Ui_show(object):
    def setupUi(self, show):
        if not show.objectName():
            show.setObjectName(u"show")
        show.resize(600, 410)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(show.sizePolicy().hasHeightForWidth())
        show.setSizePolicy(sizePolicy)
        show.setMinimumSize(QSize(600, 410))
        show.setMaximumSize(QSize(600, 410))
        show.setStyleSheet(u"QLineEdit {\n"
"    color: #e0e6f0; /* light gray text for dark bg */\n"
"    font-size: 14px;\n"
"    background-color: rgba(255, 255, 255, 0.05); /* slightly visible bg for input field */\n"
"    padding: 6px;\n"
"    border: none;\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 0.2); /* soft light line before focus */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgba(255, 255, 255, 0.1); /* slightly brighter on hover */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    outline: none;\n"
"    border-bottom: 2px solid #5891ff; /* bright blue focus line */\n"
"    background-color: rgba(255, 255, 255, 0.12);\n"
"}\n"
"\n"
"QLabel#show_image_lable {\n"
"    border: 1px solid white;   /* White border */\n"
"    border-radius: 6px;        /* Rounded corners (optional) */\n"
"    padding: 4px;              /* Space inside */\n"
"}\n"
"\n"
"QWidget { \n"
"	background-color: #2b3640;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: #e0e6f0; /* light text */\n"
"    font-size: 14px;\n"
""
                        "    background-color: #2e3a4b; /* dark gray-blue button */\n"
"    border: 1px solid rgba(255, 255, 255, 0.15);\n"
"    border-radius: 6px;\n"
"    padding: 6px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c4d63; /* lighter on hover */\n"
"    border: 1px solid #5891ff; /* subtle blue glow */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1e2a3a; /* darker when pressed */\n"
"    border: 1px solid #4f7de0;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: rgba(255, 255, 255, 0.4);\n"
"    background-color: rgba(255, 255, 255, 0.05);\n"
"    border: 1px solid rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"QComboBox {\n"
"    color: #e0e6f0; /* light text */\n"
"    font-size: 14px;\n"
"    background-color: rgba(255, 255, 255, 0.05); /* subtle transparent bg */\n"
"    border: 1px solid rgba(255, 255, 255, 0.15);\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    border: 1px sol"
                        "id #5891ff; /* subtle blue border */\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #5891ff;\n"
"    background-color: rgba(255, 255, 255, 0.12);\n"
"    outline: none;\n"
"}\n"
"\n"
"/* \u25bc Dropdown arrow */\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 25px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/Icons/sort_by.png); /* replace with your icon */\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"/* Popup (the dropdown list) */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #2e3a4b; /* darker popup background */\n"
"    color: #e0e6f0;\n"
"    border: 1px solid #5891ff;\n"
"    selection-background-color: #3c4d63; /* selected item background */\n"
"    selection-color: #ffffff;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #e0e6f0; /* soft light gray text */\n"
"    font-size: 14px;\n"
"    background-color: transparent; /* blend with bg */\n"
"}\n"
"\n"
"")
        self.gridLayout = QGridLayout(show)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(show)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.show_widget = QWidget()
        self.show_widget.setObjectName(u"show_widget")
        self.gridLayout_2 = QGridLayout(self.show_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.show_image_lable = QLabel(self.show_widget)
        self.show_image_lable.setObjectName(u"show_image_lable")
        self.show_image_lable.setMinimumSize(QSize(180, 270))
        self.show_image_lable.setMaximumSize(QSize(180, 270))
        self.show_image_lable.setStyleSheet(u"QLabel {\n"
"    border: 1px solid white;   /* White border */\n"
"    border-radius: 6px;        /* Rounded corners (optional) */\n"
"    padding: 4px;              /* Space inside */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.show_image_lable)

        self.move_to_combobox = QComboBox(self.show_widget)
        self.move_to_combobox.setObjectName(u"move_to_combobox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.move_to_combobox.sizePolicy().hasHeightForWidth())
        self.move_to_combobox.setSizePolicy(sizePolicy1)
        self.move_to_combobox.setMinimumSize(QSize(100, 0))
        self.move_to_combobox.setMaximumSize(QSize(100, 16777215))
        self.move_to_combobox.setStyleSheet(u"")
        self.move_to_combobox.setFrame(False)

        self.verticalLayout_2.addWidget(self.move_to_combobox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(28, 6, -1, 6)
        self.show_name_lable = QLabel(self.show_widget)
        self.show_name_lable.setObjectName(u"show_name_lable")
        self.show_name_lable.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        self.show_name_lable.setFont(font)
        self.show_name_lable.setStyleSheet(u"")
        self.show_name_lable.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.show_name_lable)

        self.show_time_lable = QLabel(self.show_widget)
        self.show_time_lable.setObjectName(u"show_time_lable")
        self.show_time_lable.setMaximumSize(QSize(16777215, 50))
        self.show_time_lable.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.show_time_lable)

        self.show_label = QLabel(self.show_widget)
        self.show_label.setObjectName(u"show_label")
        self.show_label.setMaximumSize(QSize(1111111, 50))
        self.show_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.show_label)

        self.show_gener_lable = QLabel(self.show_widget)
        self.show_gener_lable.setObjectName(u"show_gener_lable")
        self.show_gener_lable.setMaximumSize(QSize(16777215, 50))
        self.show_gener_lable.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.show_gener_lable)

        self.show_plot_lable = QLabel(self.show_widget)
        self.show_plot_lable.setObjectName(u"show_plot_lable")
        self.show_plot_lable.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.show_plot_lable)

        self.show_imdb_rate_lable = QLabel(self.show_widget)
        self.show_imdb_rate_lable.setObjectName(u"show_imdb_rate_lable")
        self.show_imdb_rate_lable.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.show_imdb_rate_lable)

        self.show_user_rate_lable = QLabel(self.show_widget)
        self.show_user_rate_lable.setObjectName(u"show_user_rate_lable")
        self.show_user_rate_lable.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.show_user_rate_lable)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 5)
        self.show_edit_button = QPushButton(self.show_widget)
        self.show_edit_button.setObjectName(u"show_edit_button")

        self.horizontalLayout.addWidget(self.show_edit_button)

        self.line_2 = QFrame(self.show_widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.show_delete_button = QPushButton(self.show_widget)
        self.show_delete_button.setObjectName(u"show_delete_button")

        self.horizontalLayout.addWidget(self.show_delete_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.show_apply_button = QPushButton(self.show_widget)
        self.show_apply_button.setObjectName(u"show_apply_button")

        self.horizontalLayout.addWidget(self.show_apply_button)

        self.line_3 = QFrame(self.show_widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.show_cancel_button = QPushButton(self.show_widget)
        self.show_cancel_button.setObjectName(u"show_cancel_button")

        self.horizontalLayout.addWidget(self.show_cancel_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 2, 2)

        self.stackedWidget.addWidget(self.show_widget)
        self.edit_widget = QWidget()
        self.edit_widget.setObjectName(u"edit_widget")
        self.gridLayout_3 = QGridLayout(self.edit_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.show_edit_image_label = QLabel(self.edit_widget)
        self.show_edit_image_label.setObjectName(u"show_edit_image_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.show_edit_image_label.sizePolicy().hasHeightForWidth())
        self.show_edit_image_label.setSizePolicy(sizePolicy2)
        self.show_edit_image_label.setMinimumSize(QSize(180, 270))
        self.show_edit_image_label.setMaximumSize(QSize(180, 270))
        self.show_edit_image_label.setStyleSheet(u"QLabel {\n"
"    border: 1px solid white;   /* White border */\n"
"    border-radius: 6px;        /* Rounded corners (optional) */\n"
"    padding: 4px;              /* Space inside */\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.show_edit_image_label)

        self.show_edit_image_url = QLineEdit(self.edit_widget)
        self.show_edit_image_url.setObjectName(u"show_edit_image_url")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.show_edit_image_url.sizePolicy().hasHeightForWidth())
        self.show_edit_image_url.setSizePolicy(sizePolicy3)

        self.verticalLayout_5.addWidget(self.show_edit_image_url)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 20, -1)
        self.show_edit_name_line = QLineEdit(self.edit_widget)
        self.show_edit_name_line.setObjectName(u"show_edit_name_line")
        self.show_edit_name_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.show_edit_name_line)

        self.show_edit_time_line = QLineEdit(self.edit_widget)
        self.show_edit_time_line.setObjectName(u"show_edit_time_line")
        self.show_edit_time_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.show_edit_time_line)

        self.show_edit_date_line = QLineEdit(self.edit_widget)
        self.show_edit_date_line.setObjectName(u"show_edit_date_line")
        self.show_edit_date_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.show_edit_date_line)

        self.show_edit_gener_line = QLineEdit(self.edit_widget)
        self.show_edit_gener_line.setObjectName(u"show_edit_gener_line")
        self.show_edit_gener_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.show_edit_gener_line)

        self.show_edit_plot_line = QLineEdit(self.edit_widget)
        self.show_edit_plot_line.setObjectName(u"show_edit_plot_line")
        self.show_edit_plot_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.show_edit_plot_line)

        self.show_edit_imdb_rate_line = QLineEdit(self.edit_widget)
        self.show_edit_imdb_rate_line.setObjectName(u"show_edit_imdb_rate_line")
        self.show_edit_imdb_rate_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.show_edit_imdb_rate_line)

        self.show_edit_user_rate_line = QLineEdit(self.edit_widget)
        self.show_edit_user_rate_line.setObjectName(u"show_edit_user_rate_line")
        self.show_edit_user_rate_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.show_edit_user_rate_line)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.show_edit_apply_button = QPushButton(self.edit_widget)
        self.show_edit_apply_button.setObjectName(u"show_edit_apply_button")

        self.horizontalLayout_4.addWidget(self.show_edit_apply_button)

        self.show_edit_cancel_button = QPushButton(self.edit_widget)
        self.show_edit_cancel_button.setObjectName(u"show_edit_cancel_button")

        self.horizontalLayout_4.addWidget(self.show_edit_cancel_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.edit_widget)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.retranslateUi(show)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(show)
    # setupUi

    def retranslateUi(self, show):
        show.setWindowTitle(QCoreApplication.translate("show", u"Form", None))
        self.show_image_lable.setText("")
        self.move_to_combobox.setPlaceholderText(QCoreApplication.translate("show", u"Move to :-", None))
        self.show_name_lable.setText(QCoreApplication.translate("show", u"Name", None))
        self.show_time_lable.setText(QCoreApplication.translate("show", u"Runtime", None))
        self.show_label.setText(QCoreApplication.translate("show", u"Date", None))
        self.show_gener_lable.setText(QCoreApplication.translate("show", u"Gener", None))
        self.show_plot_lable.setText(QCoreApplication.translate("show", u"Plot", None))
        self.show_imdb_rate_lable.setText(QCoreApplication.translate("show", u"IMDB rate", None))
        self.show_user_rate_lable.setText(QCoreApplication.translate("show", u"User rate", None))
        self.show_edit_button.setText(QCoreApplication.translate("show", u"Edit", None))
        self.show_delete_button.setText(QCoreApplication.translate("show", u"Delete", None))
        self.show_apply_button.setText(QCoreApplication.translate("show", u"Apply", None))
        self.show_cancel_button.setText(QCoreApplication.translate("show", u"Cancel", None))
        self.show_edit_image_label.setText("")
        self.show_edit_image_url.setPlaceholderText(QCoreApplication.translate("show", u"   New image URL", None))
        self.show_edit_name_line.setPlaceholderText(QCoreApplication.translate("show", u"Name", None))
        self.show_edit_time_line.setText("")
        self.show_edit_time_line.setPlaceholderText(QCoreApplication.translate("show", u"Runtime", None))
        self.show_edit_date_line.setPlaceholderText(QCoreApplication.translate("show", u"Release", None))
        self.show_edit_gener_line.setPlaceholderText(QCoreApplication.translate("show", u"Genre", None))
        self.show_edit_plot_line.setPlaceholderText(QCoreApplication.translate("show", u"Plot", None))
        self.show_edit_imdb_rate_line.setPlaceholderText(QCoreApplication.translate("show", u"IMDB rate", None))
        self.show_edit_user_rate_line.setPlaceholderText(QCoreApplication.translate("show", u"User rate", None))
        self.show_edit_apply_button.setText(QCoreApplication.translate("show", u"Apply", None))
        self.show_edit_cancel_button.setText(QCoreApplication.translate("show", u"Cancel", None))
    # retranslateUi

