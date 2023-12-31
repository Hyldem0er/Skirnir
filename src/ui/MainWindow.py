# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from src.ui.CrawlResultWindow import CrawlResultWindow
from src.ui.DeepResultWindow import DeepResultWindow
from src.ui.ProgressThread import ProgressThread
import os, time, sys
from src.utils.start_research import start_profile_research, sort_crawl_result
from src.ui.Loading import Loading
from src.utils.login import open_social_network_login_page
from loguru import logger
from src.surface_crawl.match_nicknames import list_nicknames
from src.relevance.sort_by_relevance import sort_by_relevance
import copy

logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")

list_of_nickname = list_nicknames()

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
        self.number_of_start = 0
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
        self.createExportButton()

        self.AdvancedSettings.setLayout(self.AdvancedSettingsLayout)

    def createSliderHorizontalLayout(self):
        self.Sliderlayout = QHBoxLayout()
        # Slider value
        self.limitLabel = QLabel("Limit the size of generated nicknames :")


        # Slide Bar
        limit = 9

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setFocusPolicy(Qt.NoFocus)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(1)
        self.slider.setSingleStep(1)
        self.slider.setRange(3, 15)
        self.slider.setValue(limit)
        self.slider.valueChanged[int].connect(self.setLimit)
        self.slider.setStyleSheet(
                             "QSlider::handle:horizontal {"
                             "background-color: #e03d3d;"
                             "}")
        
        self.Sliderlayout.addWidget(self.limitLabel)
        self.limit = QLabel(str(limit))
        self.Sliderlayout.addWidget(self.limit)
        self.Sliderlayout.addWidget(self.slider)
       

        # Add the QHBoxLayout to a container widget (QGroupBox) before adding it to the QVBoxLayout to avoid strange bugs 
        self.slider_container = QWidget()
        self.slider_container.setLayout(self.Sliderlayout)
        self.AdvancedSettingsLayout.addWidget(self.slider_container)
        self.slider_container.setStyleSheet("color:grey;")
        self.slider.setStyleSheet(
                            "QSlider::handle:horizontal {"
                            "background-color: grey;"
                            "}")
        self.slider.setDisabled(True)
    
    def createCheckBoxForm(self):
        # creating a form layout
        formlayout = QFormLayout()

        # # setting layout
        # self.formGroupBox.setLayout(formlayout)

        # DeepCrawl Checkbox
        self.show_deepcrawl_checkbox = QCheckBox()
        self.show_deepcrawl_checkbox.setChecked(False)
        self.show_deepcrawl_checkbox.stateChanged.connect(self.gray)
        

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

        checkboxlayout = QVBoxLayout()
        checkboxlayout.setSpacing(0)  # Adjust the spacing between elements
        checkboxlayout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero
        checkboxlayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        checkboxcontainer = QWidget()

        instaLayout = QHBoxLayout()
        instaLayout.setSpacing(0)  # Adjust the spacing between elements
        instaLayout.setContentsMargins(0, 10, 0, 0)  # Set margins to zero
        instaLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        instaLayout.addWidget(self.show_instagram_checkbox)
        instaLayout.addWidget(QLabel("Instagram"))
        instacontainer = QWidget()
        instacontainer.setLayout(instaLayout)

        fbLayout = QHBoxLayout()
        fbLayout.setSpacing(0)  # Adjust the spacing between elements
        fbLayout.setContentsMargins(0, 10, 0, 0)  # Set margins to zero
        fbLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        fbLayout.addWidget(self.show_facebook_checkbox)
        fbLayout.addWidget(QLabel("Facebook"))
        fbcontainer = QWidget()
        fbcontainer.setLayout(fbLayout)

        twitterLayout = QHBoxLayout()
        twitterLayout.setSpacing(0)  # Adjust the spacing between elements
        twitterLayout.setContentsMargins(0, 10, 0, 0)  # Set margins to zero
        twitterLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        twitterLayout.addWidget(self.show_twitter_checkbox)
        twitterLayout.addWidget(QLabel("Twitter"))
        twittercontainer = QWidget()
        twittercontainer.setLayout(twitterLayout)

        linkedinLayout = QHBoxLayout()
        linkedinLayout.setSpacing(0)  # Adjust the spacing between elements
        linkedinLayout.setContentsMargins(0, 10, 0, 0)  # Set margins to zero
        linkedinLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        linkedinLayout.addWidget(self.show_linkedin_checkbox)
        linkedinLayout.addWidget(QLabel("LinkedIn"))
        linkedincontainer = QWidget()
        linkedincontainer.setLayout(linkedinLayout)

        checkboxlayout.addWidget(instacontainer)
        checkboxlayout.addWidget(fbcontainer)
        checkboxlayout.addWidget(twittercontainer)
        checkboxlayout.addWidget(linkedincontainer)
        checkboxcontainer.setLayout(checkboxlayout)

        formlayout.setVerticalSpacing(15)
        
        formlayout.addRow(checkboxcontainer)
        formlayout.addRow(QLabel("Deep Crawl"), self.show_deepcrawl_checkbox)

        self.AdvancedSettingsLayout.addLayout(formlayout)
        
    def createExportButton(self):

        export_layout = QHBoxLayout()
        export_layout.addWidget(QLabel("Export generated nickanmes in CSV"))

        # DeepCrawl Checkbox
        self.show_exportCSV_checkbox = QCheckBox()
        self.show_exportCSV_checkbox.setChecked(False)
        self.show_exportCSV_checkbox.stateChanged.connect(self.gray)
        self.show_exportCSV_checkbox.setDisabled(True)

        
        export_layout.addWidget(self.show_exportCSV_checkbox)
        self.exportCSV = QWidget()
        self.exportCSV.setLayout(export_layout)
        self.exportCSV.setStyleSheet("color:grey;")


        self.AdvancedSettingsLayout.addWidget(self.exportCSV)

    def createForm(self):
        # Regular expression pattern for first name with accented letters
        pattern_firstname = "[A-Za-zÀ-ÖØ-öø-ÿ]+((['\\-\\s])[A-Za-zÀ-ÖØ-öø-ÿ]+)"
        # Regular expression pattern for last name with accented letters
        pattern_lastname = "[A-Za-zÀ-ÖØ-öø-ÿ]+((['\\-\\s])[A-Za-zÀ-ÖØ-öø-ÿ]+)*"

        # Create QRegExp objects with the patterns
        reg_ex_firstname = QRegExp(pattern_firstname)
        reg_ex_lastname = QRegExp(pattern_lastname)

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
        self.show_date_checkbox.setChecked(False)
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
        self.formGroupBox.layout().labelForField(self.date).hide()
        self.date.hide()

    # # when button is pressed this method is being called
    # def set_progress(self, value):
    #     self.progress.setValue(value)

    
    def start_loading_bar_thread(self, size):
        self.progressBarThread = ProgressThread(size)
        self.progressBarThread.reportProgress.connect(self.set_progress)
        # self.progressBarThread.calculationFinished.connect(self.calculationFinished)
        self.progressBarThread.start()

    def gray(self):
        if not self.show_deepcrawl_checkbox.isChecked():
            self.slider_container.setStyleSheet("color:grey;")
            self.slider.setStyleSheet(
                             "QSlider::handle:horizontal {"
                             "background-color: grey;"
                             "}")
            self.slider.setDisabled(True)
            self.exportCSV.setStyleSheet("color:grey;")
            self.show_exportCSV_checkbox.setDisabled(True)
            self.show_exportCSV_checkbox.setCheckState(False)

        else:
            self.slider_container.setStyleSheet("color:white")
            self.slider.setStyleSheet(
                             "QSlider::handle:horizontal {"
                             "background-color: #e03d3d;"
                             "}")
            self.slider.setDisabled(False)
            self.exportCSV.setStyleSheet("color:white;")
            self.show_exportCSV_checkbox.setDisabled(False)



    def setLimit(self, value):
        self.limit.setText(str(value))

    # call nickname generation function
    def start_checking_profile(self):
        self.number_of_start += 1
        if self.number_of_start == 1: # Open social network login page only on first launch
            open_social_network_login_page(self.show_instagram_checkbox.isChecked(), self.show_facebook_checkbox.isChecked(),
                self.show_twitter_checkbox.isChecked(), self.show_linkedin_checkbox.isChecked())
        self.showLoadingBar = True
        logger.info("Start Crawling")
        
        crawl_list, advanced_profile_set, social_networks_dict = start_profile_research(self.show_instagram_checkbox.isChecked(), self.show_facebook_checkbox.isChecked(),
                                    self.show_twitter_checkbox.isChecked(), self.show_linkedin_checkbox.isChecked(),
                                    self.Firstname.text(), self.Lastname.text(), self.date.text(), self.nickname.text(),
                                    self.show_date_checkbox.isChecked(), self.nickname_only.isChecked(), int(self.limit.text()), self.show_deepcrawl_checkbox.isChecked(),
                                    self.show_exportCSV_checkbox.isChecked())


        if self.show_deepcrawl_checkbox.isChecked():
            crawl_set = sort_crawl_result(crawl_list)
            backup_facebook = copy.deepcopy(advanced_profile_set["facebook"])
            for platform in crawl_set:
                advanced_profile_set[platform].extend(crawl_set[platform])

            advanced_profile_set['instagram'] = sort_by_relevance(advanced_profile_set['instagram'], self.Firstname.text(), self.Lastname.text(),  self.nickname.text(), list_of_nickname, self.nickname_only.isChecked())
            advanced_profile_set['facebook'] = sort_by_relevance(advanced_profile_set['facebook'], self.Firstname.text(), self.Lastname.text(),  self.nickname.text(), list_of_nickname, self.nickname_only.isChecked())
            advanced_profile_set['twitter'] = sort_by_relevance(advanced_profile_set['twitter'], self.Firstname.text(), self.Lastname.text(),  self.nickname.text(), list_of_nickname, self.nickname_only.isChecked())
            advanced_profile_set['linkedin'] = sort_by_relevance(advanced_profile_set['linkedin'], self.Firstname.text(), self.Lastname.text(),  self.nickname.text(), list_of_nickname, self.nickname_only.isChecked())
            
            self.w = DeepResultWindow(advanced_profile_set, social_networks_dict, backup_facebook)
        else:
            crawl_list = sort_by_relevance(set(crawl_list), self.Firstname.text(), self.Lastname.text(),  self.nickname.text(), list_of_nickname, self.nickname_only.isChecked())
            self.w = CrawlResultWindow(crawl_list, social_networks_dict)

      
        self.w.show()