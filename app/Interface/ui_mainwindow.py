# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMaximumSize(QSize(200, 16777215))
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.title_aplication = QLabel(self.frame)
        self.title_aplication.setObjectName(u"title_aplication")

        self.verticalLayout_3.addWidget(self.title_aplication)


        self.verticalLayout_2.addWidget(self.frame)

        self.Menu = QFrame(self.left_container)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setFrameShape(QFrame.StyledPanel)
        self.Menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Menu)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Selections = QToolBox(self.Menu)
        self.Selections.setObjectName(u"Selections")
        self.buttons = QWidget()
        self.buttons.setObjectName(u"buttons")
        self.buttons.setGeometry(QRect(0, 0, 146, 460))
        self.verticalLayout_5 = QVBoxLayout(self.buttons)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_work_of_art = QPushButton(self.buttons)
        self.btn_work_of_art.setObjectName(u"btn_work_of_art")

        self.verticalLayout_5.addWidget(self.btn_work_of_art)

        self.btn_painting = QPushButton(self.buttons)
        self.btn_painting.setObjectName(u"btn_painting")

        self.verticalLayout_5.addWidget(self.btn_painting)

        self.btn_sculpture = QPushButton(self.buttons)
        self.btn_sculpture.setObjectName(u"btn_sculpture")

        self.verticalLayout_5.addWidget(self.btn_sculpture)

        self.btn_author = QPushButton(self.buttons)
        self.btn_author.setObjectName(u"btn_author")

        self.verticalLayout_5.addWidget(self.btn_author)

        self.btn_exhibition = QPushButton(self.buttons)
        self.btn_exhibition.setObjectName(u"btn_exhibition")

        self.verticalLayout_5.addWidget(self.btn_exhibition)

        self.btn_exihibition_work_of_art = QPushButton(self.buttons)
        self.btn_exihibition_work_of_art.setObjectName(u"btn_exihibition_work_of_art")

        self.verticalLayout_5.addWidget(self.btn_exihibition_work_of_art)

        self.btn_institution = QPushButton(self.buttons)
        self.btn_institution.setObjectName(u"btn_institution")

        self.verticalLayout_5.addWidget(self.btn_institution)

        self.btn_loan = QPushButton(self.buttons)
        self.btn_loan.setObjectName(u"btn_loan")

        self.verticalLayout_5.addWidget(self.btn_loan)

        self.btn_location = QPushButton(self.buttons)
        self.btn_location.setObjectName(u"btn_location")

        self.verticalLayout_5.addWidget(self.btn_location)

        self.btn_visitor = QPushButton(self.buttons)
        self.btn_visitor.setObjectName(u"btn_visitor")

        self.verticalLayout_5.addWidget(self.btn_visitor)

        self.btn_ticket = QPushButton(self.buttons)
        self.btn_ticket.setObjectName(u"btn_ticket")

        self.verticalLayout_5.addWidget(self.btn_ticket)

        self.btn_guide = QPushButton(self.buttons)
        self.btn_guide.setObjectName(u"btn_guide")

        self.verticalLayout_5.addWidget(self.btn_guide)

        self.btn_guided_visit = QPushButton(self.buttons)
        self.btn_guided_visit.setObjectName(u"btn_guided_visit")

        self.verticalLayout_5.addWidget(self.btn_guided_visit)

        self.btn_security = QPushButton(self.buttons)
        self.btn_security.setObjectName(u"btn_security")

        self.verticalLayout_5.addWidget(self.btn_security)

        self.Selections.addItem(self.buttons, u"Pages")
        self.buttuns_events = QWidget()
        self.buttuns_events.setObjectName(u"buttuns_events")
        self.buttuns_events.setGeometry(QRect(0, 0, 160, 434))
        self.verticalLayout_6 = QVBoxLayout(self.buttuns_events)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_create = QPushButton(self.buttuns_events)
        self.btn_create.setObjectName(u"btn_create")

        self.verticalLayout_6.addWidget(self.btn_create)

        self.btn_update = QPushButton(self.buttuns_events)
        self.btn_update.setObjectName(u"btn_update")

        self.verticalLayout_6.addWidget(self.btn_update)

        self.btn_delete = QPushButton(self.buttuns_events)
        self.btn_delete.setObjectName(u"btn_delete")

        self.verticalLayout_6.addWidget(self.btn_delete)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.Selections.addItem(self.buttuns_events, u"Events")

        self.verticalLayout_4.addWidget(self.Selections)


        self.verticalLayout_2.addWidget(self.Menu)


        self.horizontalLayout.addWidget(self.left_container)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(0, 50))
        self.top_frame.setMaximumSize(QSize(16777215, 100))
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.msg_error = QLabel(self.top_frame)
        self.msg_error.setObjectName(u"msg_error")

        self.horizontalLayout_2.addWidget(self.msg_error)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setEnabled(True)
        self.main_frame.setMinimumSize(QSize(0, 500))
        self.main_frame.setMaximumSize(QSize(16777215, 16777215))
        self.main_frame.setSizeIncrement(QSize(0, 500))
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.main_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pages_events = QStackedWidget(self.main_frame)
        self.pages_events.setObjectName(u"pages_events")
        self.create_itens = QWidget()
        self.create_itens.setObjectName(u"create_itens")
        self.verticalLayout_8 = QVBoxLayout(self.create_itens)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.formularies = QTabWidget(self.create_itens)
        self.formularies.setObjectName(u"formularies")
        self.create_work_of_art = QWidget()
        self.create_work_of_art.setObjectName(u"create_work_of_art")
        self.verticalLayout_10 = QVBoxLayout(self.create_work_of_art)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.line_work_of_art_id = QLineEdit(self.create_work_of_art)
        self.line_work_of_art_id.setObjectName(u"line_work_of_art_id")

        self.verticalLayout_10.addWidget(self.line_work_of_art_id)

        self.line_work_of_art_name = QLineEdit(self.create_work_of_art)
        self.line_work_of_art_name.setObjectName(u"line_work_of_art_name")

        self.verticalLayout_10.addWidget(self.line_work_of_art_name)

        self.line_work_of_art_description = QLineEdit(self.create_work_of_art)
        self.line_work_of_art_description.setObjectName(u"line_work_of_art_description")

        self.verticalLayout_10.addWidget(self.line_work_of_art_description)

        self.line_work_of_art_creation_date = QLineEdit(self.create_work_of_art)
        self.line_work_of_art_creation_date.setObjectName(u"line_work_of_art_creation_date")

        self.verticalLayout_10.addWidget(self.line_work_of_art_creation_date)

        self.line_work_of_art_author_id = QLineEdit(self.create_work_of_art)
        self.line_work_of_art_author_id.setObjectName(u"line_work_of_art_author_id")

        self.verticalLayout_10.addWidget(self.line_work_of_art_author_id)

        self.line_work_of_art_location_id = QLineEdit(self.create_work_of_art)
        self.line_work_of_art_location_id.setObjectName(u"line_work_of_art_location_id")

        self.verticalLayout_10.addWidget(self.line_work_of_art_location_id)

        self.line_work_of_art_type = QLineEdit(self.create_work_of_art)
        self.line_work_of_art_type.setObjectName(u"line_work_of_art_type")

        self.verticalLayout_10.addWidget(self.line_work_of_art_type)

        self.btn_apply_work_of_art = QPushButton(self.create_work_of_art)
        self.btn_apply_work_of_art.setObjectName(u"btn_apply_work_of_art")

        self.verticalLayout_10.addWidget(self.btn_apply_work_of_art)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)

        self.formularies.addTab(self.create_work_of_art, "")
        self.create_painting = QWidget()
        self.create_painting.setObjectName(u"create_painting")
        self.verticalLayout_21 = QVBoxLayout(self.create_painting)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.line_painting_id = QLineEdit(self.create_painting)
        self.line_painting_id.setObjectName(u"line_painting_id")

        self.verticalLayout_21.addWidget(self.line_painting_id)

        self.line_painting_work_of_art_id = QLineEdit(self.create_painting)
        self.line_painting_work_of_art_id.setObjectName(u"line_painting_work_of_art_id")

        self.verticalLayout_21.addWidget(self.line_painting_work_of_art_id)

        self.line_painting_technique = QLineEdit(self.create_painting)
        self.line_painting_technique.setObjectName(u"line_painting_technique")

        self.verticalLayout_21.addWidget(self.line_painting_technique)

        self.btn_apply_painting = QPushButton(self.create_painting)
        self.btn_apply_painting.setObjectName(u"btn_apply_painting")

        self.verticalLayout_21.addWidget(self.btn_apply_painting)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_11)

        self.formularies.addTab(self.create_painting, "")
        self.create_sculpture = QWidget()
        self.create_sculpture.setObjectName(u"create_sculpture")
        self.verticalLayout_22 = QVBoxLayout(self.create_sculpture)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.line_sculpture_id = QLineEdit(self.create_sculpture)
        self.line_sculpture_id.setObjectName(u"line_sculpture_id")

        self.verticalLayout_22.addWidget(self.line_sculpture_id)

        self.line_sculpture_work_of_art_id = QLineEdit(self.create_sculpture)
        self.line_sculpture_work_of_art_id.setObjectName(u"line_sculpture_work_of_art_id")

        self.verticalLayout_22.addWidget(self.line_sculpture_work_of_art_id)

        self.line_sculpture_material = QLineEdit(self.create_sculpture)
        self.line_sculpture_material.setObjectName(u"line_sculpture_material")

        self.verticalLayout_22.addWidget(self.line_sculpture_material)

        self.line_sculpture_weight = QLineEdit(self.create_sculpture)
        self.line_sculpture_weight.setObjectName(u"line_sculpture_weight")

        self.verticalLayout_22.addWidget(self.line_sculpture_weight)

        self.btn_apply_sculpture = QPushButton(self.create_sculpture)
        self.btn_apply_sculpture.setObjectName(u"btn_apply_sculpture")

        self.verticalLayout_22.addWidget(self.btn_apply_sculpture)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_12)

        self.formularies.addTab(self.create_sculpture, "")
        self.create_exhibition = QWidget()
        self.create_exhibition.setObjectName(u"create_exhibition")
        self.create_exhibition.setEnabled(True)
        self.verticalLayout_14 = QVBoxLayout(self.create_exhibition)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.line_exhibition_id = QLineEdit(self.create_exhibition)
        self.line_exhibition_id.setObjectName(u"line_exhibition_id")

        self.verticalLayout_14.addWidget(self.line_exhibition_id)

        self.line_exhibition_title = QLineEdit(self.create_exhibition)
        self.line_exhibition_title.setObjectName(u"line_exhibition_title")

        self.verticalLayout_14.addWidget(self.line_exhibition_title)

        self.line_exhibition_description = QLineEdit(self.create_exhibition)
        self.line_exhibition_description.setObjectName(u"line_exhibition_description")

        self.verticalLayout_14.addWidget(self.line_exhibition_description)

        self.line_exhibition_start_date = QLineEdit(self.create_exhibition)
        self.line_exhibition_start_date.setObjectName(u"line_exhibition_start_date")

        self.verticalLayout_14.addWidget(self.line_exhibition_start_date)

        self.line_exhibition_end_date = QLineEdit(self.create_exhibition)
        self.line_exhibition_end_date.setObjectName(u"line_exhibition_end_date")

        self.verticalLayout_14.addWidget(self.line_exhibition_end_date)

        self.btn_apply_exhibition = QPushButton(self.create_exhibition)
        self.btn_apply_exhibition.setObjectName(u"btn_apply_exhibition")

        self.verticalLayout_14.addWidget(self.btn_apply_exhibition)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_4)

        self.formularies.addTab(self.create_exhibition, "")
        self.create_author = QWidget()
        self.create_author.setObjectName(u"create_author")
        self.verticalLayout_11 = QVBoxLayout(self.create_author)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.line_author_id = QLineEdit(self.create_author)
        self.line_author_id.setObjectName(u"line_author_id")

        self.verticalLayout_11.addWidget(self.line_author_id)

        self.line_author_name = QLineEdit(self.create_author)
        self.line_author_name.setObjectName(u"line_author_name")

        self.verticalLayout_11.addWidget(self.line_author_name)

        self.btn_apply_author = QPushButton(self.create_author)
        self.btn_apply_author.setObjectName(u"btn_apply_author")

        self.verticalLayout_11.addWidget(self.btn_apply_author)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)

        self.formularies.addTab(self.create_author, "")
        self.create_exhibition_work_of_art = QWidget()
        self.create_exhibition_work_of_art.setObjectName(u"create_exhibition_work_of_art")
        self.verticalLayout_15 = QVBoxLayout(self.create_exhibition_work_of_art)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.line_exhibition_work_of_art_work_id = QLineEdit(self.create_exhibition_work_of_art)
        self.line_exhibition_work_of_art_work_id.setObjectName(u"line_exhibition_work_of_art_work_id")

        self.verticalLayout_15.addWidget(self.line_exhibition_work_of_art_work_id)

        self.line_exhibition_work_of_art_exhibition_id = QLineEdit(self.create_exhibition_work_of_art)
        self.line_exhibition_work_of_art_exhibition_id.setObjectName(u"line_exhibition_work_of_art_exhibition_id")

        self.verticalLayout_15.addWidget(self.line_exhibition_work_of_art_exhibition_id)

        self.btn_apply_exhibition_work_of_art = QPushButton(self.create_exhibition_work_of_art)
        self.btn_apply_exhibition_work_of_art.setObjectName(u"btn_apply_exhibition_work_of_art")

        self.verticalLayout_15.addWidget(self.btn_apply_exhibition_work_of_art)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_5)

        self.formularies.addTab(self.create_exhibition_work_of_art, "")
        self.create_guide = QWidget()
        self.create_guide.setObjectName(u"create_guide")
        self.verticalLayout_16 = QVBoxLayout(self.create_guide)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.line_guide_id = QLineEdit(self.create_guide)
        self.line_guide_id.setObjectName(u"line_guide_id")

        self.verticalLayout_16.addWidget(self.line_guide_id)

        self.line_guide_name = QLineEdit(self.create_guide)
        self.line_guide_name.setObjectName(u"line_guide_name")

        self.verticalLayout_16.addWidget(self.line_guide_name)

        self.line_guide_email = QLineEdit(self.create_guide)
        self.line_guide_email.setObjectName(u"line_guide_email")

        self.verticalLayout_16.addWidget(self.line_guide_email)

        self.line_guide_phone = QLineEdit(self.create_guide)
        self.line_guide_phone.setObjectName(u"line_guide_phone")

        self.verticalLayout_16.addWidget(self.line_guide_phone)

        self.btn_apply_guide = QPushButton(self.create_guide)
        self.btn_apply_guide.setObjectName(u"btn_apply_guide")

        self.verticalLayout_16.addWidget(self.btn_apply_guide)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_6)

        self.formularies.addTab(self.create_guide, "")
        self.create_guided_visits = QWidget()
        self.create_guided_visits.setObjectName(u"create_guided_visits")
        self.verticalLayout_17 = QVBoxLayout(self.create_guided_visits)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.line_guided_visits_id = QLineEdit(self.create_guided_visits)
        self.line_guided_visits_id.setObjectName(u"line_guided_visits_id")

        self.verticalLayout_17.addWidget(self.line_guided_visits_id)

        self.line_guided_visits_group = QLineEdit(self.create_guided_visits)
        self.line_guided_visits_group.setObjectName(u"line_guided_visits_group")

        self.verticalLayout_17.addWidget(self.line_guided_visits_group)

        self.line_guided_visits_visit_date = QLineEdit(self.create_guided_visits)
        self.line_guided_visits_visit_date.setObjectName(u"line_guided_visits_visit_date")

        self.verticalLayout_17.addWidget(self.line_guided_visits_visit_date)

        self.line_guided_visits_hours = QLineEdit(self.create_guided_visits)
        self.line_guided_visits_hours.setObjectName(u"line_guided_visits_hours")

        self.verticalLayout_17.addWidget(self.line_guided_visits_hours)

        self.line_guided_visits_guide_id = QLineEdit(self.create_guided_visits)
        self.line_guided_visits_guide_id.setObjectName(u"line_guided_visits_guide_id")

        self.verticalLayout_17.addWidget(self.line_guided_visits_guide_id)

        self.btn_apply_guided_visits = QPushButton(self.create_guided_visits)
        self.btn_apply_guided_visits.setObjectName(u"btn_apply_guided_visits")

        self.verticalLayout_17.addWidget(self.btn_apply_guided_visits)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_7)

        self.formularies.addTab(self.create_guided_visits, "")
        self.create_institution = QWidget()
        self.create_institution.setObjectName(u"create_institution")
        self.verticalLayout_18 = QVBoxLayout(self.create_institution)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.line_institution_id = QLineEdit(self.create_institution)
        self.line_institution_id.setObjectName(u"line_institution_id")

        self.verticalLayout_18.addWidget(self.line_institution_id)

        self.line_institution_name = QLineEdit(self.create_institution)
        self.line_institution_name.setObjectName(u"line_institution_name")

        self.verticalLayout_18.addWidget(self.line_institution_name)

        self.btn_apply_institution = QPushButton(self.create_institution)
        self.btn_apply_institution.setObjectName(u"btn_apply_institution")

        self.verticalLayout_18.addWidget(self.btn_apply_institution)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_8)

        self.formularies.addTab(self.create_institution, "")
        self.create_loan = QWidget()
        self.create_loan.setObjectName(u"create_loan")
        self.verticalLayout_19 = QVBoxLayout(self.create_loan)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.line_loan_id = QLineEdit(self.create_loan)
        self.line_loan_id.setObjectName(u"line_loan_id")

        self.verticalLayout_19.addWidget(self.line_loan_id)

        self.line_loan_work_of_art_id = QLineEdit(self.create_loan)
        self.line_loan_work_of_art_id.setObjectName(u"line_loan_work_of_art_id")

        self.verticalLayout_19.addWidget(self.line_loan_work_of_art_id)

        self.line_loan_institution_id = QLineEdit(self.create_loan)
        self.line_loan_institution_id.setObjectName(u"line_loan_institution_id")

        self.verticalLayout_19.addWidget(self.line_loan_institution_id)

        self.line_loan_date = QLineEdit(self.create_loan)
        self.line_loan_date.setObjectName(u"line_loan_date")

        self.verticalLayout_19.addWidget(self.line_loan_date)

        self.line_loan_return_date = QLineEdit(self.create_loan)
        self.line_loan_return_date.setObjectName(u"line_loan_return_date")

        self.verticalLayout_19.addWidget(self.line_loan_return_date)

        self.btn_apply_loan = QPushButton(self.create_loan)
        self.btn_apply_loan.setObjectName(u"btn_apply_loan")

        self.verticalLayout_19.addWidget(self.btn_apply_loan)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_9)

        self.formularies.addTab(self.create_loan, "")
        self.create_location = QWidget()
        self.create_location.setObjectName(u"create_location")
        self.verticalLayout_20 = QVBoxLayout(self.create_location)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.line_location_id = QLineEdit(self.create_location)
        self.line_location_id.setObjectName(u"line_location_id")

        self.verticalLayout_20.addWidget(self.line_location_id)

        self.line_location_name = QLineEdit(self.create_location)
        self.line_location_name.setObjectName(u"line_location_name")

        self.verticalLayout_20.addWidget(self.line_location_name)

        self.btn_apply_location = QPushButton(self.create_location)
        self.btn_apply_location.setObjectName(u"btn_apply_location")

        self.verticalLayout_20.addWidget(self.btn_apply_location)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_10)

        self.formularies.addTab(self.create_location, "")
        self.create_security = QWidget()
        self.create_security.setObjectName(u"create_security")
        self.verticalLayout_23 = QVBoxLayout(self.create_security)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.line_security_id = QLineEdit(self.create_security)
        self.line_security_id.setObjectName(u"line_security_id")

        self.verticalLayout_23.addWidget(self.line_security_id)

        self.line_security_name = QLineEdit(self.create_security)
        self.line_security_name.setObjectName(u"line_security_name")

        self.verticalLayout_23.addWidget(self.line_security_name)

        self.line_security_email = QLineEdit(self.create_security)
        self.line_security_email.setObjectName(u"line_security_email")

        self.verticalLayout_23.addWidget(self.line_security_email)

        self.line_security_phone = QLineEdit(self.create_security)
        self.line_security_phone.setObjectName(u"line_security_phone")

        self.verticalLayout_23.addWidget(self.line_security_phone)

        self.line_security_location_id = QLineEdit(self.create_security)
        self.line_security_location_id.setObjectName(u"line_security_location_id")

        self.verticalLayout_23.addWidget(self.line_security_location_id)

        self.btn_apply_security = QPushButton(self.create_security)
        self.btn_apply_security.setObjectName(u"btn_apply_security")

        self.verticalLayout_23.addWidget(self.btn_apply_security)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_13)

        self.formularies.addTab(self.create_security, "")
        self.create_ticket = QWidget()
        self.create_ticket.setObjectName(u"create_ticket")
        self.verticalLayout_24 = QVBoxLayout(self.create_ticket)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.line_ticket_id = QLineEdit(self.create_ticket)
        self.line_ticket_id.setObjectName(u"line_ticket_id")

        self.verticalLayout_24.addWidget(self.line_ticket_id)

        self.line_ticket_visitor_id = QLineEdit(self.create_ticket)
        self.line_ticket_visitor_id.setObjectName(u"line_ticket_visitor_id")

        self.verticalLayout_24.addWidget(self.line_ticket_visitor_id)

        self.line_ticket_type = QLineEdit(self.create_ticket)
        self.line_ticket_type.setObjectName(u"line_ticket_type")

        self.verticalLayout_24.addWidget(self.line_ticket_type)

        self.line_ticket_visit_date = QLineEdit(self.create_ticket)
        self.line_ticket_visit_date.setObjectName(u"line_ticket_visit_date")
        self.line_ticket_visit_date.setReadOnly(False)

        self.verticalLayout_24.addWidget(self.line_ticket_visit_date)

        self.line_ticket_purchase_date = QLineEdit(self.create_ticket)
        self.line_ticket_purchase_date.setObjectName(u"line_ticket_purchase_date")

        self.verticalLayout_24.addWidget(self.line_ticket_purchase_date)

        self.line_ticket_guide_id = QLineEdit(self.create_ticket)
        self.line_ticket_guide_id.setObjectName(u"line_ticket_guide_id")

        self.verticalLayout_24.addWidget(self.line_ticket_guide_id)

        self.btn_apply_ticket = QPushButton(self.create_ticket)
        self.btn_apply_ticket.setObjectName(u"btn_apply_ticket")

        self.verticalLayout_24.addWidget(self.btn_apply_ticket)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_14)

        self.formularies.addTab(self.create_ticket, "")
        self.create_visitor = QWidget()
        self.create_visitor.setObjectName(u"create_visitor")
        self.verticalLayout_25 = QVBoxLayout(self.create_visitor)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.line_visitor_id = QLineEdit(self.create_visitor)
        self.line_visitor_id.setObjectName(u"line_visitor_id")

        self.verticalLayout_25.addWidget(self.line_visitor_id)

        self.line_visitor_name = QLineEdit(self.create_visitor)
        self.line_visitor_name.setObjectName(u"line_visitor_name")

        self.verticalLayout_25.addWidget(self.line_visitor_name)

        self.line_visitor_email = QLineEdit(self.create_visitor)
        self.line_visitor_email.setObjectName(u"line_visitor_email")

        self.verticalLayout_25.addWidget(self.line_visitor_email)

        self.line_visitor_phone = QLineEdit(self.create_visitor)
        self.line_visitor_phone.setObjectName(u"line_visitor_phone")

        self.verticalLayout_25.addWidget(self.line_visitor_phone)

        self.btn_apply_visitor = QPushButton(self.create_visitor)
        self.btn_apply_visitor.setObjectName(u"btn_apply_visitor")

        self.verticalLayout_25.addWidget(self.btn_apply_visitor)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_15)

        self.formularies.addTab(self.create_visitor, "")

        self.verticalLayout_8.addWidget(self.formularies)

        self.pages_events.addWidget(self.create_itens)
        self.page_author = QWidget()
        self.page_author.setObjectName(u"page_author")
        self.verticalLayout_13 = QVBoxLayout(self.page_author)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.search_author = QFrame(self.page_author)
        self.search_author.setObjectName(u"search_author")
        self.search_author.setMinimumSize(QSize(0, 100))
        self.search_author.setFrameShape(QFrame.StyledPanel)
        self.search_author.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.search_author)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.search_author_name = QLineEdit(self.search_author)
        self.search_author_name.setObjectName(u"search_author_name")

        self.verticalLayout_39.addWidget(self.search_author_name)

        self.search_author_id = QLineEdit(self.search_author)
        self.search_author_id.setObjectName(u"search_author_id")

        self.verticalLayout_39.addWidget(self.search_author_id)

        self.btn_search_author = QPushButton(self.search_author)
        self.btn_search_author.setObjectName(u"btn_search_author")

        self.verticalLayout_39.addWidget(self.btn_search_author)


        self.verticalLayout_13.addWidget(self.search_author)

        self.table_author = QTableWidget(self.page_author)
        self.table_author.setObjectName(u"table_author")

        self.verticalLayout_13.addWidget(self.table_author)

        self.pages_events.addWidget(self.page_author)
        self.page_work_of_art = QWidget()
        self.page_work_of_art.setObjectName(u"page_work_of_art")
        self.verticalLayout_9 = QVBoxLayout(self.page_work_of_art)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.search_work_of_art = QFrame(self.page_work_of_art)
        self.search_work_of_art.setObjectName(u"search_work_of_art")
        self.search_work_of_art.setMinimumSize(QSize(0, 100))
        self.search_work_of_art.setFrameShape(QFrame.StyledPanel)
        self.search_work_of_art.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.search_work_of_art)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.search_work_of_art_name = QLineEdit(self.search_work_of_art)
        self.search_work_of_art_name.setObjectName(u"search_work_of_art_name")

        self.gridLayout_6.addWidget(self.search_work_of_art_name, 0, 0, 1, 1)

        self.search_work_of_art_author_name = QLineEdit(self.search_work_of_art)
        self.search_work_of_art_author_name.setObjectName(u"search_work_of_art_author_name")

        self.gridLayout_6.addWidget(self.search_work_of_art_author_name, 0, 1, 1, 2)

        self.search_work_of_art_location_name = QLineEdit(self.search_work_of_art)
        self.search_work_of_art_location_name.setObjectName(u"search_work_of_art_location_name")

        self.gridLayout_6.addWidget(self.search_work_of_art_location_name, 0, 3, 1, 1)

        self.search_work_of_art_creation_date = QLineEdit(self.search_work_of_art)
        self.search_work_of_art_creation_date.setObjectName(u"search_work_of_art_creation_date")

        self.gridLayout_6.addWidget(self.search_work_of_art_creation_date, 1, 0, 1, 2)

        self.search_work_of_art_type = QLineEdit(self.search_work_of_art)
        self.search_work_of_art_type.setObjectName(u"search_work_of_art_type")

        self.gridLayout_6.addWidget(self.search_work_of_art_type, 1, 2, 1, 2)

        self.btn_search_work_of_art = QPushButton(self.search_work_of_art)
        self.btn_search_work_of_art.setObjectName(u"btn_search_work_of_art")

        self.gridLayout_6.addWidget(self.btn_search_work_of_art, 2, 0, 1, 4)


        self.verticalLayout_9.addWidget(self.search_work_of_art)

        self.table_work_of_art = QTableWidget(self.page_work_of_art)
        self.table_work_of_art.setObjectName(u"table_work_of_art")

        self.verticalLayout_9.addWidget(self.table_work_of_art)

        self.pages_events.addWidget(self.page_work_of_art)
        self.page_painting = QWidget()
        self.page_painting.setObjectName(u"page_painting")
        self.verticalLayout_12 = QVBoxLayout(self.page_painting)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.search_painting = QFrame(self.page_painting)
        self.search_painting.setObjectName(u"search_painting")
        self.search_painting.setMinimumSize(QSize(0, 100))
        self.search_painting.setFrameShape(QFrame.StyledPanel)
        self.search_painting.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.search_painting)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.search_painting_work_of_art_name = QLineEdit(self.search_painting)
        self.search_painting_work_of_art_name.setObjectName(u"search_painting_work_of_art_name")

        self.gridLayout_3.addWidget(self.search_painting_work_of_art_name, 0, 0, 1, 1)

        self.search_painting_technique = QLineEdit(self.search_painting)
        self.search_painting_technique.setObjectName(u"search_painting_technique")

        self.gridLayout_3.addWidget(self.search_painting_technique, 0, 1, 1, 1)

        self.btn_search_painting = QPushButton(self.search_painting)
        self.btn_search_painting.setObjectName(u"btn_search_painting")

        self.gridLayout_3.addWidget(self.btn_search_painting, 1, 0, 1, 2)


        self.verticalLayout_12.addWidget(self.search_painting)

        self.table_painting = QTableWidget(self.page_painting)
        self.table_painting.setObjectName(u"table_painting")

        self.verticalLayout_12.addWidget(self.table_painting)

        self.pages_events.addWidget(self.page_painting)
        self.page_sculpture = QWidget()
        self.page_sculpture.setObjectName(u"page_sculpture")
        self.verticalLayout_7 = QVBoxLayout(self.page_sculpture)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.search_sculpture = QFrame(self.page_sculpture)
        self.search_sculpture.setObjectName(u"search_sculpture")
        self.search_sculpture.setMinimumSize(QSize(0, 100))
        self.search_sculpture.setFrameShape(QFrame.StyledPanel)
        self.search_sculpture.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.search_sculpture)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.search_sculpture_work_of_art_name = QLineEdit(self.search_sculpture)
        self.search_sculpture_work_of_art_name.setObjectName(u"search_sculpture_work_of_art_name")

        self.verticalLayout_42.addWidget(self.search_sculpture_work_of_art_name)

        self.search_sculpture_material = QLineEdit(self.search_sculpture)
        self.search_sculpture_material.setObjectName(u"search_sculpture_material")

        self.verticalLayout_42.addWidget(self.search_sculpture_material)

        self.search_sculpture_weight = QLineEdit(self.search_sculpture)
        self.search_sculpture_weight.setObjectName(u"search_sculpture_weight")

        self.verticalLayout_42.addWidget(self.search_sculpture_weight)

        self.btn_search_sculpture = QPushButton(self.search_sculpture)
        self.btn_search_sculpture.setObjectName(u"btn_search_sculpture")

        self.verticalLayout_42.addWidget(self.btn_search_sculpture)


        self.verticalLayout_7.addWidget(self.search_sculpture)

        self.table_sculpture = QTableWidget(self.page_sculpture)
        self.table_sculpture.setObjectName(u"table_sculpture")

        self.verticalLayout_7.addWidget(self.table_sculpture)

        self.pages_events.addWidget(self.page_sculpture)
        self.page_exhibition = QWidget()
        self.page_exhibition.setObjectName(u"page_exhibition")
        self.verticalLayout_26 = QVBoxLayout(self.page_exhibition)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.search_exhibition = QFrame(self.page_exhibition)
        self.search_exhibition.setObjectName(u"search_exhibition")
        self.search_exhibition.setMinimumSize(QSize(0, 100))
        self.search_exhibition.setFrameShape(QFrame.StyledPanel)
        self.search_exhibition.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.search_exhibition)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.search_exhibition_start_date = QLineEdit(self.search_exhibition)
        self.search_exhibition_start_date.setObjectName(u"search_exhibition_start_date")

        self.verticalLayout_37.addWidget(self.search_exhibition_start_date)

        self.search_exhibition_name = QLineEdit(self.search_exhibition)
        self.search_exhibition_name.setObjectName(u"search_exhibition_name")

        self.verticalLayout_37.addWidget(self.search_exhibition_name)

        self.search_exhibition_end_date = QLineEdit(self.search_exhibition)
        self.search_exhibition_end_date.setObjectName(u"search_exhibition_end_date")

        self.verticalLayout_37.addWidget(self.search_exhibition_end_date)

        self.btn_search_exhibition = QPushButton(self.search_exhibition)
        self.btn_search_exhibition.setObjectName(u"btn_search_exhibition")

        self.verticalLayout_37.addWidget(self.btn_search_exhibition)


        self.verticalLayout_26.addWidget(self.search_exhibition)

        self.table_exhibition = QTableWidget(self.page_exhibition)
        self.table_exhibition.setObjectName(u"table_exhibition")

        self.verticalLayout_26.addWidget(self.table_exhibition)

        self.pages_events.addWidget(self.page_exhibition)
        self.page_ew = QWidget()
        self.page_ew.setObjectName(u"page_ew")
        self.verticalLayout_27 = QVBoxLayout(self.page_ew)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.search_ew = QFrame(self.page_ew)
        self.search_ew.setObjectName(u"search_ew")
        self.search_ew.setMinimumSize(QSize(100, 100))
        self.search_ew.setFrameShape(QFrame.StyledPanel)
        self.search_ew.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.search_ew)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.search_ew_work_of_art_name = QLineEdit(self.search_ew)
        self.search_ew_work_of_art_name.setObjectName(u"search_ew_work_of_art_name")

        self.verticalLayout_36.addWidget(self.search_ew_work_of_art_name)

        self.search_ew_exhibition_name = QLineEdit(self.search_ew)
        self.search_ew_exhibition_name.setObjectName(u"search_ew_exhibition_name")

        self.verticalLayout_36.addWidget(self.search_ew_exhibition_name)

        self.btn_serach_ew = QPushButton(self.search_ew)
        self.btn_serach_ew.setObjectName(u"btn_serach_ew")

        self.verticalLayout_36.addWidget(self.btn_serach_ew)


        self.verticalLayout_27.addWidget(self.search_ew)

        self.table_ew = QTableWidget(self.page_ew)
        self.table_ew.setObjectName(u"table_ew")

        self.verticalLayout_27.addWidget(self.table_ew)

        self.pages_events.addWidget(self.page_ew)
        self.page_institution = QWidget()
        self.page_institution.setObjectName(u"page_institution")
        self.verticalLayout_30 = QVBoxLayout(self.page_institution)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.search_institution = QFrame(self.page_institution)
        self.search_institution.setObjectName(u"search_institution")
        self.search_institution.setMinimumSize(QSize(0, 100))
        self.search_institution.setFrameShape(QFrame.StyledPanel)
        self.search_institution.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.search_institution)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.search_institution_name = QLineEdit(self.search_institution)
        self.search_institution_name.setObjectName(u"search_institution_name")

        self.verticalLayout_40.addWidget(self.search_institution_name)

        self.search_institution_loan_date = QLineEdit(self.search_institution)
        self.search_institution_loan_date.setObjectName(u"search_institution_loan_date")

        self.verticalLayout_40.addWidget(self.search_institution_loan_date)

        self.search_institution_return_loan_date = QLineEdit(self.search_institution)
        self.search_institution_return_loan_date.setObjectName(u"search_institution_return_loan_date")

        self.verticalLayout_40.addWidget(self.search_institution_return_loan_date)

        self.btn_search_institution = QPushButton(self.search_institution)
        self.btn_search_institution.setObjectName(u"btn_search_institution")

        self.verticalLayout_40.addWidget(self.btn_search_institution)


        self.verticalLayout_30.addWidget(self.search_institution)

        self.table_institution = QTableWidget(self.page_institution)
        self.table_institution.setObjectName(u"table_institution")

        self.verticalLayout_30.addWidget(self.table_institution)

        self.pages_events.addWidget(self.page_institution)
        self.page_loan = QWidget()
        self.page_loan.setObjectName(u"page_loan")
        self.verticalLayout_31 = QVBoxLayout(self.page_loan)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.search_loan = QFrame(self.page_loan)
        self.search_loan.setObjectName(u"search_loan")
        self.search_loan.setMinimumSize(QSize(0, 100))
        self.search_loan.setFrameShape(QFrame.StyledPanel)
        self.search_loan.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.search_loan)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.search_loan_work_of_art_name = QLineEdit(self.search_loan)
        self.search_loan_work_of_art_name.setObjectName(u"search_loan_work_of_art_name")

        self.gridLayout_2.addWidget(self.search_loan_work_of_art_name, 0, 0, 1, 1)

        self.search_loan_institution_name = QLineEdit(self.search_loan)
        self.search_loan_institution_name.setObjectName(u"search_loan_institution_name")

        self.gridLayout_2.addWidget(self.search_loan_institution_name, 0, 1, 1, 1)

        self.search_loan_date = QLineEdit(self.search_loan)
        self.search_loan_date.setObjectName(u"search_loan_date")

        self.gridLayout_2.addWidget(self.search_loan_date, 1, 0, 1, 1)

        self.search_loan_return_date = QLineEdit(self.search_loan)
        self.search_loan_return_date.setObjectName(u"search_loan_return_date")

        self.gridLayout_2.addWidget(self.search_loan_return_date, 1, 1, 1, 1)

        self.btn_search_loan = QPushButton(self.search_loan)
        self.btn_search_loan.setObjectName(u"btn_search_loan")

        self.gridLayout_2.addWidget(self.btn_search_loan, 2, 0, 1, 2)


        self.verticalLayout_31.addWidget(self.search_loan)

        self.table_loan = QTableWidget(self.page_loan)
        self.table_loan.setObjectName(u"table_loan")

        self.verticalLayout_31.addWidget(self.table_loan)

        self.pages_events.addWidget(self.page_loan)
        self.page_location = QWidget()
        self.page_location.setObjectName(u"page_location")
        self.verticalLayout_32 = QVBoxLayout(self.page_location)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.search_location = QFrame(self.page_location)
        self.search_location.setObjectName(u"search_location")
        self.search_location.setMinimumSize(QSize(0, 100))
        self.search_location.setFrameShape(QFrame.StyledPanel)
        self.search_location.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.search_location)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.search_location_name = QLineEdit(self.search_location)
        self.search_location_name.setObjectName(u"search_location_name")

        self.verticalLayout_41.addWidget(self.search_location_name)

        self.btn_search_location = QPushButton(self.search_location)
        self.btn_search_location.setObjectName(u"btn_search_location")

        self.verticalLayout_41.addWidget(self.btn_search_location)


        self.verticalLayout_32.addWidget(self.search_location)

        self.table_location = QTableWidget(self.page_location)
        self.table_location.setObjectName(u"table_location")

        self.verticalLayout_32.addWidget(self.table_location)

        self.pages_events.addWidget(self.page_location)
        self.page_visitor = QWidget()
        self.page_visitor.setObjectName(u"page_visitor")
        self.verticalLayout_35 = QVBoxLayout(self.page_visitor)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.search_visitor = QFrame(self.page_visitor)
        self.search_visitor.setObjectName(u"search_visitor")
        self.search_visitor.setMinimumSize(QSize(0, 100))
        self.search_visitor.setFrameShape(QFrame.StyledPanel)
        self.search_visitor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.search_visitor)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.search_visitor_name = QLineEdit(self.search_visitor)
        self.search_visitor_name.setObjectName(u"search_visitor_name")

        self.verticalLayout_43.addWidget(self.search_visitor_name)

        self.search_visitor_email = QLineEdit(self.search_visitor)
        self.search_visitor_email.setObjectName(u"search_visitor_email")

        self.verticalLayout_43.addWidget(self.search_visitor_email)

        self.search_visitor_phone = QLineEdit(self.search_visitor)
        self.search_visitor_phone.setObjectName(u"search_visitor_phone")

        self.verticalLayout_43.addWidget(self.search_visitor_phone)

        self.btn_search_visitor = QPushButton(self.search_visitor)
        self.btn_search_visitor.setObjectName(u"btn_search_visitor")

        self.verticalLayout_43.addWidget(self.btn_search_visitor)


        self.verticalLayout_35.addWidget(self.search_visitor)

        self.table_visitor = QTableWidget(self.page_visitor)
        self.table_visitor.setObjectName(u"table_visitor")

        self.verticalLayout_35.addWidget(self.table_visitor)

        self.pages_events.addWidget(self.page_visitor)
        self.page_ticket = QWidget()
        self.page_ticket.setObjectName(u"page_ticket")
        self.verticalLayout_34 = QVBoxLayout(self.page_ticket)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.search_ticket = QFrame(self.page_ticket)
        self.search_ticket.setObjectName(u"search_ticket")
        self.search_ticket.setMinimumSize(QSize(0, 100))
        self.search_ticket.setFrameShape(QFrame.StyledPanel)
        self.search_ticket.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.search_ticket)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.search_ticket_visitor_name = QLineEdit(self.search_ticket)
        self.search_ticket_visitor_name.setObjectName(u"search_ticket_visitor_name")

        self.gridLayout_5.addWidget(self.search_ticket_visitor_name, 0, 0, 1, 1)

        self.search_ticket_type = QLineEdit(self.search_ticket)
        self.search_ticket_type.setObjectName(u"search_ticket_type")

        self.gridLayout_5.addWidget(self.search_ticket_type, 0, 1, 1, 1)

        self.btn_search_ticket = QPushButton(self.search_ticket)
        self.btn_search_ticket.setObjectName(u"btn_search_ticket")

        self.gridLayout_5.addWidget(self.btn_search_ticket, 1, 0, 1, 2)


        self.verticalLayout_34.addWidget(self.search_ticket)

        self.table_ticket = QTableWidget(self.page_ticket)
        self.table_ticket.setObjectName(u"table_ticket")

        self.verticalLayout_34.addWidget(self.table_ticket)

        self.pages_events.addWidget(self.page_ticket)
        self.page_guide = QWidget()
        self.page_guide.setObjectName(u"page_guide")
        self.verticalLayout_28 = QVBoxLayout(self.page_guide)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.search_guide = QFrame(self.page_guide)
        self.search_guide.setObjectName(u"search_guide")
        self.search_guide.setMinimumSize(QSize(0, 100))
        self.search_guide.setFrameShape(QFrame.StyledPanel)
        self.search_guide.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.search_guide)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.search_guide_name = QLineEdit(self.search_guide)
        self.search_guide_name.setObjectName(u"search_guide_name")

        self.verticalLayout_38.addWidget(self.search_guide_name)

        self.search_guide_email = QLineEdit(self.search_guide)
        self.search_guide_email.setObjectName(u"search_guide_email")

        self.verticalLayout_38.addWidget(self.search_guide_email)

        self.search_guide_phone = QLineEdit(self.search_guide)
        self.search_guide_phone.setObjectName(u"search_guide_phone")

        self.verticalLayout_38.addWidget(self.search_guide_phone)

        self.btn_search_guide = QPushButton(self.search_guide)
        self.btn_search_guide.setObjectName(u"btn_search_guide")

        self.verticalLayout_38.addWidget(self.btn_search_guide)


        self.verticalLayout_28.addWidget(self.search_guide)

        self.table_guide = QTableWidget(self.page_guide)
        self.table_guide.setObjectName(u"table_guide")

        self.verticalLayout_28.addWidget(self.table_guide)

        self.pages_events.addWidget(self.page_guide)
        self.page_gv = QWidget()
        self.page_gv.setObjectName(u"page_gv")
        self.verticalLayout_29 = QVBoxLayout(self.page_gv)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.search_gv = QFrame(self.page_gv)
        self.search_gv.setObjectName(u"search_gv")
        self.search_gv.setMinimumSize(QSize(0, 100))
        self.search_gv.setFrameShape(QFrame.StyledPanel)
        self.search_gv.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.search_gv)
        self.gridLayout.setObjectName(u"gridLayout")
        self.search_gv_group = QLineEdit(self.search_gv)
        self.search_gv_group.setObjectName(u"search_gv_group")

        self.gridLayout.addWidget(self.search_gv_group, 0, 0, 1, 1)

        self.search_gv_visit_date = QLineEdit(self.search_gv)
        self.search_gv_visit_date.setObjectName(u"search_gv_visit_date")

        self.gridLayout.addWidget(self.search_gv_visit_date, 0, 1, 1, 1)

        self.search_gv_hours = QLineEdit(self.search_gv)
        self.search_gv_hours.setObjectName(u"search_gv_hours")

        self.gridLayout.addWidget(self.search_gv_hours, 1, 0, 1, 1)

        self.search_gv_guide_name = QLineEdit(self.search_gv)
        self.search_gv_guide_name.setObjectName(u"search_gv_guide_name")

        self.gridLayout.addWidget(self.search_gv_guide_name, 1, 1, 1, 1)

        self.btn_search_gv = QPushButton(self.search_gv)
        self.btn_search_gv.setObjectName(u"btn_search_gv")

        self.gridLayout.addWidget(self.btn_search_gv, 2, 0, 1, 2)


        self.verticalLayout_29.addWidget(self.search_gv)

        self.table_gv = QTableWidget(self.page_gv)
        self.table_gv.setObjectName(u"table_gv")

        self.verticalLayout_29.addWidget(self.table_gv)

        self.pages_events.addWidget(self.page_gv)
        self.page_security = QWidget()
        self.page_security.setObjectName(u"page_security")
        self.verticalLayout_33 = QVBoxLayout(self.page_security)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.search_security = QFrame(self.page_security)
        self.search_security.setObjectName(u"search_security")
        self.search_security.setMinimumSize(QSize(0, 100))
        self.search_security.setFrameShape(QFrame.StyledPanel)
        self.search_security.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.search_security)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.search_security_name = QLineEdit(self.search_security)
        self.search_security_name.setObjectName(u"search_security_name")

        self.gridLayout_4.addWidget(self.search_security_name, 0, 0, 1, 1)

        self.search_security_phone = QLineEdit(self.search_security)
        self.search_security_phone.setObjectName(u"search_security_phone")

        self.gridLayout_4.addWidget(self.search_security_phone, 0, 1, 1, 1)

        self.search_security_email = QLineEdit(self.search_security)
        self.search_security_email.setObjectName(u"search_security_email")

        self.gridLayout_4.addWidget(self.search_security_email, 1, 0, 1, 1)

        self.search_security_location_name = QLineEdit(self.search_security)
        self.search_security_location_name.setObjectName(u"search_security_location_name")

        self.gridLayout_4.addWidget(self.search_security_location_name, 1, 1, 1, 1)

        self.btn_search_security = QPushButton(self.search_security)
        self.btn_search_security.setObjectName(u"btn_search_security")

        self.gridLayout_4.addWidget(self.btn_search_security, 2, 0, 1, 2)


        self.verticalLayout_33.addWidget(self.search_security)

        self.table_security = QTableWidget(self.page_security)
        self.table_security.setObjectName(u"table_security")

        self.verticalLayout_33.addWidget(self.table_security)

        self.pages_events.addWidget(self.page_security)

        self.horizontalLayout_4.addWidget(self.pages_events)


        self.verticalLayout.addWidget(self.main_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Selections.setCurrentIndex(1)
        self.pages_events.setCurrentIndex(0)
        self.formularies.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_aplication.setText(QCoreApplication.translate("MainWindow", u"MuseuVivo", None))
        self.btn_work_of_art.setText(QCoreApplication.translate("MainWindow", u"Work Of Art", None))
        self.btn_painting.setText(QCoreApplication.translate("MainWindow", u"Painting", None))
        self.btn_sculpture.setText(QCoreApplication.translate("MainWindow", u"Sculpture", None))
        self.btn_author.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        self.btn_exhibition.setText(QCoreApplication.translate("MainWindow", u"Exhibition", None))
        self.btn_exihibition_work_of_art.setText(QCoreApplication.translate("MainWindow", u"EW", None))
        self.btn_institution.setText(QCoreApplication.translate("MainWindow", u"Institution", None))
        self.btn_loan.setText(QCoreApplication.translate("MainWindow", u"Loan", None))
        self.btn_location.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.btn_visitor.setText(QCoreApplication.translate("MainWindow", u"Visitor", None))
        self.btn_ticket.setText(QCoreApplication.translate("MainWindow", u"Ticket", None))
        self.btn_guide.setText(QCoreApplication.translate("MainWindow", u"Guide", None))
        self.btn_guided_visit.setText(QCoreApplication.translate("MainWindow", u"GV", None))
        self.btn_security.setText(QCoreApplication.translate("MainWindow", u"Security", None))
        self.Selections.setItemText(self.Selections.indexOf(self.buttons), QCoreApplication.translate("MainWindow", u"Pages", None))
        self.btn_create.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.btn_update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.Selections.setItemText(self.Selections.indexOf(self.buttuns_events), QCoreApplication.translate("MainWindow", u"Events", None))
        self.msg_error.setText("")
        self.line_work_of_art_id.setText("")
        self.line_work_of_art_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identification", None))
        self.line_work_of_art_name.setText("")
        self.line_work_of_art_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.line_work_of_art_description.setText("")
        self.line_work_of_art_description.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.line_work_of_art_creation_date.setText("")
        self.line_work_of_art_creation_date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Creation Date", None))
        self.line_work_of_art_author_id.setText("")
        self.line_work_of_art_author_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Author identification", None))
        self.line_work_of_art_location_id.setText("")
        self.line_work_of_art_location_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Location identification", None))
        self.line_work_of_art_type.setText("")
        self.line_work_of_art_type.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.btn_apply_work_of_art.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.formularies.setTabText(self.formularies.indexOf(self.create_work_of_art), QCoreApplication.translate("MainWindow", u"Work of Art", None))
        self.line_painting_id.setText("")
        self.line_painting_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identification", None))
        self.line_painting_work_of_art_id.setText("")
        self.line_painting_work_of_art_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Work of Art Identification", None))
        self.line_painting_technique.setText("")
        self.line_painting_technique.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Technique", None))
        self.btn_apply_painting.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.formularies.setTabText(self.formularies.indexOf(self.create_painting), QCoreApplication.translate("MainWindow", u"Painting", None))
        self.line_sculpture_id.setText("")
        self.line_sculpture_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identification", None))
        self.line_sculpture_work_of_art_id.setText("")
        self.line_sculpture_work_of_art_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Work of Art Identification", None))
        self.line_sculpture_material.setText("")
        self.line_sculpture_material.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Material", None))
        self.line_sculpture_weight.setText("")
        self.line_sculpture_weight.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Weight", None))
        self.btn_apply_sculpture.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.formularies.setTabText(self.formularies.indexOf(self.create_sculpture), QCoreApplication.translate("MainWindow", u"Sculpture", None))
        self.line_exhibition_id.setText("")
        self.line_exhibition_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identification", None))
        self.line_exhibition_title.setText("")
        self.line_exhibition_title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.line_exhibition_description.setText("")
        self.line_exhibition_description.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.line_exhibition_start_date.setText("")
        self.line_exhibition_start_date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Start Date", None))
        self.line_exhibition_end_date.setText("")
        self.line_exhibition_end_date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"End date", None))
        self.btn_apply_exhibition.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.formularies.setTabText(self.formularies.indexOf(self.create_exhibition), QCoreApplication.translate("MainWindow", u"Exhibition", None))
        self.line_author_id.setText("")
        self.line_author_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identification", None))
        self.line_author_name.setText("")
        self.line_author_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.btn_apply_author.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.formularies.setTabText(self.formularies.indexOf(self.create_author), QCoreApplication.translate("MainWindow", u"Author", None))
        self.line_exhibition_work_of_art_work_id.setText("")
        self.line_exhibition_work_of_art_work_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Work of Art identification", None))
        self.line_exhibition_work_of_art_exhibition_id.setText("")
        self.line_exhibition_work_of_art_exhibition_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Exhibition identification", None))
        self.btn_apply_exhibition_work_of_art.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.formularies.setTabText(self.formularies.indexOf(self.create_exhibition_work_of_art), QCoreApplication.translate("MainWindow", u"EW", None))
        self.line_guide_id.setText("")
        self.line_guide_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identification", None))
        self.line_guide_name.setText("")
        self.line_guide_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.line_guide_email.setText("")
        self.line_guide_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.line_guide_phone.setText("")
        self.line_guide_phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.btn_apply_guide.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.formularies.setTabText(self.formularies.indexOf(self.create_guide), QCoreApplication.translate("MainWindow", u"Guide", None))
        self.line_guided_visits_id.setText("")
        self.line_guided_visits_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identification", None))
        self.line_guided_visits_group.setText("")
        self.line_guided_visits_group.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.line_guided_visits_visit_date.setText("")
        self.line_guided_visits_visit_date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Visit Date", None))
        self.line_guided_visits_hours.setText("")
        self.line_guided_visits_hours.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hours", None))
        self.line_guided_visits_guide_id.setText("")
        self.line_guided_visits_guide_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Guide identification", None))
        self.btn_apply_guided_visits.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.formularies.setTabText(self.formularies.indexOf(self.create_guided_visits), QCoreApplication.translate("MainWindow", u"GV", None))
        self.line_institution_id.setText("")
        self.line_institution_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identification", None))
        self.line_institution_name.setText("")
        self.line_institution_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"name", None))
        self.btn_apply_institution.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.formularies.setTabText(self.formularies.indexOf(self.create_institution), QCoreApplication.translate("MainWindow", u"Institution", None))
        self.line_loan_id.setText("")
        self.line_loan_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identification", None))
        self.line_loan_work_of_art_id.setText("")
        self.line_loan_work_of_art_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Work of Art identification", None))
        self.line_loan_institution_id.setText("")
        self.line_loan_institution_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Institution identification", None))
        self.line_loan_date.setText("")
        self.line_loan_date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Loan Date", None))
        self.line_loan_return_date.setText("")
        self.line_loan_return_date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Return Date", None))
        self.btn_apply_loan.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.formularies.setTabText(self.formularies.indexOf(self.create_loan), QCoreApplication.translate("MainWindow", u"Loan", None))
        self.line_location_id.setText("")
        self.line_location_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identification", None))
        self.line_location_name.setText("")
        self.line_location_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.btn_apply_location.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.formularies.setTabText(self.formularies.indexOf(self.create_location), QCoreApplication.translate("MainWindow", u"Location", None))
        self.line_security_id.setText("")
        self.line_security_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identification", None))
        self.line_security_name.setText("")
        self.line_security_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.line_security_email.setText("")
        self.line_security_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.line_security_phone.setText("")
        self.line_security_phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.line_security_location_id.setText("")
        self.line_security_location_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Location identification", None))
        self.btn_apply_security.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.formularies.setTabText(self.formularies.indexOf(self.create_security), QCoreApplication.translate("MainWindow", u"Security", None))
        self.line_ticket_id.setText("")
        self.line_ticket_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identification", None))
        self.line_ticket_visitor_id.setText("")
        self.line_ticket_visitor_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Visitor identification", None))
        self.line_ticket_type.setText("")
        self.line_ticket_type.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.line_ticket_visit_date.setText("")
        self.line_ticket_visit_date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Visit Date", None))
        self.line_ticket_purchase_date.setText("")
        self.line_ticket_purchase_date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Purchase Date", None))
        self.line_ticket_guide_id.setText("")
        self.line_ticket_guide_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Guide identification", None))
        self.btn_apply_ticket.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.formularies.setTabText(self.formularies.indexOf(self.create_ticket), QCoreApplication.translate("MainWindow", u"Ticket", None))
        self.line_visitor_id.setText("")
        self.line_visitor_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identification", None))
        self.line_visitor_name.setText("")
        self.line_visitor_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.line_visitor_email.setText("")
        self.line_visitor_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.line_visitor_phone.setText("")
        self.line_visitor_phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.btn_apply_visitor.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.formularies.setTabText(self.formularies.indexOf(self.create_visitor), QCoreApplication.translate("MainWindow", u"Visitor", None))
        self.search_author_name.setText("")
        self.search_author_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.search_author_id.setText("")
        self.search_author_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identification", None))
        self.btn_search_author.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_work_of_art_name.setText("")
        self.search_work_of_art_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.search_work_of_art_author_name.setText("")
        self.search_work_of_art_author_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Author Name", None))
        self.search_work_of_art_location_name.setText("")
        self.search_work_of_art_location_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Location Name", None))
        self.search_work_of_art_creation_date.setText("")
        self.search_work_of_art_creation_date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Creation Date", None))
        self.search_work_of_art_type.setText("")
        self.search_work_of_art_type.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.btn_search_work_of_art.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_painting_work_of_art_name.setText("")
        self.search_painting_work_of_art_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Work of Art Name", None))
        self.search_painting_technique.setText("")
        self.search_painting_technique.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Technique", None))
        self.btn_search_painting.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_sculpture_work_of_art_name.setText("")
        self.search_sculpture_work_of_art_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Work of Art Name", None))
        self.search_sculpture_material.setText("")
        self.search_sculpture_material.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Material", None))
        self.search_sculpture_weight.setText("")
        self.search_sculpture_weight.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Weight", None))
        self.btn_search_sculpture.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_exhibition_start_date.setText("")
        self.search_exhibition_start_date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Start Date", None))
        self.search_exhibition_name.setText("")
        self.search_exhibition_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.search_exhibition_end_date.setText("")
        self.search_exhibition_end_date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"End Date", None))
        self.btn_search_exhibition.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_ew_work_of_art_name.setText("")
        self.search_ew_work_of_art_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Work of Art Name", None))
        self.search_ew_exhibition_name.setText("")
        self.search_ew_exhibition_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Exhibition name", None))
        self.btn_serach_ew.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_institution_name.setText("")
        self.search_institution_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.search_institution_loan_date.setText("")
        self.search_institution_loan_date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Loan Date", None))
        self.search_institution_return_loan_date.setText("")
        self.search_institution_return_loan_date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Return Loan Date", None))
        self.btn_search_institution.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_loan_work_of_art_name.setText("")
        self.search_loan_work_of_art_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Work of Art Name", None))
        self.search_loan_institution_name.setText("")
        self.search_loan_institution_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Institution Name", None))
        self.search_loan_date.setText("")
        self.search_loan_date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Loan Date", None))
        self.search_loan_return_date.setText("")
        self.search_loan_return_date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Return Date", None))
        self.btn_search_loan.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_location_name.setText("")
        self.search_location_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.btn_search_location.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_visitor_name.setText("")
        self.search_visitor_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.search_visitor_email.setText("")
        self.search_visitor_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.search_visitor_phone.setText("")
        self.search_visitor_phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.btn_search_visitor.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_ticket_visitor_name.setText("")
        self.search_ticket_visitor_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Visitor Name", None))
        self.search_ticket_type.setText("")
        self.search_ticket_type.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.btn_search_ticket.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_guide_name.setText("")
        self.search_guide_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.search_guide_email.setText("")
        self.search_guide_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.search_guide_phone.setText("")
        self.search_guide_phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.btn_search_guide.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_gv_group.setText("")
        self.search_gv_group.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.search_gv_visit_date.setText("")
        self.search_gv_visit_date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Visit Date", None))
        self.search_gv_hours.setText("")
        self.search_gv_hours.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hours", None))
        self.search_gv_guide_name.setText("")
        self.search_gv_guide_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Guide Name", None))
        self.btn_search_gv.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_security_name.setText("")
        self.search_security_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.search_security_phone.setText("")
        self.search_security_phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.search_security_email.setText("")
        self.search_security_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.search_security_location_name.setText("")
        self.search_security_location_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Location Name", None))
        self.btn_search_security.setText(QCoreApplication.translate("MainWindow", u"Search", None))
    # retranslateUi

