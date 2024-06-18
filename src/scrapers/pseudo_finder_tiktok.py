from src.request_helper.request_handling import get
import requests
from random import shuffle
import os, sys
from loguru import logger

logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")

def create_tiktok_link(rebound_site, nickname):
    """
    Create an TikTok profile link based on the given nickname.

    Args:
        nickname (str): The TikTok nickname.

    Returns:
        str: The TikTok profile link.

    Example:
        >>> create_TikTok_link("jean_pierre")
        'https://www.picnob.com/fr/profile/jean_pierre/'
    """
    return rebound_site + "@" + nickname + '/'

# Setting user-agent to emulate human connection, request to picnob, return True if status code = 200
import requests

def is_tiktok_profile(link, proxy):
    """
    Checks if the provided link corresponds to an existing TikTok profile.

    Args:
        link (str): The link to check.
        proxy (Proxy): The proxy object to be used for the request.

    Returns:
        bool: True if the link corresponds to an existing TikTok profile, False otherwise.

    Raises:
        Exception: If an unexpected error occurs during the request.

    Example:
        >>> is_tiktok_profile("https://www.TikTok.com/example_profile/", proxy)
        True
    """
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 
        'Accept-Language': 'en-US,en;q=0.5'
    }
    try:
        response = get(link, proxy, header=header, timeout=20.0)
        if response.status_code == 200:
            return True
        return False
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code
        if status_code == 404:
            return False
    except Exception as e:
        raise Exception(e)


def find_tiktok_profile(nicknameList, proxy):
    """
    Searches for TikTok profiles corresponding to the provided nicknames.

    Args:
        nicknameList (list): A list of nicknames to search for.
        proxy (Proxy): The proxy object to be used for the request.

    Returns:
        list: A list of existing TikTok profile links.

    Example:
        >>> find_tiktok_profile(["nickname1", "nickname2", "nickname3"], proxy)
        ['https://www.tiktok.com/@nickname1', 'https://www.tiktok.com/@nickname2']
    """
    logger.info("Searching for TikTok profile")

    # Keep this list update
    rebound_sites = [
       # "https://www.tiktokstalk.com/user/"
    ]

    existing_profile_list = []

    for nickname in nicknameList:
        shuffle(rebound_sites)

        for rebound_site in rebound_sites:
            try:
                logger.info("Searching {}", nickname)
                igLink = create_tiktok_link(rebound_site, nickname)
                logger.info(igLink)

                if is_tiktok_profile(igLink, proxy):
                    var = "https://www.tiktok.com/@" + nickname
                    existing_profile_list.append(var)
                    logger.info("Found! {}", var)
                break

            except Exception as e:
                logger.exception(e)

    return existing_profile_list


