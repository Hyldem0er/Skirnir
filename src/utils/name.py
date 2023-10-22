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
