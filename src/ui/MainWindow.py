# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os, time, sys
from loguru import logger
from src.ui.WorkerThread import WorkerThread
from src.utils.start_research import sort_crawl_result
from src.relevance.sort_by_relevance import sort_by_relevance
from src.ui.CrawlResultWindow import CrawlResultWindow
from src.ui.DeepResultWindow import DeepResultWindow
import copy
import os, time, sys
from src.surface_crawl.match_nicknames import list_nicknames
from superqt import QLabeledRangeSlider
from src.utils.stylecss import range_style_sheet, result_style_sheet
os.environ["USE_MAC_SLIDER_PATCH"] = "1"

list_of_nicknames = list_nicknames()

scriptDir = os.path.dirname(os.path.realpath(__file__))
gifFile = (scriptDir + os.path.sep + 'loading.gif')

logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")

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
        self.number_of_start = 0
        self.initUI()


    def initUI(self):

        # setting window title
        self.setWindowTitle("Skirnir")
        self.setWindowIcon(QIcon(os.path.abspath("data/Skirnir.png")))

        # print(os.path.abspath("data/Skirnir.png"))

        # setting geometry to the window
        self.setGeometry(self.left, self.top, self.width, self.height)


        # calling the method that create the form
        self.createForm()
        
        # calling the method to create Advanced settings 
        self.createAdvancedSettings()

        # creating a dialog button for ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # adding action when form is accepted
        # adding action when form is accepted
        
        self.buttonBox.accepted.connect(self.start_checking_profile)

        # adding action when form is rejected
        self.buttonBox.rejected.connect(self.reject)

        # creating a vertical layout
        mainLayout = QVBoxLayout()

        # adding form group box to the layout
        mainLayout.addWidget(self.formGroupBox)

        # adding limit size of generated aliass
        mainLayout.addWidget(self.AdvancedSettings) 

        # Add a loading gif
        self.label = QLabel()
        mainLayout.addWidget(self.label)

        self.movie = QMovie(gifFile)
        self.label.setMovie(self.movie)
        self.label.setAlignment(Qt.AlignCenter)
        self.movie.start()
        self.label.hide()

        # adding button box to the layout
        mainLayout.addWidget(self.buttonBox)

        # setting main layout
        self.setLayout(mainLayout)

        # Activate drag/drop
        self.setAcceptDrops(True)


    # Date can be invisible
    def toggleDateVisibility(self, state):
        show_date = state == Qt.Checked
        self.date.setVisible(show_date)

        if show_date:
            self.formGroupBox.layout().labelForField(self.date).show()
        else:
            self.formGroupBox.layout().labelForField(self.date).hide()

     # Hide names if the research is only on alias
    def toggleNamesVisibility(self, state):
        alias_only = state == Qt.Checked
        self.Firstname.setVisible(not alias_only)
        self.Lastname.setVisible(not alias_only)

        if not alias_only:
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
        self.createImportProxyFileButton()

        self.AdvancedSettings.setLayout(self.AdvancedSettingsLayout)

    def createSliderHorizontalLayout(self):
        self.Sliderlayout = QVBoxLayout()
        # Slider value
        self.limitLabel = QLabel("Limit the size of generated nicknames :")

        # Slide Bar
        limit = 9

        self.rangeSlider = QLabeledRangeSlider(Qt.Orientation.Horizontal)
        self.rangeSlider.setValue((5, 12))
        self.rangeSlider.setRange(2, 15)
        
        self.Sliderlayout.addWidget(self.limitLabel)
        self.Sliderlayout.addWidget(self.rangeSlider)
       

        # Add the QHBoxLayout to a container widget (QGroupBox) before adding it to the QVBoxLayout to avoid strange bugs 
        self.slider_container = QWidget()
        self.slider_container.setLayout(self.Sliderlayout)
        self.AdvancedSettingsLayout.addWidget(self.slider_container)

        self.slider_container.setStyleSheet("color:grey;")
        self.rangeSlider.setStyleSheet(
                            "QSlider::handle:horizontal {"
                            "background-color: grey;"
                            "}")
        self.rangeSlider.setDisabled(True)
    
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

        # TikTok Checkbox
        self.show_tiktok_checkbox = QCheckBox()
        self.show_tiktok_checkbox.setChecked(True)

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

        tiktokLayout = QHBoxLayout()
        tiktokLayout.setSpacing(0)  # Adjust the spacing between elements
        tiktokLayout.setContentsMargins(0, 10, 0, 0)  # Set margins to zero
        tiktokLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        tiktokLayout.addWidget(self.show_tiktok_checkbox)
        tiktokLayout.addWidget(QLabel("TikTok"))
        tiktokcontainer = QWidget()
        tiktokcontainer.setLayout(tiktokLayout)

        checkboxlayout.addWidget(instacontainer)
        checkboxlayout.addWidget(fbcontainer)
        checkboxlayout.addWidget(twittercontainer)
        checkboxlayout.addWidget(linkedincontainer)
        checkboxlayout.addWidget(tiktokcontainer)
        checkboxcontainer.setLayout(checkboxlayout)

        formlayout.setVerticalSpacing(15)
        
        formlayout.addRow(checkboxcontainer)
        formlayout.addRow(QLabel("Deep Crawl*", toolTip="Tries generated aliass on selected social networks"), self.show_deepcrawl_checkbox)

        self.AdvancedSettingsLayout.addLayout(formlayout)
        
    def createExportButton(self):

        export_layout = QHBoxLayout()
        export_layout.addWidget(QLabel("Export generated nicknames in CSV"))

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

    def createImportProxyFileButton(self):

        self.proxyfile_path = ""

        export_layout = QHBoxLayout()
        export_layout.addWidget(QLabel("Import you custom private/public proxy list : "))

        # Create a button
        self.import_button = QPushButton('Import File', self)
        self.import_button.clicked.connect(self.show_file_dialog)
        
        export_layout.addWidget(self.import_button)

        self.proxy= QWidget()
        self.proxy.setLayout(export_layout)
        self.AdvancedSettingsLayout.addWidget(self.proxy)

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

        # Alias
        self.alias_only = QCheckBox()
        self.alias_only.setChecked(False)
        self.alias_only.stateChanged.connect(self.toggleNamesVisibility)
        self.alias = QLineEdit()

        # Keyword
        self.keyword = QLineEdit()

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
        layout.addRow(QLabel("Search only the alias: "), self.alias_only)
        layout.addRow(QLabel(("Alias* : "), toolTip="Adds an additional search if an alias is known"), self.alias)
        layout.addRow(QLabel(("Keyword* : "), toolTip="Adds a keyword or a boolean query to complete the first and last name search"), self.keyword)

        # setting layout
        self.formGroupBox.setLayout(layout)
        self.formGroupBox.layout().labelForField(self.date).hide()
        self.date.hide()

    def gray(self):
        if not self.show_deepcrawl_checkbox.isChecked():
            self.slider_container.setStyleSheet("color:grey;")
            self.rangeSlider.setStyleSheet(
                             "QSlider::handle:horizontal {"
                             "background-color: grey;"
                             "}")
            self.rangeSlider.setDisabled(True)
            self.exportCSV.setStyleSheet("color:grey;")
            self.show_exportCSV_checkbox.setDisabled(True)
            self.show_exportCSV_checkbox.setCheckState(False)

        else:
            self.slider_container.setStyleSheet("color:white")
            self.rangeSlider.setStyleSheet(range_style_sheet)
            self.rangeSlider.setDisabled(False)
            self.exportCSV.setStyleSheet("color:white;")
            self.show_exportCSV_checkbox.setDisabled(False)

    def show_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File to Import", "", "All Files (*);;Text Files (*.txt)", options=options)

        if file_name:
            logger.info(f"Selected file: {file_name}")
            self.import_button.setText(file_name.split('/')[-1])
            self.proxyfile_path = file_name

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self.import_button.setText('Drop here to import')
            self.setStyleSheet("background-color: #343A48;")

    def dropEvent(self, event):
        files = [url.toLocalFile() for url in event.mimeData().urls()]
        if files:
            first_file = files[0]
            logger.info(f"Files dropped: {first_file}")
            self.import_button.setText(first_file.split('/')[-1])
            self.proxyfile_path = first_file
        self.setStyleSheet("")
    
    def dragLeaveEvent(self, event):
        self.import_button.setText('Import File')
        self.setStyleSheet("")  # Reset window style to default

    def setLimit(self, value):
        self.limit.setText(str(value))

    def on_worker_finished(self, result):
        self.label.hide()
        self.adjustSize()
        crawl_list, advanced_profile_set, social_networks_dict = result

        if self.show_deepcrawl_checkbox.isChecked():
            crawl_set = sort_crawl_result(crawl_list)
            backup_facebook = copy.deepcopy(advanced_profile_set["facebook"])
            for platform in crawl_set:
                if crawl_set[platform]:
                    advanced_profile_set[platform].extend(crawl_set[platform])

            advanced_profile_set['instagram'] = sort_by_relevance(advanced_profile_set['instagram'], self.Firstname.text(), self.Lastname.text(),  self.alias.text(), list_of_nicknames, self.alias_only.isChecked())
            advanced_profile_set['facebook'] = sort_by_relevance(advanced_profile_set['facebook'], self.Firstname.text(), self.Lastname.text(),  self.alias.text(), list_of_nicknames, self.alias_only.isChecked())
            advanced_profile_set['twitter'] = sort_by_relevance(advanced_profile_set['twitter'], self.Firstname.text(), self.Lastname.text(),  self.alias.text(), list_of_nicknames, self.alias_only.isChecked())
            advanced_profile_set['linkedin'] = sort_by_relevance(advanced_profile_set['linkedin'], self.Firstname.text(), self.Lastname.text(),  self.alias.text(), list_of_nicknames, self.alias_only.isChecked())
            advanced_profile_set['tiktok'] = sort_by_relevance(advanced_profile_set['tiktok'], self.Firstname.text(), self.Lastname.text(),  self.alias.text(), list_of_nicknames, self.alias_only.isChecked())
            
            self.w = DeepResultWindow(advanced_profile_set, social_networks_dict, backup_facebook)
            self.w.setStyleSheet(result_style_sheet)
        else:
            crawl_list = sort_by_relevance(set(crawl_list), self.Firstname.text(), self.Lastname.text(),  self.alias.text(), list_of_nicknames, self.alias_only.isChecked())
            self.w = CrawlResultWindow(crawl_list, social_networks_dict)
            self.w.setStyleSheet(result_style_sheet)
        self.w.show()
    
    # call alias generation function
    def start_checking_profile(self):
        print(self.proxyfile_path)
        self.label.show()
        self.worker_thread = WorkerThread(self.show_instagram_checkbox.isChecked(), self.show_facebook_checkbox.isChecked(),
                                    self.show_twitter_checkbox.isChecked(), self.show_linkedin_checkbox.isChecked(), self.show_tiktok_checkbox.isChecked(),
                                    self.Firstname.text(), self.Lastname.text(), self.date.text(), self.alias.text(),
                                    self.show_date_checkbox.isChecked(), self.alias_only.isChecked(), self.rangeSlider.value(), self.show_deepcrawl_checkbox.isChecked(),
                                    self.show_exportCSV_checkbox.isChecked(), self.keyword.text(), self.proxyfile_path, self)
        self.worker_thread.finished.connect(self.on_worker_finished)
        self.worker_thread.start()