# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from src.ui.CrawlResultWindow import CrawlResultWindow
from src.ui.DeepResultWindow import DeepResultWindow
from src.ui.ProgressThread import ProgressThread
import os, time
from src.utils.start_research import start_profile_research, sort_crawl_result
from src.ui.Loading import Loading

# creating a class
# that inherits the QDialog class
class MainWindow(QDialog):
 
    # constructor
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title = 'Skirnir'
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 400
        self.progressBarThread = None
        self.p = Loading()

        self.initUI()


    def initUI(self):

        # setting window title
        self.setWindowTitle("Skirnir")
        self.setWindowIcon(QIcon(os.path.abspath("data/Skirnir.png")))

        # print(os.path.abspath("data/Skirnir.png"))

        # setting geometry to the window
        self.setGeometry(self.left, self.top, self.width, self.height)

        # # Progress
        # self.progress = QProgressBar(self)
        # self.progress.setMaximum(100)

        # calling the method that create the form
        self.createForm()
        
        # calling the method to create Advanced settings 
        self.createAdvancedSettings()

        # creating a dialog button for ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # adding action when form is accepted
        self.buttonBox.accepted.connect(self.start_checking_profile)

        # adding action when form is rejected
        self.buttonBox.rejected.connect(self.reject)

        # creating a vertical layout
        mainLayout = QVBoxLayout()

        # adding form group box to the layout
        mainLayout.addWidget(self.formGroupBox)

        # adding limit size of generated nicknames
        mainLayout.addWidget(self.AdvancedSettings) 

        # # adding progress bar
        # mainLayout.addWidget(self.progress)

        # adding button box to the layout
        mainLayout.addWidget(self.buttonBox)

        # setting main layout
        self.setLayout(mainLayout)


    # Date can be invisible
    def toggleDateVisibility(self, state):
        show_date = state == Qt.Checked
        self.date.setVisible(show_date)

        if show_date:
            self.formGroupBox.layout().labelForField(self.date).show()
        else:
            self.formGroupBox.layout().labelForField(self.date).hide()

     # Hide names if the research is only on pseudo
    def toggleNamesVisibility(self, state):
        nickname_only = state == Qt.Checked
        self.Firstname.setVisible(not nickname_only)
        self.Lastname.setVisible(not nickname_only)

        if not nickname_only:
            self.formGroupBox.layout().labelForField(self.Firstname).show()
            self.formGroupBox.layout().labelForField(self.Lastname).show()
        else:
            self.formGroupBox.layout().labelForField(self.Firstname).hide()
            self.formGroupBox.layout().labelForField(self.Lastname).hide()

    def createAdvancedSettings(self):
        self.AdvancedSettings = QGroupBox("Advanced settings :")
        self.AdvancedSettingsLayout = QVBoxLayout()
        
        self.createCheckBoxForm()
        self.createSliderHorizontalLayout()

        self.AdvancedSettings.setLayout(self.AdvancedSettingsLayout)

    def createSliderHorizontalLayout(self):
        self.Sliderlayout = QHBoxLayout()
        # Slider value
        self.limitLabel = QLabel("Limit the size \n of generated nicknames :")

        self.limit = QLabel("13")

        # Slide Bar
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setFocusPolicy(Qt.NoFocus)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(1)
        self.slider.setSingleStep(1)
        self.slider.setRange(11, 15)
        self.slider.setValue(13)
        self.slider.valueChanged[int].connect(self.setLimit)
        self.slider.setStyleSheet(
                             "QSlider::handle:horizontal {"
                             "background-color: #e03d3d;"
                             "}")
        
        self.Sliderlayout.addWidget(self.limitLabel)
        self.Sliderlayout.addWidget(self.limit)
        self.Sliderlayout.addWidget(self.slider)
       

        # Add the QHBoxLayout to a container widget (QGroupBox) before adding it to the QVBoxLayout to avoid strange bugs 
        self.slider_container = QWidget()
        self.slider_container.setLayout(self.Sliderlayout)
        self.AdvancedSettingsLayout.addWidget(self.slider_container)
    
    def createCheckBoxForm(self):
        # creating a form layout
        formlayout = QFormLayout()

        # setting layout
        self.formGroupBox.setLayout(formlayout)

        # Surface Crawl Checkbox
        self.show_crawl_checkbox = QCheckBox()
        self.show_crawl_checkbox.setChecked(False)
        self.show_crawl_checkbox.stateChanged.connect(self.gray)

        # Instagram Checkbox
        self.show_instagram_checkbox = QCheckBox()
        self.show_instagram_checkbox.setChecked(True)

        # Facebook Checkbox
        self.show_facebook_checkbox = QCheckBox()
        self.show_facebook_checkbox.setChecked(True)

        # Twitter Checkbox
        self.show_twitter_checkbox = QCheckBox()
        self.show_twitter_checkbox.setChecked(True)
        
        # LinkedIn Checkbox
        self.show_linkedin_checkbox = QCheckBox()
        self.show_linkedin_checkbox.setChecked(True)

        formlayout.addRow(QLabel("Surface Crawl only"), self.show_crawl_checkbox)
        formlayout.addRow(QLabel(""))

        formlayout.addRow(self.show_instagram_checkbox, QLabel("Instagram"))
        formlayout.addRow(self.show_facebook_checkbox, QLabel("Facebook"))
        formlayout.addRow(self.show_twitter_checkbox, QLabel("Twitter"))
        formlayout.addRow(self.show_linkedin_checkbox, QLabel("LinkedIn"))

        self.AdvancedSettingsLayout.addLayout(formlayout)


    # create form method
    def createForm(self):
        reg_ex_firstname = QRegExp("[A-Za-z][A-Za-z]+(([\ \' \-]){1}[A-Za-z]+)")
        reg_ex_lastname = QRegExp("[A-Za-z][A-Za-z]+(([\ \' \-]){1}[A-Za-z]+)*")

        # creating a group box
        self.formGroupBox = QGroupBox("Search Form :")

        # Firstname
        self.Firstname = QLineEdit()
        input_validator = QRegExpValidator(reg_ex_firstname, self.Firstname)
        self.Firstname.setValidator(input_validator)

        # Lastname
        self.Lastname = QLineEdit()
        input_validator_lastname = QRegExpValidator(reg_ex_lastname, self.Lastname)
        self.Lastname.setValidator(input_validator_lastname)

        # Birthday
        self.date = QDateEdit()
        d = QDate(2020, 6, 10)
        self.date.setDate(d)

        # Nickname
        self.nickname_only = QCheckBox()
        self.nickname_only.setChecked(False)
        self.nickname_only.stateChanged.connect(self.toggleNamesVisibility)
        self.nickname = QLineEdit()
        

        # Date Checkbox
        self.show_date_checkbox = QCheckBox()
        self.show_date_checkbox.setChecked(True)
        self.show_date_checkbox.stateChanged.connect(self.toggleDateVisibility)

        # creating a form layout
        layout = QFormLayout()
 
        # adding rows for inputs
        layout.addRow(QLabel("Firstname: "), self.Firstname)
        layout.addRow(QLabel("Lastname: "), self.Lastname)
        layout.addRow(QLabel("Toggle Birthday: "), self.show_date_checkbox)
        layout.addRow(QLabel("Birthday: "), self.date)
        layout.addRow(QLabel("Search only the pseudo: "), self.nickname_only)
        layout.addRow(QLabel("Pseudo: "), self.nickname)

        # setting layout
        self.formGroupBox.setLayout(layout)

    # # when button is pressed this method is being called
    # def set_progress(self, value):
    #     self.progress.setValue(value)

    
    def start_loading_bar_thread(self, size):
        self.progressBarThread = ProgressThread(size)
        self.progressBarThread.reportProgress.connect(self.set_progress)
        # self.progressBarThread.calculationFinished.connect(self.calculationFinished)
        self.progressBarThread.start()

    def gray(self):
        if self.show_crawl_checkbox.isChecked():
            self.slider_container.setStyleSheet("color:grey;")
            self.slider.setStyleSheet(
                             "QSlider::handle:horizontal {"
                             "background-color: grey;"
                             "}")
            self.slider.setDisabled(True)
        else:
            self.slider_container.setStyleSheet("color:white")
            self.slider.setStyleSheet(
                             "QSlider::handle:horizontal {"
                             "background-color: #e03d3d;"
                             "}")
            self.slider.setDisabled(False)

    def setLimit(self, value):
        self.limit.setText(str(value))

    # call nickname generation function
    def start_checking_profile(self):
        self.showLoadingBar = True
        
        
        crawl_list, advanced_profile_set, social_networks_dict = start_profile_research(self.show_instagram_checkbox.isChecked(), self.show_facebook_checkbox.isChecked(),
                                    self.show_twitter_checkbox.isChecked(), self.show_linkedin_checkbox.isChecked(),
                                    self.Firstname.text(), self.Lastname.text(), self.date.text(), self.nickname.text(),
                                    self.show_date_checkbox.isChecked(), self.nickname_only.isChecked(), int(self.limit.text()), self.show_crawl_checkbox.isChecked())

        if self.show_crawl_checkbox.isChecked():
            self.w = CrawlResultWindow(crawl_list, social_networks_dict)
        else:
            crawl_set = sort_crawl_result(crawl_list)
            self.w = DeepResultWindow(crawl_set, advanced_profile_set, social_networks_dict)
        self.w.show()