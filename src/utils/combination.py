def generate_string_combinations(list1, list2):
    """
    Generate all possible combinations of strings from two given lists.

    Args:
        list1 (list): The first list of strings.
        list2 (list): The second list of strings.

    Returns:
        list: A list of all possible combinations of strings from list1 and list2.

    Example:
        >>> generate_string_combinations(['a', 'b', 'c'], ['x', 'y', 'z'])
        ['ax', 'ay', 'az', 'bx', 'by', 'bz', 'cx', 'cy', 'cz']
    """
    return [elt1 + elt2 for elt1 in list1 for elt2 in list2]
