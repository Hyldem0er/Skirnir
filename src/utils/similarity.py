from Levenshtein import jaro_winkler as jar

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
        if jar(name, lastname, score_cutoff=True) >= 0.85:
            return True
        if len(splitted_url) == 1:
                return True
    return False