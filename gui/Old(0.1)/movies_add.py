# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Add_widget_1UGWDDM.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
import gui.resources_rc

class Ui_add_widget(object):
    def setupUi(self, add_widget):
        if not add_widget.objectName():
            add_widget.setObjectName(u"add_widget")
        add_widget.resize(741, 530)
        add_widget.setMinimumSize(QSize(741, 530))
        add_widget.setMaximumSize(QSize(741, 530))
        self.layoutWidget = QWidget(add_widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 741, 531))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.manual_button = QPushButton(self.layoutWidget)
        self.manual_button.setObjectName(u"manual_button")
        self.manual_button.setStyleSheet(u"QPushButton {\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-transform: uppercase;\n"
"    color: #ffffff;\n"
"    background-color: #0f1923;\n"
"    border: 1px solid #7D8082;\n"
"    border-radius: 4px;\n"
"    padding: 10px 20px;\n"
"    min-height: 40px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1a2430; /* slightly lighter on hover */\n"
"    border-color: #ffffff;      /* highlight border */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0a1017; /* darker when pressed */\n"
"    border-color: #ff4655;     /* red highlight */\n"
"}\n"
"\n"
"/* Optional: checked state if toggle button */\n"
"QPushButton:checked {\n"
"    background-color: #ff4655; /* red to indicate active */\n"
"    color: #ffffff;\n"
"    border-color: #ffffff;\n"
"}\n"
"")
        self.manual_button.setCheckable(True)
        self.manual_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.manual_button)

        self.api_button = QPushButton(self.layoutWidget)
        self.api_button.setObjectName(u"api_button")
        self.api_button.setStyleSheet(u"QPushButton {\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-transform: uppercase;\n"
"    color: #ffffff;\n"
"    background-color: #0f1923;\n"
"    border: 1px solid #7D8082;\n"
"    border-radius: 4px;\n"
"    padding: 10px 20px;\n"
"    min-height: 40px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1a2430; /* slightly lighter on hover */\n"
"    border-color: #ffffff;      /* highlight border */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0a1017; /* darker when pressed */\n"
"    border-color: #ff4655;     /* red highlight */\n"
"}\n"
"\n"
"/* Optional: checked state if toggle button */\n"
"QPushButton:checked {\n"
"    background-color: #ff4655; /* red to indicate active */\n"
"    color: #ffffff;\n"
"    border-color: #ffffff;\n"
"}\n"
"")
        self.api_button.setCheckable(True)
        self.api_button.setChecked(True)
        self.api_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.api_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.stackedWidget = QStackedWidget(self.layoutWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.manual_page = QWidget()
        self.manual_page.setObjectName(u"manual_page")
        self.layoutWidget1 = QWidget(self.manual_page)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 741, 411))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setSpacing(28)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, -1, 99, -1)
        self.manual_image_label = QLabel(self.layoutWidget1)
        self.manual_image_label.setObjectName(u"manual_image_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manual_image_label.sizePolicy().hasHeightForWidth())
        self.manual_image_label.setSizePolicy(sizePolicy)
        self.manual_image_label.setMinimumSize(QSize(180, 270))
        self.manual_image_label.setMaximumSize(QSize(180, 270))
        self.manual_image_label.setStyleSheet(u"QLabel {\n"
"    border: 1px solid white;   /* White border */\n"
"    border-radius: 6px;        /* Rounded corners (optional) */\n"
"    padding: 4px;              /* Space inside */\n"
"}\n"
"")
        self.manual_image_label.setScaledContents(True)
        self.manual_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.manual_image_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.image_url = QLineEdit(self.layoutWidget1)
        self.image_url.setObjectName(u"image_url")

        self.horizontalLayout_3.addWidget(self.image_url)

        self.line_2 = QFrame(self.layoutWidget1)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.manual_section_selector = QComboBox(self.layoutWidget1)
        self.manual_section_selector.addItem("")
        self.manual_section_selector.addItem("")
        self.manual_section_selector.addItem("")
        self.manual_section_selector.addItem("")
        self.manual_section_selector.addItem("")
        self.manual_section_selector.setObjectName(u"manual_section_selector")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.manual_section_selector.sizePolicy().hasHeightForWidth())
        self.manual_section_selector.setSizePolicy(sizePolicy1)
        self.manual_section_selector.setMaximumSize(QSize(100, 30))
        font = QFont()
        font.setPointSize(9)
        self.manual_section_selector.setFont(font)
        self.manual_section_selector.setAutoFillBackground(False)
        self.manual_section_selector.setEditable(False)
        self.manual_section_selector.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.manual_section_selector.setIconSize(QSize(16, 10))
        self.manual_section_selector.setFrame(False)
        self.manual_section_selector.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_3.addWidget(self.manual_section_selector)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.manual_name_input = QLineEdit(self.layoutWidget1)
        self.manual_name_input.setObjectName(u"manual_name_input")
        self.manual_name_input.setStyleSheet(u"QLineEdit {\n"
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
        self.manual_name_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.manual_name_input)

        self.manual_time_input = QLineEdit(self.layoutWidget1)
        self.manual_time_input.setObjectName(u"manual_time_input")
        self.manual_time_input.setStyleSheet(u"QLineEdit {\n"
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
        self.manual_time_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.manual_time_input)

        self.manual_date_input = QLineEdit(self.layoutWidget1)
        self.manual_date_input.setObjectName(u"manual_date_input")
        self.manual_date_input.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit {\n"
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
"    outline:"
                        " none;\n"
"    border-bottom: 2px solid #5891ff; /* \u0628\u0639\u062f \u0627\u0644\u062a\u0631\u0643\u064a\u0632 */\n"
"}\n"
"")
        self.manual_date_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.manual_date_input)

        self.manual_gener_input = QLineEdit(self.layoutWidget1)
        self.manual_gener_input.setObjectName(u"manual_gener_input")
        self.manual_gener_input.setStyleSheet(u"QLineEdit {\n"
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
        self.manual_gener_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.manual_gener_input)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.layoutWidget2 = QWidget(self.manual_page)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(550, 420, 158, 26))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.manual_apply_button = QPushButton(self.layoutWidget2)
        self.manual_apply_button.setObjectName(u"manual_apply_button")
        self.manual_apply_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.manual_apply_button)

        self.manual_cancel_button = QPushButton(self.layoutWidget2)
        self.manual_cancel_button.setObjectName(u"manual_cancel_button")

        self.horizontalLayout_5.addWidget(self.manual_cancel_button)

        self.stackedWidget.addWidget(self.manual_page)
        self.api_page = QWidget()
        self.api_page.setObjectName(u"api_page")
        self.layoutWidget_2 = QWidget(self.api_page)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 60, 741, 351))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_7.setSpacing(28)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, -1, 99, -1)
        self.api_image_label = QLabel(self.layoutWidget_2)
        self.api_image_label.setObjectName(u"api_image_label")
        sizePolicy.setHeightForWidth(self.api_image_label.sizePolicy().hasHeightForWidth())
        self.api_image_label.setSizePolicy(sizePolicy)
        self.api_image_label.setMinimumSize(QSize(180, 175))
        self.api_image_label.setMaximumSize(QSize(180, 270))
        self.api_image_label.setStyleSheet(u"QLabel {\n"
"    border: 1px solid white;   /* White border */\n"
"    border-radius: 6px;        /* Rounded corners (optional) */\n"
"    padding: 4px;              /* Space inside */\n"
"}\n"
"")
        self.api_image_label.setScaledContents(True)
        self.api_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.api_image_label)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(40)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.api_section_selector = QComboBox(self.layoutWidget_2)
        self.api_section_selector.addItem("")
        self.api_section_selector.addItem("")
        self.api_section_selector.addItem("")
        self.api_section_selector.addItem("")
        self.api_section_selector.addItem("")
        self.api_section_selector.setObjectName(u"api_section_selector")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.api_section_selector.sizePolicy().hasHeightForWidth())
        self.api_section_selector.setSizePolicy(sizePolicy2)
        self.api_section_selector.setMinimumSize(QSize(100, 20))
        self.api_section_selector.setMaximumSize(QSize(100, 20))
        self.api_section_selector.setFont(font)
        self.api_section_selector.setAutoFillBackground(False)
        self.api_section_selector.setEditable(False)
        self.api_section_selector.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.api_section_selector.setIconSize(QSize(16, 10))
        self.api_section_selector.setFrame(False)
        self.api_section_selector.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_8.addWidget(self.api_section_selector)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_7.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.api_name_input = QLineEdit(self.layoutWidget_2)
        self.api_name_input.setObjectName(u"api_name_input")
        self.api_name_input.setStyleSheet(u"QLineEdit {\n"
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
        self.api_name_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.api_name_input)

        self.api_time_input = QLineEdit(self.layoutWidget_2)
        self.api_time_input.setObjectName(u"api_time_input")
        self.api_time_input.setStyleSheet(u"QLineEdit {\n"
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
        self.api_time_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.api_time_input)

        self.api_date_input = QLineEdit(self.layoutWidget_2)
        self.api_date_input.setObjectName(u"api_date_input")
        self.api_date_input.setStyleSheet(u"QLineEdit {\n"
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
        self.api_date_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.api_date_input)

        self.api_gener_input = QLineEdit(self.layoutWidget_2)
        self.api_gener_input.setObjectName(u"api_gener_input")
        self.api_gener_input.setStyleSheet(u"QLineEdit {\n"
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
        self.api_gener_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.api_gener_input)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)

        self.layoutWidget_3 = QWidget(self.api_page)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(550, 420, 158, 26))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.api_apply_button = QPushButton(self.layoutWidget_3)
        self.api_apply_button.setObjectName(u"api_apply_button")
        self.api_apply_button.setFlat(False)

        self.horizontalLayout_10.addWidget(self.api_apply_button)

        self.api_cancel_button = QPushButton(self.layoutWidget_3)
        self.api_cancel_button.setObjectName(u"api_cancel_button")

        self.horizontalLayout_10.addWidget(self.api_cancel_button)

        self.layoutWidget3 = QWidget(self.api_page)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(210, 10, 331, 36))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.search_button = QPushButton(self.layoutWidget3)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setFlat(False)

        self.horizontalLayout_6.addWidget(self.search_button)

        self.search_line = QLineEdit(self.layoutWidget3)
        self.search_line.setObjectName(u"search_line")
        self.search_line.setStyleSheet(u"QLineEdit {\n"
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
        self.search_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.search_line)

        self.stackedWidget.addWidget(self.api_page)

        self.verticalLayout.addWidget(self.stackedWidget)

#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(add_widget)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(add_widget)
    # setupUi

    def retranslateUi(self, add_widget):
        add_widget.setWindowTitle(QCoreApplication.translate("add_widget", u"Form", None))
        self.manual_button.setText(QCoreApplication.translate("add_widget", u"API", None))
        self.api_button.setText(QCoreApplication.translate("add_widget", u"Manual", None))
        self.manual_image_label.setText("")
        self.image_url.setPlaceholderText(QCoreApplication.translate("add_widget", u"Past the image URL", None))
        self.manual_section_selector.setItemText(0, QCoreApplication.translate("add_widget", u"Dont want to watch", None))
        self.manual_section_selector.setItemText(1, QCoreApplication.translate("add_widget", u"New Item", None))
        self.manual_section_selector.setItemText(2, QCoreApplication.translate("add_widget", u"New Item", None))
        self.manual_section_selector.setItemText(3, QCoreApplication.translate("add_widget", u"New Item", None))
        self.manual_section_selector.setItemText(4, QCoreApplication.translate("add_widget", u"New Item", None))

        self.manual_section_selector.setCurrentText("")
        self.manual_section_selector.setPlaceholderText(QCoreApplication.translate("add_widget", u"Add to", None))
        self.manual_name_input.setText("")
        self.manual_name_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Name", None))
        self.manual_time_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Time", None))
        self.manual_date_input.setText("")
        self.manual_date_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Date", None))
        self.manual_gener_input.setText("")
        self.manual_gener_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Genre  (Action-Horror)", None))
        self.manual_apply_button.setText(QCoreApplication.translate("add_widget", u"Apply", None))
        self.manual_cancel_button.setText(QCoreApplication.translate("add_widget", u"Cancel", None))
        self.api_image_label.setText("")
        self.api_section_selector.setItemText(0, QCoreApplication.translate("add_widget", u"New Item", None))
        self.api_section_selector.setItemText(1, QCoreApplication.translate("add_widget", u"New Item", None))
        self.api_section_selector.setItemText(2, QCoreApplication.translate("add_widget", u"New Item", None))
        self.api_section_selector.setItemText(3, QCoreApplication.translate("add_widget", u"New Item", None))
        self.api_section_selector.setItemText(4, QCoreApplication.translate("add_widget", u"New Item", None))

        self.api_section_selector.setCurrentText("")
        self.api_section_selector.setPlaceholderText(QCoreApplication.translate("add_widget", u"Add to", None))
        self.api_name_input.setText("")
        self.api_name_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Name", None))
        self.api_time_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Time", None))
        self.api_date_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Date", None))
        self.api_gener_input.setText("")
        self.api_gener_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Genre  (Action-Horror)", None))
        self.api_apply_button.setText(QCoreApplication.translate("add_widget", u"Apply", None))
        self.api_cancel_button.setText(QCoreApplication.translate("add_widget", u"Cancel", None))
        self.search_button.setText(QCoreApplication.translate("add_widget", u"Search", None))
        self.search_line.setPlaceholderText(QCoreApplication.translate("add_widget", u"Search Online", None))
    # retranslateUi

