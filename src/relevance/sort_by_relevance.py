from src.utils.name import *
from unidecode import unidecode
from src.generator.nickname_generation import get_nicknames_variations_with_delimiters
from Levenshtein import jaro_winkler as jar

def composed_name_test_in_url(name, url):
    """
    Checks if a composed name with delimiters is present in a given URL.

    Args:
        name (str): The composed name to check for in the URL.
        url (str): The URL to search for the composed name.

    Returns:
        bool: True if the composed name is found in the URL, False otherwise.
    """
    delimiters = ['-', '_', '.', '']
    names = get_nicknames_variations_with_delimiters(name, delimiters)
    for n in names:
        if n in url:
            return True
    return False

def similarity_score(url, firstname, lastname, alias, list_nickname):
    """
    Calculates a similarity score between a URL and provided personal information.

    Args:
        url (str): The URL to compare.
        firstname (str): The first name of the individual.
        lastname (str): The last name of the individual.
        alias (str): An alias used by the individual.
        list_nickname (list): A list of nicknames associated with the individual.

    Returns:
        int: The similarity score between the URL and the provided personal information.

    Notes:
        The similarity score is calculated based on the presence of the individual's first name,
        last name, alias, and nicknames in the URL, as well as variations of these names.
    """
    if url == "":
        return 0
    if "linkedin" in url:
        url = url.split("/")[4]
    else:
        url = url.split("/")[3]


    firstname_in_url = True if firstname in url else False
    first_char_firstname_in_url = True if first_char(firstname) in url else False
    lastname_in_url = True if lastname in url else False
    first_char_lastname_in_url = True if first_char(lastname) in url else False
    rem_vowel_firstname_in_url = True if rem_vowel(firstname) in url else False
    rem_vowel_lastname_in_url = True if rem_vowel(lastname) in url else False
    nickname_in_url = True if (firstname[0].upper() + firstname[1:]) in list_nickname else False

    # Composed Firstname
    if '-' in firstname or '_' in firstname or '.' in firstname or ' ' in firstname:
        firstname_in_url = composed_name_test_in_url(firstname, url)
        first_char_firstname_in_url = composed_name_test_in_url(first_char(firstname), url)
        rem_vowel_firstname_in_url = composed_name_test_in_url(rem_vowel(firstname), url)

    # Composed Lastname
    if '-' in lastname or '_' in lastname or '.' in lastname or ' ' in lastname:
        lastname_in_url = composed_name_test_in_url(lastname, url)
        first_char_lastname_in_url = composed_name_test_in_url(lastname, url)
        rem_vowel_lastname_in_url = composed_name_test_in_url(rem_vowel(lastname), url)

    if firstname_in_url and lastname_in_url:
        return 100
    if rem_vowel_firstname_in_url and lastname_in_url:
        return 90
    if nickname_in_url and lastname_in_url:
        return 80
    if first_char_firstname_in_url and lastname_in_url:
        return 70
    if firstname_in_url and rem_vowel_lastname_in_url:
        return 60
    if alias in url and not alias == "":
        return 55
    if firstname_in_url and first_char_lastname_in_url:
        return 50
    if nickname_in_url and rem_vowel_lastname_in_url:
        return 40
    if nickname_in_url and first_char_lastname_in_url:
        return 30
    if rem_vowel_lastname_in_url and rem_vowel_firstname_in_url:
        return 20
    if first_char_firstname_in_url and first_char_lastname_in_url:
        return 10
    if lastname_in_url:
        return 5
    return 0

def similarity_score_nickname_only(url, alias):
    """
    Calculates a similarity score between a URL and an alias (nickname).

    Args:
        url (str): The URL to compare.
        alias (str): The alias (nickname) to compare against.

    Returns:
        int: The similarity score between the URL and the alias.

    Notes:
        The similarity score is calculated based on the Jaro-Winkler similarity between
        the URL and the alias, multiplied by 100. If the score is below or equal to 75 and
        the alias is present in the URL, a score of 75 is returned.
    """
    if url == "":
        return 0
    if "linkedin" in url:
        url = url.split("/")[4]
    else:
        url = url.split("/")[3]
    score = jar(url, alias) * 100
    if score <= 75  and alias in url:
        return 75
    return score


def print_score(set, firstname, lastname, alias, list_nickname, alias_only=False):
    """
    Print the similarity score for a set of URLs.

    Args:
        urls (set): A set of URLs to calculate similarity scores for.
        firstname (str): The first name of the person associated with the URLs.
        lastname (str): The last name of the person associated with the URLs.
        alias (str): The alias (nickname) of the person associated with the URLs.
        list_nickname (list): A list of nicknames associated with the person.
        alias_only (bool, optional): If True, only calculates the similarity score based on the alias.
                                     Defaults to False.

    Returns:
        None

    Notes:
        This function calculates the similarity score between each URL in the set and the
        provided first name, last name, alias, and list of nicknames. It then prints the URL
        along with its corresponding similarity score.
    """
    for url in set:
        if alias_only:
            print(url," :" , similarity_score_nickname_only(unidecode(url.lower()), alias.lower()))
        else:
            print(url," :" , similarity_score(unidecode(url.lower()), firstname.lower(), lastname.lower(), alias.lower(), list_nickname))

def sort_by_relevance(iterable, firstname, lastname, alias, list_nickname, alias_only=False):
    """
    Sorts an iterable of URLs by relevance based on similarity scores.

    Args:
        iterable (iterable): An iterable containing URLs to sort.
        firstname (str): The first name of the person associated with the URLs.
        lastname (str): The last name of the person associated with the URLs.
        alias (str): The alias (nickname) of the person associated with the URLs.
        list_nickname (list): A list of nicknames associated with the person.
        alias_only (bool, optional): If True, sort only based on the alias.
                                     Defaults to False.

    Returns:
        list: A list of URLs sorted by relevance.

    Notes:
        This function calculates the similarity score between each URL in the iterable and the
        provided first name, last name, alias, and list of nicknames. It then sorts the URLs
        based on these similarity scores in descending order and returns the sorted list.
    """
    if alias_only:
        return sorted(iterable, key=lambda url: similarity_score_nickname_only(unidecode(url.lower()), alias.lower()), reverse=True)
    else:
        return sorted(iterable, key=lambda url: similarity_score(unidecode(url.lower()), firstname.lower(), lastname.lower(), alias.lower(), list_nickname), reverse=True)
