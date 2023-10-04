from src.request_helper.request_handling import get
import requests
from random import shuffle
import os, sys
from loguru import logger

logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")

def create_instagram_link(rebound_site, nickname):
    """
    Create an Instagram profile link based on the given nickname.

    Args:
        nickname (str): The Instagram nickname.

    Returns:
        str: The Instagram profile link.

    Example:
        >>> create_instagram_link("jean_pierre")
        'https://www.picnob.com/fr/profile/jean_pierre/'
    """
    return rebound_site + nickname + '/'

# Setting user-agent to emulate human connection, request to picnob, return True if status code = 200
import requests

def is_instagram_profile(link):
    """
    Checks if the provided link corresponds to an existing Instagram profile.

    Args:
        link (str): The link to check.

    Returns:
        bool: True if the link corresponds to an existing Instagram profile, False otherwise.

    Raises:
        Exception: If an unexpected error occurs during the request.

    Example:
        >>> is_instagram_profile("https://www.instagram.com/example_profile/")
        True
    """
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 
        'Accept-Language': 'en-US,en;q=0.5'
    }
    try:
        response = get(link, header=header, timeout=1.0)
        if response.status_code == 200:
            return True
        return False
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code
        if status_code == 404:
            return False
    except Exception as e:
        raise Exception(e)


def find_instagram_profile(nicknameList):
    """
    Searches for Instagram profiles corresponding to the provided nicknames.

    Args:
        nicknameList (list): A list of nicknames to search for.

    Returns:
        list: A list of existing Instagram profile links.

    Example:
        >>> find_instagram_profile(["nickname1", "nickname2", "nickname3"])
        ['https://www.instagram.com/nickname1/', 'https://www.instagram.com/nickname2/']
    """
    logger.info("Searching for IG profile")

    # Keep this list update
    rebound_sites = [
        "https://www.picnob.com/fr/profile/",
        "https://imginn.com/",
        "https://storiesig.me/info?username=",
        "https://instastories.watch/info?username=",
        "https://dumpoir.com/v/",
        "https://picuki.com/profile/",
        "https://greatfon.com/v/"
    ]

    existing_profile_list = []

    for nickname in nicknameList:
        shuffle(rebound_sites)

        for rebound_site in rebound_sites:
            # os.system('cls' if os.name == 'nt' else 'clear')
            try:
                logger.info("Searching {}", nickname)
                igLink = create_instagram_link(rebound_site, nickname)
                logger.info(igLink)

                if is_instagram_profile(igLink):
                    var = "https://www.instagram.com/" + nickname + "/"
                    existing_profile_list.append(var)
                    logger.info("Found! {}", var)
                break

            except Exception as e:
                logger.exception(e)

    return existing_profile_list