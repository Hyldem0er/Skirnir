from src.utils.name import *
from unidecode import unidecode
from src.generator.nickname_generation import get_nicknames_variations_with_delimiters


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
    if nickname in url and nickname != '':
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

def print_score(set, firstname, lastname, nickname, list_nickname):
    for url in set:
        print(url," :" , similarity_score(unidecode(url.lower()), firstname.lower(), lastname.lower(), nickname.lower(), list_nickname))

def sort_by_relevance(iterable, firstname, lastname, nickname, list_nickname):
    return sorted(iterable, key=lambda url: similarity_score(unidecode(url.lower()), firstname.lower(), lastname.lower(), nickname.lower(), list_nickname), reverse=True)