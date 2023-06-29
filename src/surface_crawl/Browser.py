from src.surface_crawl.create_url_or_query import *

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

    def perform_surface_crawl(self, instagram, facebook, twitter, linkedin, name):
        """
        Performs a surface crawl on specified platforms using the browser.

        Args:
            instagram (bool): Flag indicating whether to perform a surface crawl on Instagram.
            facebook (bool): Flag indicating whether to perform a surface crawl on Facebook.
            twitter (bool): Flag indicating whether to perform a surface crawl on Twitter.
            linkedin (bool): Flag indicating whether to perform a surface crawl on LinkedIn.
            name (str): The name to use for the surface crawl.

        Returns:
            list or None: A list of results from the surface crawl, or None if the browser is not supported.

        Note:
            The returned list represents the search results obtained from the surface crawl.

        Example:
            >>> browser = Browser("google", research_url="https://www.google.com")
            >>> browser.perform_surface_crawl(instagram=True, facebook=True, twitter=True, linkedin=True, name="JohnDoe")
            ['result1', 'result2', 'result3']
        """
        if self.name == "google":
            research_url = create_surface_crawl_url(self, instagram, facebook, twitter, linkedin, name)
            result_list = search_google(research_url)
            return result_list

        if self.name == "duckduckgo":
            research_queries = create_surface_crawl_query(instagram, facebook, twitter, linkedin, name)
            result_list = []
            for query in research_queries:
                result_list.extend(search_duckduckgo(query))
            return result_list

        if self.name == "bing":
            result_list = []
            research_urls = create_surface_crawl_multiple_url(self, instagram, facebook, twitter, linkedin, name)
            for research_url in research_urls:
                result_list.extend(search_google(research_url))
            return result_list

        return None

