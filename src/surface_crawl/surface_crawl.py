
from src.utils.similarity import is_similar
from src.utils.format_url import format_url
from src.surface_crawl.Browser import Browser
import re
import requests
from src.surface_crawl.match_nicknames import create_query_matching_nicknames

def is_not_noise_url(url):
    return ("/directory/" not in url and "/posts/" not in url and "/photos/" not in url and "/videos/" not in url and "/story/" not in url and "/media/" not in url and "/groups/" not in url and "/status/" not in url and "/dir/" not in url and "/pulse/" not in url and "/company/" not in url and "/events/" not in url and "/hashtag/" not in url and "/p/" not in url and "/public/" not in url and "/search/" not in url and "/filter/" not in url  and "/jobs/" not in url and "/explore/" not in url and "/pages/" not in url)

def extract_profile_url(url):
    """
    Extracts the profile URL from a given URL based on predefined social media sites.

    Args:
        url (str): The URL to extract the profile URL from.

    Returns:
        str or None: The extracted profile URL, or None if not a correct profile url.
    """
    social_media_sites = ["www.instagram.com", "m.facebook.com", "www.facebook.com", "twitter.com", "fr.linkedin.com"]
    for site in social_media_sites:
        url = requests.utils.unquote(url)
        if re.match("^https://" + site + "/[a-zA-Z]", url):
            if "profile.php" in url: # Facebook profile with id
                return url
            else:
                if "/directory/" not in url and "/videos/" not in url and "/photo/" not in url: # exclude LinkedIn directory and Facebook videos
                    return url.split('?')[0]
    return None

def surface_crawl(instagram, facebook, twitter, linkedin, name, firstname, lastname):
    """
    Performs surface crawling based on the provided parameters.

    Args:
        instagram (bool): Whether Instagram should be included in the search.
        facebook (bool): Whether Facebook should be included in the search.
        twitter (bool): Whether Twitter should be included in the search.
        linkedin (bool): Whether LinkedIn should be included in the search.
        firstname (str): First name for the search query.
        lastname (str): Last name for the search query.

    Returns:
        list: A list of profile URLs found during surface crawling
    """
    urls = []
    browsers = [Browser("google", "https://www.google.com/search?client=firefox-b-d&q="), Browser("duckduckgo")] #  Browser("bing", "https://www.bing.com/search?q=")
    
    # Name
    for browser in browsers:
        temp = browser.perform_surface_crawl(instagram, facebook, twitter, linkedin, name)
        urls.extend(temp)

    # Mathing Nicknames
    urls.extend(browsers[0].perform_surface_crawl(instagram, facebook, twitter, linkedin, create_query_matching_nicknames(firstname, lastname)))

    profile_urls = []
    for url in urls:
        tmp = extract_profile_url(url)
        if tmp is not None and is_not_noise_url(url):
            if tmp[len(tmp) - 1] != '/':
                tmp += '/'
            if "linkedin.com/in/" in tmp and not is_similar(tmp, lastname): # Eliminate wrong linkedIn profile
                continue
            profile_urls.append(format_url(tmp))
    
    return list(set(profile_urls))
