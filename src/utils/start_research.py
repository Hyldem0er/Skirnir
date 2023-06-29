from src.generator.possible_pseudonyms_generation import generate_possible_pseudonyms
from src.surface_crawl.surface_crawl import surface_crawl
from src.scrapers.pseudo_finder_instagram import find_instagram_profile

def sort_crawl_result(crawl_results):
    """
    Sort and categorize crawl results based on social network.

    Args:
        crawl_results: A list of URLs obtained from crawling.
        advanced_profile_set: A dictionary containing categorized URLs for advanced profiles.

    Returns:
        An updated dictionary with categorized URLs for advanced profiles.
    """

    crawl_set = {}
    crawl_set["instagram"] = []
    crawl_set["facebook"] = []
    crawl_set["twitter"] = []
    crawl_set["linkedin"] = []
    
    for url in crawl_results:
        if "instagram" in url:
            crawl_set["instagram"].append(url)
        if "facebook" in url:
            crawl_set["facebook"].append(url)
        if "twitter" in url:
            crawl_set["twitter"].append(url)
        if "linkedin" in url:
            crawl_set["linkedin"].append(url)
    return crawl_set

def add_possible_profile(instagram_profiles):
    """
    Adds possible Facebook profiles based on the given Instagram profiles.

    Args:
        instagram_profiles (list): A list of Instagram profile URLs.

    Returns:
        list: A list of possible Facebook profile URLs.

    Example:
        >>> add_possible_profile(["https://www.instagram.com/user1/", "https://www.instagram.com/user2/"])
        ['https://www.facebook.com/user1/', 'https://www.facebook.com/user2/']
    """
    facebook_profiles = []
    for instagram_profile in instagram_profiles:
        facebook_profiles.append(instagram_profile.replace("https://www.instagram.com/", "https://www.facebook.com/"))
    return facebook_profiles

def create_social_networks_dict(instagram_checkbox, facebook_checkbox, twitter_checkbox, linkedin_checkbox):
    """
    Creates a dictionary representing the selected social network checkboxes.

    Args:
        instagram_checkbox (bool): The state of the Instagram checkbox.
        facebook_checkbox (bool): The state of the Facebook checkbox.
        twitter_checkbox (bool): The state of the Twitter checkbox.
        linkedin_checkbox (bool): The state of the LinkedIn checkbox.

    Returns:
        dict: A dictionary representing the selected social network checkboxes.

    Example:
        >>> create_social_networks_dict(True, False, True, False)
        {'instagram': True, 'facebook': False, 'twitter': True, 'linkedin': False}
    """
    return {
        "instagram": instagram_checkbox,
        "facebook": facebook_checkbox,
        "twitter": twitter_checkbox,
        "linkedin": linkedin_checkbox
    }


def start_profile_research(instagram_checkbox, facebook_checkbox, twitter_checkbox, linkedin_checkbox,
                           firstname, lastname, date, nickname, birthday_on, nickname_only, limit, crawl_is_checked):
    """
    Starts the profile research process based on the provided parameters.

    Args:
        instagram_checkbox (bool): The state of the Instagram checkbox.
        facebook_checkbox (bool): The state of the Facebook checkbox.
        twitter_checkbox (bool): The state of the Twitter checkbox.
        linkedin_checkbox (bool): The state of the LinkedIn checkbox.
        firstname (str): The firstname.
        lastname (str): The lastname.
        date (str): The date.
        nickname (str): The nickname.
        birthday_on (str): The birthday option.
        nickname_only (bool): The state of the "Nickname Only" checkbox.
        limit (int): The limit for generating possible pseudonyms.
        crawl_is_checked (bool): The state of the "Crawl" checkbox.

    Returns:
        tuple: A tuple containing the crawl list, advanced profile set, and social networks dictionary.

    Example:
        >>> start_profile_research(True, False, True, False, "John", "Doe", "2023-06-28", "johndoe", "No", False, 10, True)
        (['https://www.example.com', 'https://www.example2.com'], {'instagram': ['https://www.instagram.com/user1/']}, {'instagram': True, 'facebook': False, 'twitter': True, 'linkedin': False})
    """
    social_networks_dict = create_social_networks_dict(instagram_checkbox, facebook_checkbox, twitter_checkbox, linkedin_checkbox)

    name = nickname
    if not nickname_only:
        name = firstname + " " + lastname

    crawl_list = surface_crawl(instagram_checkbox, facebook_checkbox, twitter_checkbox, linkedin_checkbox, name, lastname)

    generated_nicknames = generate_possible_pseudonyms(firstname, lastname, date, nickname, limit, birthday_on, nickname_only)

    advanced_profile_set = {}

    if not crawl_is_checked:
        instagram_profiles = find_instagram_profile(generated_nicknames)
        if instagram_checkbox:
            advanced_profile_set["instagram"] = instagram_profiles

        if facebook_checkbox:
            advanced_profile_set["facebook"] = add_possible_profile(instagram_profiles)

        if twitter_checkbox:
            advanced_profile_set["twitter"] = []
            # TODO

        if linkedin_checkbox:
            advanced_profile_set["linkedin"] = []
            # TODO

    return crawl_list, advanced_profile_set, social_networks_dict
