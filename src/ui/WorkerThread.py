from PyQt5.QtCore import QThread, pyqtSignal
from src.utils.start_research import start_profile_research
from src.utils.login import open_social_network_login_page

class WorkerThread(QThread):
    finished = pyqtSignal(object)

    def __init__(self, show_instagram_checkbox=False, show_facebook_checkbox=False, show_twitter_checkbox=False, show_linkedin_checkbox=False,
                 show_tiktok_checkbox=False, Firstname=None, Lastname=None, date=None, alias=None, show_date_checkbox=False, alias_only=False,
                 limit=None, show_deepcrawl_checkbox=False, show_exportCSV_checkbox=False, keyword="", proxyfile_path="", w=None):
        super(WorkerThread, self).__init__()
        self.show_instagram_checkbox = show_instagram_checkbox
        self.show_facebook_checkbox = show_facebook_checkbox
        self.show_twitter_checkbox = show_twitter_checkbox
        self.show_linkedin_checkbox = show_linkedin_checkbox
        self.show_tiktok_checkbox = show_tiktok_checkbox
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.date = date
        self.alias = alias
        self.show_date_checkbox = show_date_checkbox
        self.alias_only = alias_only
        self.limit = limit
        self.show_deepcrawl_checkbox = show_deepcrawl_checkbox 
        self.show_exportCSV_checkbox = show_exportCSV_checkbox
        self.keyword = keyword
        self.proxyfile_path = proxyfile_path
        self.w = None

    def run(self):
        """
        Executes the worker thread task.
        """
        # Move your time-consuming operations here
        self.number_of_start = 0
        self.number_of_start += 1
        if self.number_of_start == 1: # Open social network login page only on first launch
            open_social_network_login_page(self.show_instagram_checkbox, self.show_facebook_checkbox,
                self.show_twitter_checkbox, self.show_linkedin_checkbox, self.show_tiktok_checkbox)

        crawl_list, advanced_profile_set, social_networks_dict = start_profile_research(self.show_instagram_checkbox, self.show_facebook_checkbox,
                                    self.show_twitter_checkbox, self.show_linkedin_checkbox, self.show_tiktok_checkbox, 
                                    self.Firstname, self.Lastname, self.date, self.alias,
                                    self.show_date_checkbox, self.alias_only, self.limit, self.show_deepcrawl_checkbox,
                                    self.show_exportCSV_checkbox, self.keyword, self.proxyfile_path)

        self.finished.emit((crawl_list, advanced_profile_set, social_networks_dict))
