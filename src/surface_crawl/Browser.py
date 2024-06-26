from src.surface_crawl.create_url_or_query import *
import sys
from loguru import logger
from src.surface_crawl.match_nicknames import match_nicknames, create_query_matching_nicknames
import urllib.parse

logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")

class Browser:
    """
    Represents a web browser.

    Args:
        name (str): The name of the browser.
        research_url (str or None, optional): The research URL associated with the browser. Defaults to None.

    Attributes:
        name (str): The name of the browser.
        research_urls (str or None): The research URL associated with the browser.

    Methods:
        get_name(): Returns the name of the browser.
        get_research_urls(): Returns the research URL associated with the browser.
        perform_surface_crawl(instagram, facebook, twitter, linkedin, name): Performs a surface crawl on specified platforms.

    Example:
        >>> browser = Browser("google", research_url="https://www.google.com")
        >>> browser.get_name()
        'google'
        >>> browser.get_research_urls()
        'https://www.google.com'
        >>> browser.perform_surface_crawl(instagram=True, facebook=True, twitter=True, linkedin=True, name="JohnDoe")
        ['result1', 'result2', 'result3']
    """

    def __init__(self, name, research_url=None):
        self.name = name
        self.research_urls = research_url

    def get_name(self):
        """
        Returns the name of the browser.

        Returns:
            str: The name of the browser.
        """
        return self.name

    def get_research_urls(self):
        """
        Returns the research URL associated with the browser.

        Returns:
            str or None: The research URL associated with the browser.
        """
        return self.research_urls

    def perform_surface_crawl(self, instagram, facebook, twitter, linkedin, tiktok, firstname, lastname, alias, keyword, proxy):
        """
        Performs a surface crawl on specified platforms using the browser.
        
        Args:
            instagram (bool): Flag indicating whether to perform a surface crawl on Instagram.
            facebook (bool): Flag indicating whether to perform a surface crawl on Facebook.
            twitter (bool): Flag indicating whether to perform a surface crawl on Twitter.
            linkedin (bool): Flag indicating whether to perform a surface crawl on LinkedIn.
            tiktok (bool): Flag indicating whether to perform a surface crawl on TikTok.
            firstname (str): The first name for the surface crawl.
            lastname (str): The last name for the surface crawl.
            alias (str): The alias used for the surface crawl.
            keyword (str): The keyword for the surface crawl.
            proxy (Proxy): The proxy object to be used for the request.

        Returns:
            list or None: A list of results from the surface crawl, or None if the browser is not supported.

        Note:
            The returned list represents the search results obtained from the surface crawl.

        Example:
            >>> browser = Browser("google", research_url="https://www.google.com")
            >>> browser.perform_surface_crawl(instagram=True, facebook=True, twitter=True, linkedin=True, tiktok=True, firstname="John", lastname="Doe", alias="", keyword="", proxy=proxy)
            ['result1', 'result2', 'result3']
        """
        
        if self.name == "google":
            if lastname == "" or firstname == "":
                return []
            custom_url = "%22" + firstname + "+" + lastname + "%22"
            research_url = create_surface_crawl_url(self, instagram, facebook, twitter, linkedin, tiktok, custom_url)
            result_list = search_google(research_url, proxy)
            logger.debug("Google crawling result : {}", result_list)
            return result_list
        
        if self.name == "alias":
            if alias == "":
                alias = "%22" + lastname + "+" + firstname+ "%22"
            elif lastname != "" and firstname != "":
                alias = "(%22" + alias + "%22+OR+%22" + lastname + "+" + firstname + "%22)" # ("alias" OR "lastname firstname")
            else:
                alias = "%22" + alias + "%22"
            research_url = create_surface_crawl_url(self, instagram, facebook, twitter, linkedin, tiktok, alias)
            result_list = search_google(research_url, proxy)
            logger.debug("alias crawling result : {}", result_list)
            return result_list
        
        if self.name == "nicknames":
            # Nicknames
            matching_nicknames_list = match_nicknames(firstname)
            if matching_nicknames_list == []:
                return []
            nickname_query = create_query_matching_nicknames(firstname, lastname, matching_nicknames_list)
            research_url = create_surface_crawl_url(self, instagram, facebook, twitter, linkedin, tiktok, nickname_query, nickname_mode=True)
            
            logger.debug("Google crawling result for nicknames that match to {} : {}", firstname, research_url)
            result_list = search_google(research_url, proxy)
            return result_list

        if self.name == "duckduckgo":
            if lastname == "" or firstname == "":
                return []
            name = firstname + " " + lastname
            research_queries = create_surface_crawl_query(instagram, facebook, twitter, linkedin, tiktok, name)
            result_list = []
            for query in research_queries:
                print(query)
                result_list.extend(search_duckduckgo(query))
            logger.debug("Duckduckgo crawling result : {}", result_list)
            return result_list

        if self.name == "keyword":
            if lastname == "" or firstname == "" or keyword == "":
                return []
            custom_url = "%22" + firstname + "+" + lastname + "%22" + "+" + urllib.parse.quote_plus(keyword)
            research_url = create_surface_crawl_url(self, instagram, facebook, twitter, linkedin, tiktok, custom_url, nickname_mode=True)
            result_list = search_google(research_url, proxy)
            logger.debug("Keyword crawling result : {}", result_list)
            return result_list

        if self.name == "bing":
            if lastname == "" or firstname == "":
                return []
            result_list = []
            custom_url = "%22" + firstname + "+" + lastname + "%22"
            research_urls = create_surface_crawl_multiple_url(self, instagram, facebook, twitter, linkedin, tiktok, custom_url)
            for research_url in research_urls:
                result_list.extend(search_google(research_url, proxy))
            logger.debug("Bing crawling result : {}",result_list)
            return result_list

        return None

