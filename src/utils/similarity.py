from Levenshtein import distance as lev
def name_check_similarity(input_string, lastname):
    """
    Checks the similarity between an input string and a last name.

    Args:
        input_string (str): The input string to check.
        lastname (str): The last name to compare against.

    Returns:
        bool: True if the similarity percentage is above 85%, False otherwise.
    """
    match_count = 0
    for c in lastname:
        if c in input_string:
            match_count += 1

    similarity_percentage = match_count / len(lastname) * 100
    return similarity_percentage > 85


def is_similar(url,lastname):
    """
    Checks if a URL contains a similar first name or last name.

    Args:
        url (str): The URL to check.
        firstname (str): The first name to compare against.
        lastname (str): The last name to compare against.

    Returns:
        bool: True if a similar first name or last name is found in the URL, False otherwise.
    """
    if lastname in url:
        return True

    splitted_url = url.split("/")[4].split("-")
    for name in splitted_url:
        if lev(name, lastname) <= 2:
            return True
        if len(splitted_url) == 1:
                return True
    return False