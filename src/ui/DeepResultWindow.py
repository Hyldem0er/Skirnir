from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QClipboard
import os
import webbrowser

def check_social_networks(item, social_networks):
    return any(sn in item for sn in social_networks)


class DeepResultWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, crawl_set, social_networks_dict, backup_facebook):
        super().__init__()
        self.left = 1000
        self.top = 200
        self.width = 500
        self.height = 400
        self.crawl_set = crawl_set
        self.show_instagram_tab = social_networks_dict["instagram"]
        self.show_facebook_tab = social_networks_dict["facebook"]
        self.show_twitter_tab = social_networks_dict["twitter"]
        self.show_linkedin_tab = social_networks_dict["linkedin"]
        self.backup_facebook = backup_facebook

        self.initUI()
       
    
    def initUI(self):
        # setting window title
        self.setWindowTitle("Skirnir")
        self.setWindowIcon(QIcon(os.path.abspath("data/Skirnir.png")))

       
        mainLayout = QVBoxLayout()

        # setting geometry to the window
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.create_tabs()

        mainLayout.addWidget(self.tabs)
        self.setLayout(mainLayout)


    def create_tabs(self):
        self.instagram_tab = QWidget()
        self.facebook_tab = QWidget()
        self.twitter_tab = QWidget()
        self.linkedin_tab = QWidget()

        if self.show_instagram_tab:
            self.tabs.addTab(self.instagram_tab, "Instagram")
            self.add_social_networks_list_widget(self.instagram_tab, "instagram")
        
        if self.show_facebook_tab:
            self.tabs.addTab(self.facebook_tab, "Facebook")
            self.add_social_networks_list_widget(self.facebook_tab, "facebook")

        if self.show_twitter_tab: 
            self.tabs.addTab(self.twitter_tab, "Twitter")
            self.add_social_networks_list_widget(self.twitter_tab, "twitter")
        
        if self.show_linkedin_tab: 
            self.tabs.addTab(self.linkedin_tab, "LinkedIn")
            self.add_social_networks_list_widget(self.linkedin_tab, "linkedin")

    def add_social_networks_list_widget(self, tab, social_network):
        tab.layout = QVBoxLayout()  
    
        # Create a QListWidget
        tab.list_widget = QListWidget()
        tab.list_widget.setSelectionMode(3)
        tab.list_widget.addItems(self.crawl_set[social_network])

        self.color_deduced_results(tab, social_network)

        tab.search_bar = QLineEdit()
        tab.open_in_web_browser_button = QPushButton("Open on Web Browser ")

        # Connect the functions with the appropriate button
        tab.search_bar.textChanged.connect(lambda : self.search(tab))
        tab.open_in_web_browser_button.clicked.connect(lambda : self.open_in_web_browser(tab))

        # Add widgets to crawl_list_group_layout
        tab.layout.addWidget(tab.search_bar)
        tab.layout.addWidget(tab.list_widget)
        tab.layout.addWidget(tab.open_in_web_browser_button)

        tab.setLayout(tab.layout)


    def color_deduced_results(self, tab, social_network):
        if social_network != "facebook":
            return
        for index in range(0, tab.list_widget.count()):
            item = tab.list_widget.item(index)
            if item.text() in self.backup_facebook:
                tab.list_widget.item(index).setBackground(QColor("#7c2929"))

    def search(self, tab):

        search_term = tab.search_bar.text()

        if search_term:
            for index in range(tab.list_widget.count()):
                item = tab.list_widget.item(index)
                # tab.list_widget.item(index).setBackground(QColor("red"))
                if search_term in item.text():
                    item.setHidden(False)
                else:
                    item.setHidden(True)

        else:
             for index in range(tab.list_widget.count()):
                item = tab.list_widget.item(index)
                item.setHidden(False)

    def open_in_web_browser(self, tab):
        selected_items = tab.list_widget.selectedItems()
        for url in selected_items:
            webbrowser.open(url.text())