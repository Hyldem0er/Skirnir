# from src.utils.name import *
from unidecode import unidecode
# from src.generator.nickname_generation import get_nicknames_variations_with_delimiters
import os
from Levenshtein import jaro_winkler as jar

database_path = os.path.abspath(os.path.join(os.path.dirname(__file__), './', 'database.txt'))

vowels = ['a','e','i','o','u','y', 'A', 'E', 'I', 'O', 'U', 'Y']

def first_char(string):
    """
    Get the first character of a given string.

    Args:
        string (str): The input string.

    Returns:
        str: The first character of the input string.

    Example:
        >>> first_char("Pierre")
        'P'
    """
    delimiters = ['-', '_', '.']

    for d in delimiters:
        if d in string:
            string = string.replace(d, ' ')
    x = string.split()
    try:
        return x[0][0] + x[1][0]
    except:
        return string[0]


def rem_vowel(string):
    """
    Remove vowels from a given string.

    Args:
        string (str): The input string.

    Returns:
        str: The input string with vowels removed.

    Example:
        >>> rem_vowel("Pierre")
        'Prr'
    """
    result = [letter for letter in string if letter.lower() not in vowels]
    result = ''.join(result)
    return result

def get_nicknames_variations_with_delimiters(nickname, delimiters):
    """
    Generate all variations of a nickname with different delimiters.

    Args:
        nickname (str): The input nickname.
        delimiters (list): A list of delimiters used to generate variations.

    Returns:
        list: A list of nickname variations.

Example:
    >>> get_nicknames_variations_with_delimiters("cassos du 76", [".", "-", "_"])
    ["cassos du 76", "cassos.du.76", "cassos-du-76", "cassos_du_76", "cassos du 76", "cassos.du.76", "cassos-du-76", "cassos_du_76"]
"""


    delimiters.append(" ")
    nicknames_variation = [nickname]
    for d in delimiters:
        if d in nickname and d != '':
            for deli in delimiters:
                if d != deli:
                    nicknames_variation.append(nickname.replace(d, deli))
    return nicknames_variation



# Using readlines()
file1 = open(database_path, 'r')
Lines = file1.readlines()


myset = set()
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    myset.add(line.strip())



def composed_name_test_in_url(name, url):
    delimiters = ['-', '_', '.', '']
    names = get_nicknames_variations_with_delimiters(name, delimiters)
    for n in names:
        if n in url:
            return True
    return False

def similarity_score(url, firstname, lastname, nickname, list_nickname):
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
    if nickname in url and not nickname == "":
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

def similarity_score_nickname_only(url, nickname):
    if url == "":
        return 0
    if "linkedin" in url:
        url = url.split("/")[4]
    else:
        url = url.split("/")[3]
    score = jar(url, nickname) * 100
    if score <= 75  and nickname in url:
        return 75
    return score


def print_score(set, firstname, lastname, nickname, list_nickname, nickname_only=False):
    for url in set:
        if nickname_only:
            print(url," :" , similarity_score_nickname_only(unidecode(url.lower()), nickname.lower()))
        else:
            print(url," :" , similarity_score(unidecode(url.lower()), firstname.lower(), lastname.lower(), nickname.lower(), list_nickname))

def sort_by_relevance(iterable, firstname, lastname, nickname, list_nickname, nickname_only=False):
    if nickname_only:
        return sorted(iterable, key=lambda url: similarity_score_nickname_only(unidecode(url.lower()), nickname.lower()), reverse=True)
    else:
        return sorted(iterable, key=lambda url: similarity_score(unidecode(url.lower()), firstname.lower(), lastname.lower(), nickname.lower(), list_nickname), reverse=True)


# print_score(myset, "Jean", "Deriaux", "djo", [], True)


res = sort_by_relevance(myset, "Jean", "Deriaux", "le vieux rat 88", [], True)
for url in res:
    print(url)