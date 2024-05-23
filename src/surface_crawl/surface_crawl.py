
from src.utils.similarity import is_similar
from src.utils.format_url import format_url
from src.surface_crawl.Browser import Browser
import re
import requests

def is_not_noise_url(url):
    """
    Checks if the given URL is not a noise URL.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL is not a noise URL, False otherwise.
    """
    return ("/directory/" not in url and "/posts/" not in url and "/photos/" not in url and "/videos/" not in url
            and "/story/" not in url and "/media/" not in url and "/groups/" not in url and "/status/" not in url
            and "/dir/" not in url and "/pulse/" not in url and "/company/" not in url and "/events/" not in url
            and "/hashtag/" not in url and "/p/" not in url and "/public/" not in url and "/search/" not in url
            and "/filter/" not in url  and "/jobs/" not in url and "/explore/" not in url and "/pages/" not in url
            and "/reel/" not in url  and "/review/" not in url and "/legacy/" not in url and "/notes/" not in url
            and "/tv/" not in url and "google" not in url and "translate" not in url and "/about-us/" not in url 
            and "/marketing-solutions/" not in url and "/help/" not in url and "/live/" not in url and "/login/" not in url 
            and "/using-x/" not in url and "/docs/" not in url and "/forms/" not in url and "/login.php/" not in url 
            and "facebook.com/reg/" not in url and "/getting-started/" not in url and "/marketplace/" not in url 
            and "/features/" not in url and "/about/" not in url and "/linkedin-news/" not in url and "/blog/" not in url 
            and "/grow/" not in url and "/who-we-are/" not in url and "/content/" not in url and "/web/" not in url and "/home/"
            and "/feed/" not in url and "/discover/" not in url and "/tags/" not in url and "/video/" not in url and "/album" not in url
            and ".php/")


def extract_profile_url(url):
    """
    Extracts the profile URL from a given URL based on predefined social media sites.

    Args:
        url (str): The URL to extract the profile URL from.

    Returns:
        str or None: The extracted profile URL, or None if not a correct profile url.
    """
    social_media_sites = ["instagram.com", "facebook.com", "twitter.com", "linkedin.com", "x.com", "tiktok.com"]
    for site in social_media_sites:
        url = requests.utils.unquote(url)
        if re.match("^https://.*" + site + "/[A-Za-zÀ-ÖØ-öø-ÿ_\-\.@]", url):
            url = re.sub('[a-z]*-?[a-z]*\.' + site , "" + site, url, 1)
            if "profile.php" in url: # Facebook profile with id
                return url
            else:
                if "/directory/" not in url and "/videos/" not in url and "/photo/" not in url: # exclude LinkedIn directory and Facebook videos
                    return url.split('?')[0]
    return None

def surface_crawl(instagram, facebook, twitter, linkedin, tiktok, firstname, lastname, alias, keyword, proxy):
    """
    Performs surface crawling based on the provided parameters.

    Args:
        instagram (bool): Whether Instagram should be included in the search.
        facebook (bool): Whether Facebook should be included in the search.
        twitter (bool): Whether Twitter should be included in the search.
        linkedin (bool): Whether LinkedIn should be included in the search.
        firstname (str): First name for the search query.
        lastname (str): Last name for the search query.
        keyword (str): The keyword to crawl
        proxy (Proxy): Proxy

    Returns:
        list: A list of profile URLs found during surface crawling
    """
    urls = []
    browsers = [Browser("google", "https://www.google.com/search?client=firefox-b-d&q="), Browser("alias", "https://www.google.com/search?client=firefox-b-d&q="),
                Browser("nicknames", "https://www.google.com/search?client=firefox-b-d&q="), Browser("keyword", "https://www.google.com/search?client=firefox-b-d&q=") , Browser("duckduckgo")] #, Browser("bing", "https://www.bing.com/search?q=")]
    # browsers = [Browser("duckduckgo")] #  Browser("bing", "https://www.bing.com/search?q=")
    
    # Name
    for browser in browsers:
        temp = browser.perform_surface_crawl(instagram, facebook, twitter, linkedin, tiktok, firstname, lastname, alias, keyword, proxy)
        urls.extend(temp)

    profile_urls = []
    for url in urls:
        tmp = extract_profile_url(url)
        if tmp is not None and is_not_noise_url(url):
            if tmp[len(tmp) - 1] != '/':
                tmp += '/'
            if "linkedin.com/in/" in tmp and not is_similar(tmp, lastname): # Eliminate wrong linkedIn profile
                # print(tmp)
                continue
            profile_urls.append(format_url(tmp))
    
    return list(set(profile_urls))
