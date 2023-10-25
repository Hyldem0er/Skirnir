from duckduckgo_search import DDGS
from bs4 import BeautifulSoup
from time import sleep
from src.request_helper.request_handling import get
import sys
from loguru import logger

logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")

def calculate_number_activate_networks(instagram, facebook, twitter, linkedin):
        """
        Calculate the number of activated social media networks based on the provided parameters.

        Args:
            instagram (bool): Whether Instagram is activated.
            facebook (bool): Whether Facebook is activated.
            twitter (bool): Whether Twitter is activated.
            linkedin (bool): Whether LinkedIn is activated.

        Returns:
            int: The number of activated social media networks.
        """
        activated_networks = sum([instagram, facebook, twitter, linkedin])
        return activated_networks
    
def create_surface_crawl_url(browser, instagram, facebook, twitter, linkedin, url_q, nickname_mode = False):
    """
    Generate a Browser search URL for surface crawling based on provided parameters.
    
    Args:
        instagram (bool): Whether Instagram should be included in the search.
        facebook (bool): Whether Facebook should be included in the search.
        twitter (bool): Whether Twitter should be included in the search.
        linkedin (bool): Whether LinkedIn should be included in the search.
        name (str): First name + Lastname for the search query.
    
    Returns:
        list : A list of the generated Google search URL for Google and Duckduckgo.
    """
    url = browser.research_urls + url_q

    
    # Calculate the limit of activated networks
    limit = calculate_number_activate_networks(instagram, facebook, twitter, linkedin)

    # Variable to keep track of remaining OR conditions
    or_limit = limit

    # Dictionary of social media sites and their corresponding search parameters
    social_media_sites = {
        'facebook': 'site%3Afacebook.com',
        'instagram': 'site%3Ainstagram.com',
        'twitter': 'site%3Atwitter.com',
        'linkedin': 'site%3Alinkedin.com'
    }

    # Iterate through each social media site and add it to the URL if needed
    for site, search_parameter in social_media_sites.items():
        if or_limit == 0:
            break
        
        # Check if the social media site should be included
        if locals()[site]:
            or_limit -= 1
            url += "+{}{}".format(search_parameter, "+OR" if or_limit != 0 else "")

    if not nickname_mode:
        # Remove noise posts, photos, and videos
        url += "+-inurl%3A%2Fposts%2F+-inurl%3A%2Fphotos%2F+-inurl%3A%2Fvideos%2F+-inurl%3A%2Fstory%2F+-inurl%3A%2Fmedia%2F+-inurl%3A%2Fgroups%2F+-inurl%3A%2Fstatus%2F+-inurl%3A%2Fdir%2F+-inurl%3A%2Fpulse%2F+-inurl%3A%2Fcompany%2F+-inurl%3A%2Fevents%2F+-inurl%3A%2Fhashtag%2F+-inurl%3A%2Fp%2F+-inurl%3A%2Fpublic%2F+-inurl%3A%2Fsearch%2F+-inurl%3A%2Fjobs%2F+-inurl%3A%2Fpages%2F+-inurl%3A%2Fexplore%2F+-inurl%3A.php&filter=0"

    if browser.name == "google" and not nickname_mode:
        # Add the 'num' parameter based on the limit of activated networks
        url += "&num=" + str(limit * 25)
    
    return url

def create_surface_crawl_multiple_url(browser, instagram, facebook, twitter, linkedin, name):
    """
    Generate a Browser search URL list for surface crawling based on provided parameters.
    
    Args:
        instagram (bool): Whether Instagram should be included in the search.
        facebook (bool): Whether Facebook should be included in the search.
        twitter (bool): Whether Twitter should be included in the search.
        linkedin (bool): Whether LinkedIn should be included in the search.
        name (str): First name + Lastname for the search query.
    
    Returns:
        str: The generated Bing search URL.
    """
    urls = []

    # Base URL with the provided first and last name
    url = browser.research_urls + "%22" + name + "%22"

    # Calculate the limit of activated networks
    limit = calculate_number_activate_networks(instagram, facebook, twitter, linkedin)

    # Variable to keep track of remaining OR conditions
    or_limit = limit


    # Dictionary of social media sites and their corresponding search parameters
    social_media_sites = {
        'facebook': 'site%3Afacebook.com',
        'instagram': 'site%3Ainstagram.com',
        'twitter': 'site%3Atwitter.com',
        'linkedin': 'site%3Alinkedin.com'
    }

    # Iterate through each social media site and add it to the URL if needed
    for site, search_parameter in social_media_sites.items():

        # Check if the social media site should be included
        if locals()[site]:
            or_limit -= 1
            temp = url + "%20" + search_parameter
            urls.append(temp)

    return urls


def create_surface_crawl_query(instagram, facebook, twitter, linkedin, name):
        """
        Generate a Google search query for surface crawling based on provided parameters.
        
        Args:
            instagram (bool): Whether Instagram should be included in the search.
            facebook (bool): Whether Facebook should be included in the search.
            twitter (bool): Whether Twitter should be included in the search.
            linkedin (bool): Whether LinkedIn should be included in the search.
            name (str): First name + Lastname for the search query.
        
        Returns:
            str: The generated Google search URL.
        """

        queries = []

        # Base URL with the provided first and last name
        query = "\"" + name + "\""
        
        # Calculate the limit of activated networks
        limit = calculate_number_activate_networks(instagram, facebook, twitter, linkedin)

        # Variable to keep track of remaining OR conditions
        or_limit = limit

        # Dictionary of social media sites and their corresponding search parameters
        social_media_sites = {
            'facebook': 'site:facebook.com',
            'instagram': 'site:instagram.com',
            'twitter': 'site:twitter.com',
            'linkedin': 'site:linkedin.com'
        }

        # Iterate through each social media site and add it to the URL if needed
        for site, search_parameter in social_media_sites.items():
            # Check if the social media site should be included
            if locals()[site]:
                or_limit -= 1
                temp = query + " " + search_parameter
                queries.append(temp)

        return queries

def search_google(research_url, sleep_interval=5):
    """
    Performs a Google search and retrieves the links from the search results.

    Args:
        research_url (str): The URL to perform the Google search.
        sleep_interval (float, optional): The sleep interval in seconds between requests. Defaults to 1.

    Returns:
        list: A list of unique links extracted from the search results.

    Example:
        >>> search_google("https://www.google.com/search?q=example")
        ['https://www.example.com', 'https://www.example2.com']
    """
    try:
        resp = get(research_url)
        links = []
        soup = BeautifulSoup(resp.content, "html.parser")
        for link in soup.findAll('a'):
            if 'href' in link.attrs:
                links.append(link.get("href"))
        sleep(sleep_interval)
        return list(set(links))
    except Exception as e:
        logger.exception(e)
        return []

def search_duckduckgo(query, sleep_interval=1):
    """
    Performs a DuckDuckGo search and retrieves the links from the search results.

    Args:
        query (str): The query to search on DuckDuckGo.
        sleep_interval (float, optional): The sleep interval in seconds between requests. Defaults to 1.

    Returns:
        list: A list of unique links extracted from the search results.

    Example:
        >>> search_duckduckgo("example query")
        ['https://www.example.com', 'https://www.example2.com']
    """
    links = []
    try:
        with DDGS() as ddgs:
            for r in ddgs.text(query, region='wt-wt', safesearch='off'):
                links.append(r['href'])

        sleep(sleep_interval)
        return list(set(links))
    except Exception as e:
        logger.exception(e)
        return links
