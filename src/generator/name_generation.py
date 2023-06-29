from src.utils.name import *
from src.utils.combination import generate_string_combinations

def get_possible_simple_name_variations(name):
    """
    Get possible variations of a simple name.

    Args:
        name (str): The input name.

    Returns:
        list: A list of possible name variations.

    Example:
        >>> get_possible_simple_name_variations("Pierre")
        ["P", "Pierre", "Prr"]
    """
    name_variations = []
    name_variations.append(first_char(name))
    name_variations.append(name)
    if first_char(name) not in vowels:
        name_variations.append(rem_vowel(name))
    return list(set(name_variations))

def get_possible_composed_name_variations(composed_name, delimiters):
    """
    Get possible variations of a composed name.

    Args:
        composed_name (list): A list containing a composed name.
        delimiters (list): A list of characters used as delimiters between the first name and last name.

    Returns:
        list: A list of possible name variations.

    Example:
        >>> get_possible_composed_name_variations(["Jean", "Pierre"], ["", ".", "-"])
        ["JP", "J.P", "J-P", "J_P", "PierreJean", "Pierre.Jean", ...]
    """
    name_variations = []

    first = [composed_name[0]]
    second = [composed_name[1]]

    first.append(first_char(composed_name[0]))
    second.append(first_char(composed_name[1]))

    first = generate_string_combinations(first, delimiters)
    name_variations = generate_string_combinations(first, second)

    if first_char(composed_name[0]) not in vowels and first_char(composed_name[1]) not in vowels:
        first = generate_string_combinations(rem_vowel(composed_name[0]), delimiters)
        name_variations.extend(generate_string_combinations(first, rem_vowel(composed_name[1])))
    return list(set(name_variations))

def get_possible_name_variations(name, delimiters):
    """
    Get possible variations of a name, taking into account if it is composed.

    Args:
    name (str): The input name.
    delimiters (list): A list of characters used as delimiters between the first name and last name.

    Returns:
    list: A list of possible variations of the name.

    Examples:
    >>> get_possible_name_variations("Pierre", ["", ".", "-"])
    ["P", "Pierre", "Prr", ""]

    >>> get_possible_name_variations("Jean Pierre", ["", ".", "-"])
    ["JP", "J.P", "J-P", "J_P", "JeanPierre", "Jean.Pierre", ...]

    >>> get_possible_name_variations("Jean-Pierre", ["", ".", "-"])
    ["J", "Jean", "P", "Pierre", "JP", "J.P", "J-P", "J_P", "PierreJean", "Pierre.Jean", ...]

    """
    if "-" not in name and " " not in name:
        return get_possible_simple_name_variations(name)
    elif ' ' in name:
        name_variations = name.split(" ")
        return get_possible_composed_name_variations(name_variations, delimiters)
    else:
        name_variations = name.split("-")
        return get_possible_composed_name_variations(name_variations, delimiters)
