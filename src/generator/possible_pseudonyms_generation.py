from src.utils.name import *
from src.utils.combination import generate_string_combinations
from src.generator.date_generation import get_possible_date_combination_with_delimiters
from src.generator.name_generation import get_possible_name_variations
from src.generator.nickname_generation import get_nicknames_variations_with_delimiters

delimiters = ['-', '_', '.', '']

def start_with_delimeters(name):
    return name[0] in ['-', '_', '.']


def generate_possible_pseudonyms(firstname, lastname, birthday, alias, limit = None, birthday_on=False, alias_only = False):
    """
    Generate all possible pseudonyms based on the given inputs.

    Args:
        firstname (str): The first name.

        lastname (str): The last name.

        birthday (str): The birthday.

        alias (str): The alias.

        limit (int, optional): The character limit for pseudonyms. Defaults to 13.

        birthday_on (bool, optional): Whether to include the birthday in pseudonyms. Defaults to False.

        alias_only (bool, optional): Whether  to generate only alias variation

    Returns:
        list: A list of generated pseudonyms.

    Example:
        >>> generate_possible_pseudonyms("Jean", "Pierre", "1970-01-01", "JP", limit=10, birthday_on=True)
        
        ['Jean.Pierre-1970', 'Pierre.Jean-1970', 'Jean-Pierre_1970', 'Pierre_Jean_1970', 'JP-1970', '1970-JP', 'JP.1970', '1970.JP'...]
    """
    min = 0 if limit == None else limit[0]
    max = 15 if limit == None else limit[1]

    pseudonyms = []
    if birthday_on:
        dates_combinations = get_possible_date_combination_with_delimiters(birthday, delimiters)

    if not alias_only:
        firstname_variations = get_possible_name_variations(firstname, delimiters)
        lastname_variations = get_possible_name_variations(lastname, delimiters)
        lastname_variations_with_delimiters = generate_string_combinations(delimiters, lastname_variations)

        for firstname in firstname_variations:
            for lastname in lastname_variations_with_delimiters:
                if birthday_on:
                    for date in dates_combinations:
                        pseudonym = firstname + lastname + date
                        if start_with_delimeters(lastname):
                            delimiter = lastname[0]
                            inversed_pseudonym = lastname[1:] + delimiter + firstname + date
                        else:
                            inversed_pseudonym = lastname + firstname + date
                        if min <= len(pseudonym) <= max:
                            pseudonyms.append(pseudonym)
                            pseudonyms.append(inversed_pseudonym)
                else:
                    pseudonym = firstname + lastname
                    delimiter = lastname[0]
                    if start_with_delimeters(lastname):
                        delimiter = lastname[0]
                        inversed_pseudonym = lastname[1:] + delimiter + firstname
                    else:
                        inversed_pseudonym = lastname + firstname

                    if min <= len(pseudonym) <= max:
                        pseudonyms.append(pseudonym)
                        pseudonyms.append(inversed_pseudonym)

    nicknames = get_nicknames_variations_with_delimiters(alias, delimiters)

    if nicknames != ['']:
        for n in nicknames:
            if birthday_on:
                for date in dates_combinations:
                    elt = n + date
                    if min <= len(elt) <= max:
                        pseudonyms.append(elt)
            else:
                if min <= len (elt) <= max:
                    pseudonyms.append(n)

    return pseudonyms
