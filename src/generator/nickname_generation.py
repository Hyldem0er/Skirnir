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
