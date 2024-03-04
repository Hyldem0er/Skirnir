def get_nicknames_variations_with_delimiters(alias, delimiters):
    """
    Generate all variations of a alias with different delimiters.

    Args:
        alias (str): The input alias.
        delimiters (list): A list of delimiters used to generate variations.

    Returns:
        list: A list of alias variations.

Example:
    >>> get_nicknames_variations_with_delimiters("cassos du 76", [".", "-", "_"])
    ["cassos du 76", "cassos.du.76", "cassos-du-76", "cassos_du_76", "cassos du 76", "cassos.du.76", "cassos-du-76", "cassos_du_76"]
"""


    delimiters.append(" ")
    nicknames_variation = [alias]
    for d in delimiters:
        if d in alias and d != '':
            for deli in delimiters:
                if d != deli:
                    nicknames_variation.append(alias.replace(d, deli))
    return nicknames_variation
