from src.utils.name import *
from unidecode import unidecode
# database_path = os.path.abspath(os.path.join(os.path.dirname(__file__), './', 'database.txt'))


# # Using readlines()
# file1 = open(database_path, 'r')
# Lines = file1.readlines()


# myset = set()
# count = 0
# # Strips the newline character
# for line in Lines:
#     count += 1
#     myset.add(line.strip())





def similarity_score(url, firstname, lastname, list_nickname):
    if url == "":
        return 0

    firstname_in_url = True if firstname in url else False
    lastname_in_url = True if lastname in url else False
    first_char_firstname_in_url = True if first_char(firstname) in url else False
    first_char_lastname_in_url = True if first_char(lastname) in url else False
    rem_vowel_firstname_in_url = True if rem_vowel(firstname) in url else False
    rem_vowel_lastname_in_url = True if rem_vowel(lastname) in url else False
    nickname_in_url = True if (firstname[0].upper() + firstname[1:]) in list_nickname else False

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

def print_score(set, firstname, lastname, list_nickname):
    for url in set:
        print(url," :" , similarity_score(url, firstname, lastname, list_nickname))

def sort_by_relevance(set, firstname, lastname, list_nickname):
    return sorted(set, key=lambda url: similarity_score(unidecode(url.lower()), firstname.lower(), lastname.lower(), list_nickname), reverse=True)


# list_nickname = list_nicknames()
# print_score(myset, "jean", "deriaux", list_nickname)

# print(sort_by_relevance(myset, "jean", "deriaux", list_nickname))