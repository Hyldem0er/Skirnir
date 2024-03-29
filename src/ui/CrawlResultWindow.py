from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os, sys
import webbrowser
import pyperclip
from loguru import logger

logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")


def check_social_networks(item, social_networks):
    return any(sn in item for sn in social_networks)


class CrawlResultWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, crawl_list, social_networks_dict):
        super().__init__()
        self.left = 1000
        self.top = 200
        self.width = 500
        self.height = 400
        self.crawl_list = crawl_list
        self.show_instagram_filter = social_networks_dict["instagram"]
        self.show_facebook_filter = social_networks_dict["facebook"]
        self.show_twitter_filter = social_networks_dict["twitter"]
        self.show_linkedin_filter = social_networks_dict["linkedin"]
        self.show_tiktok_filter = social_networks_dict["tiktok"]
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.initUI()
       
    
    def initUI(self):
        # setting window title
        self.setWindowTitle("Skirnir")
        self.setWindowIcon(QIcon(os.path.abspath("data/Skirnir.png")))

        # setting geometry to the window
        self.setGeometry(self.left, self.top, self.width, self.height)

        mainLayout = QVBoxLayout()
        
        self.add_crawl_list_widget()

        self.open_in_web_browser_button = QPushButton("Open on Web Browser (urls selected: 0)")

        mainLayout.addWidget(self.crawl_list_group)
        mainLayout.addWidget(self.open_in_web_browser_button)

        self.setLayout(mainLayout)

        # Connect the functions with the appropriate button
        self.search_bar.textChanged.connect(self.search)
        self.open_in_web_browser_button.clicked.connect(self.open_in_web_browser)

        # Connect the itemSelectionChanged signal to a custom slot
        self.crawl_list_widget.itemSelectionChanged.connect(self.handleSelectionChanged)


    def add_crawl_list_widget(self):
        self.crawl_list_group = QGroupBox("Search bar :")
        crawl_list_group_layout = QVBoxLayout()

        checkbox_layout = QHBoxLayout()

        self.show_instagram_result = QCheckBox("Instagram")
        self.show_instagram_result.setChecked(True)

        self.show_facebook_result = QCheckBox("Facebook")
        self.show_facebook_result.setChecked(True)

        self.show_twitter_result = QCheckBox("Twitter")
        self.show_twitter_result.setChecked(True)

        self.show_linkedin_result = QCheckBox("LinkedIn")
        self.show_linkedin_result.setChecked(True)
        
        self.show_tiktok_result = QCheckBox("Tiktok")
        self.show_tiktok_result.setChecked(True)
        
        # Create a QListWidget
        self.crawl_list_widget = QListWidget()
        self.crawl_list_widget.setSelectionMode(3)
        self.crawl_list_widget.addItems(self.crawl_list)

        self.search_bar = QLineEdit()

        # Add widgets to crawl_list_group_layout
        crawl_list_group_layout.addWidget(self.search_bar)
        

        # Add social networks filter only if needed
        if self.show_instagram_filter:
            checkbox_layout.addWidget(self.show_instagram_result)
            self.show_instagram_result.clicked.connect(self.search)

        if self.show_facebook_filter:
            checkbox_layout.addWidget(self.show_facebook_result)
            self.show_facebook_result.clicked.connect(self.search)

        if self.show_twitter_filter:
            checkbox_layout.addWidget(self.show_twitter_result)
            self.show_twitter_result.clicked.connect(self.search)

        if self.show_linkedin_filter:
            checkbox_layout.addWidget(self.show_linkedin_result)
            self.show_linkedin_result.clicked.connect(self.search)

        if self.show_tiktok_filter:
            checkbox_layout.addWidget(self.show_tiktok_result)
            self.show_tiktok_result.clicked.connect(self.search)


        # Add the QHBoxLayout to a container widget (QGroupBox) before adding it to the QVBoxLayout to avoid strange bugs 
        container = QWidget()
        container.setLayout(checkbox_layout)
        crawl_list_group_layout.addWidget(container)

        crawl_list_group_layout.addWidget(self.crawl_list_widget)

        self.crawl_list_group.setLayout(crawl_list_group_layout)
    
      
    def search(self):

        search_term = self.search_bar.text()
        social_networks = []
        
        # Add Social network filter 
        if self.show_instagram_result.isChecked() and self.show_instagram_filter: social_networks.append("instagram")
        if self.show_facebook_result.isChecked() and self.show_facebook_filter: social_networks.append("facebook")
        if self.show_twitter_result.isChecked() and self.show_twitter_filter: social_networks.append("twitter")
        if self.show_linkedin_result.isChecked() and self.show_linkedin_filter: social_networks.append("linkedin")
        if self.show_tiktok_result.isChecked() and self.show_tiktok_filter: social_networks.append("tiktok")

        if search_term:
            for index in range(self.crawl_list_widget.count()):
                item = self.crawl_list_widget.item(index)
                if search_term in item.text() and check_social_networks(item.text(), social_networks):
                    item.setHidden(False)
                else:
                    item.setHidden(True)
        else:
             for index in range(self.crawl_list_widget.count()):
                item = self.crawl_list_widget.item(index)
                if check_social_networks(item.text(), social_networks):
                    item.setHidden(False)
                else:
                    item.setHidden(True)

    def open_in_web_browser(self):
        selected_items = self.crawl_list_widget.selectedItems()
        for url in selected_items:
            webbrowser.open(url.text())

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if event.key() == Qt.Key_C and (event.modifiers() & Qt.ControlModifier):
            logger.info("Ctrl + C")
            selected_items = self.crawl_list_widget.selectedItems()

            urls = ""
            for url in selected_items:
                urls += url.text() + "\n"
            pyperclip.copy(urls)

            # # Create the mime data with the selected urls
            # mime_data = QMimeData()
            # mime_data.setUrls(urls)

            # # Copy the mime data to the clipboard.
            # clipboard = QApplication.clipboard()
            # clipboard.setMimeData(mime_data)

            # event = QEvent(QEvent.Clipboard)
            # QApplication.sendEvent(clipboard, event)

    def handleSelectionChanged(self):
        selected_items = self.crawl_list_widget.selectedItems()
        if selected_items:
            num_selected_items = len(selected_items)
            text = f"Open on Web Browser (urls selected: {num_selected_items})"
            self.open_in_web_browser_button.setText(text)
        else:
            text = f"Open on Web Browser (urls selected: 0)"
            self.open_in_web_browser_button.setText(text)