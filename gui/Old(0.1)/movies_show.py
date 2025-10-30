# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_ui_1DXSJxI.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

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
        show.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.gridLayout = QGridLayout(show)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(show)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.show_widget = QWidget()
        self.show_widget.setObjectName(u"show_widget")
        self.layoutWidget = QWidget(self.show_widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 571, 391))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.show_image_lable = QLabel(self.layoutWidget)
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

        self.move_to_lable = QComboBox(self.layoutWidget)
        self.move_to_lable.setObjectName(u"move_to_lable")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.move_to_lable.sizePolicy().hasHeightForWidth())
        self.move_to_lable.setSizePolicy(sizePolicy1)
        self.move_to_lable.setMinimumSize(QSize(100, 0))
        self.move_to_lable.setMaximumSize(QSize(100, 16777215))
        self.move_to_lable.setStyleSheet(u"")
        self.move_to_lable.setFrame(False)

        self.verticalLayout_2.addWidget(self.move_to_lable)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(28, -1, -1, -1)
        self.show_name_lable = QLabel(self.layoutWidget)
        self.show_name_lable.setObjectName(u"show_name_lable")
        self.show_name_lable.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(9)
        self.show_name_lable.setFont(font)
        self.show_name_lable.setStyleSheet(u"")
        self.show_name_lable.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.show_name_lable)

        self.show_time_lable = QLabel(self.layoutWidget)
        self.show_time_lable.setObjectName(u"show_time_lable")
        self.show_time_lable.setMaximumSize(QSize(16777215, 50))
        self.show_time_lable.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.show_time_lable)

        self.show_label = QLabel(self.layoutWidget)
        self.show_label.setObjectName(u"show_label")
        self.show_label.setMaximumSize(QSize(1111111, 50))
        self.show_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.show_label)

        self.show_gener_lable = QLabel(self.layoutWidget)
        self.show_gener_lable.setObjectName(u"show_gener_lable")
        self.show_gener_lable.setMaximumSize(QSize(16777215, 50))
        self.show_gener_lable.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.show_gener_lable)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.show_edit_button = QPushButton(self.layoutWidget)
        self.show_edit_button.setObjectName(u"show_edit_button")

        self.horizontalLayout.addWidget(self.show_edit_button)

        self.show_delete_button = QPushButton(self.layoutWidget)
        self.show_delete_button.setObjectName(u"show_delete_button")

        self.horizontalLayout.addWidget(self.show_delete_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.show_apply_button = QPushButton(self.layoutWidget)
        self.show_apply_button.setObjectName(u"show_apply_button")

        self.horizontalLayout.addWidget(self.show_apply_button)

        self.show_cancel_button = QPushButton(self.layoutWidget)
        self.show_cancel_button.setObjectName(u"show_cancel_button")

        self.horizontalLayout.addWidget(self.show_cancel_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.show_widget)
        self.edit_widget = QWidget()
        self.edit_widget.setObjectName(u"edit_widget")
        self.layoutWidget_2 = QWidget(self.edit_widget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 0, 571, 391))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.show_edit_image_label = QLabel(self.layoutWidget_2)
        self.show_edit_image_label.setObjectName(u"show_edit_image_label")
        self.show_edit_image_label.setMinimumSize(QSize(180, 270))
        self.show_edit_image_label.setMaximumSize(QSize(180, 270))
        self.show_edit_image_label.setStyleSheet(u"QLabel {\n"
"    border: 1px solid white;   /* White border */\n"
"    border-radius: 6px;        /* Rounded corners (optional) */\n"
"    padding: 4px;              /* Space inside */\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.show_edit_image_label)

        self.show_edit_image_url = QLineEdit(self.layoutWidget_2)
        self.show_edit_image_url.setObjectName(u"show_edit_image_url")
        self.show_edit_image_url.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_5.addWidget(self.show_edit_image_url)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 20, -1)
        self.show_edit_name_line = QLineEdit(self.layoutWidget_2)
        self.show_edit_name_line.setObjectName(u"show_edit_name_line")
        self.show_edit_name_line.setStyleSheet(u"QLineEdit {\n"
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
        self.show_edit_name_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.show_edit_name_line)

        self.show_edit_time_line = QLineEdit(self.layoutWidget_2)
        self.show_edit_time_line.setObjectName(u"show_edit_time_line")
        self.show_edit_time_line.setStyleSheet(u"QLineEdit {\n"
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
        self.show_edit_time_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.show_edit_time_line)

        self.show_edit_date_line = QLineEdit(self.layoutWidget_2)
        self.show_edit_date_line.setObjectName(u"show_edit_date_line")
        self.show_edit_date_line.setStyleSheet(u"QLineEdit {\n"
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
        self.show_edit_date_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.show_edit_date_line)

        self.show_edit_gener_line = QLineEdit(self.layoutWidget_2)
        self.show_edit_gener_line.setObjectName(u"show_edit_gener_line")
        self.show_edit_gener_line.setStyleSheet(u"QLineEdit {\n"
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
        self.show_edit_gener_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.show_edit_gener_line)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.show_edit_apply_button = QPushButton(self.layoutWidget_2)
        self.show_edit_apply_button.setObjectName(u"show_edit_apply_button")

        self.horizontalLayout_4.addWidget(self.show_edit_apply_button)

        self.show_edit_cancel_button = QPushButton(self.layoutWidget_2)
        self.show_edit_cancel_button.setObjectName(u"show_edit_cancel_button")

        self.horizontalLayout_4.addWidget(self.show_edit_cancel_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.edit_widget)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.retranslateUi(show)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(show)
    # setupUi

    def retranslateUi(self, show):
        show.setWindowTitle(QCoreApplication.translate("show", u"Form", None))
        self.show_image_lable.setText("")
        self.move_to_lable.setPlaceholderText(QCoreApplication.translate("show", u"Move to :-", None))
        self.show_name_lable.setText(QCoreApplication.translate("show", u"Name", None))
        self.show_time_lable.setText(QCoreApplication.translate("show", u"Time", None))
        self.show_label.setText(QCoreApplication.translate("show", u"Date", None))
        self.show_gener_lable.setText(QCoreApplication.translate("show", u"Gener", None))
        self.show_edit_button.setText(QCoreApplication.translate("show", u"Edit", None))
        self.show_delete_button.setText(QCoreApplication.translate("show", u"Delete", None))
        self.show_apply_button.setText(QCoreApplication.translate("show", u"Apply", None))
        self.show_cancel_button.setText(QCoreApplication.translate("show", u"Cancel", None))
        self.show_edit_image_label.setText("")
        self.show_edit_image_url.setPlaceholderText(QCoreApplication.translate("show", u"   New image URL", None))
        self.show_edit_time_line.setText("")
        self.show_edit_apply_button.setText(QCoreApplication.translate("show", u"Apply", None))
        self.show_edit_cancel_button.setText(QCoreApplication.translate("show", u"Cancel", None))
    # retranslateUi

