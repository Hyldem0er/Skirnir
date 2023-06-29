def day(string):
    """
    Extract the day from a string representing a date.

    Args:
        string (str): The input date string.

    Returns:
        str: The extracted day.

    Example:
        >>> day("31/12/1993")
        '31'
    """
    dd = string[0:2]
    return dd


def dayI(string):
    """
    Extract the day from a string representing a date and remove leading zeros.

    Args:
        string (str): The input date string.

    Returns:
        str: The extracted day without leading zeros.

    Example:
        >>> dayI("01/12/1993")
        '1'
    """
    if string[0] == '0':
        d = string[1]
    else:
        d = string[0:2]
    return d


def month(string):
    """
    Extract the month from a string representing a date.

    Args:
        string (str): The input date string.

    Returns:
        str: The extracted month.

    Example:
        >>> month("31/12/1993")
        '12'
    """
    mm = string[3:5]
    return mm


def monthI(string):
    """
    Extract the month from a string representing a date and remove leading zeros.

    Args:
        string (str): The input date string.

    Returns:
        str: The extracted month without leading zeros.

    Example:
        >>> monthI("31/09/1993")
        '9'
    """
    if string[3] == '0':
        m = string[4]
    else:
        m = string[3:5]
    return m


def year(string):
    """
    Extract the year from a string representing a date.

    Args:
        string (str): The input date string.

    Returns:
        str: The extracted year.

    Example:
        >>> year("31/12/1993")
        '1993'
    """
    aaaa = string[6:10]
    return aaaa


def yearII(string):
    """
    Extract the last two digits of the year from a string representing a date.

    Args:
        string (str): The input date string.

    Returns:
        str: The extracted last two digits of the year.

    Example:
        >>> yearII("31/12/1993")
        '93'
    """
    aa = string[8:10]
    return aa


def yearI(string):
    """
    Extract the last two digits of the year from a string representing a date and remove leading zeros.

    Args:
        string (str): The input date string.

    Returns:
        str: The extracted last two digits of the year without leading zeros.

    Example:
        >>> yearI("31/12/2003")
        '3'
    """
    if string[8] == '0':
        m = string[9]
    else:
        m = string[8:10]
    return m
