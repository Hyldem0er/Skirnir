from src.utils.date import *
from src.utils.combination import generate_string_combinations


def is_correct_date_combination(day, month, year, delimiters):
    """
    Check if a date combination is correct (i.e., month and year use the same delimiter, and day and month have the same length if not using a delimiter)
    
    Args:

        day (str): The day value.

        month (str): The month value.

        year (str): The year value.

        delimiters (list): A list of characters used as delimiters between day, month, and year.
    
    Returns:
        bool: True if the date combination is valid, False otherwise.
    """
    if month[0] == year[0] and (len(day) == len(month) and month[0] not in delimiters or len(day) != len(month) and month[0] in delimiters):
        return True
    return False


def get_possible_date_combinations(date):
    """
    Convert a date string into a list of possible day, month, and year combinations.

    Args:
        date (str): The input date string.

    Returns:
        tuple: A tuple of lists of possible day, month, and year combinations.

    Example:
        >>> get_possible_date_combinations("31/12/1993")
        ([31], [12], [1993, 93, 3])
    """
    days = []
    months = []
    years = []

    # To avoid duplicates
    if day(date) == dayI(date):
       days.append(day(date))
    else:
       days.append(day(date))
       days.append(dayI(date))

    if month(date) == monthI(date):
        months.append(month(date))
    else:
        months.append(month(date))
        months.append(monthI(date))
    years.append(year(date))
    years.append(yearI(date))
    years.append(yearII(date))

    return (days, months, years)


def get_possible_date_combination_with_delimiters(birthday, delimiters):
    """
    Generates all possible combinations of birthday with delimiters.

    Args:
        delimiters (list): List of delimiters to be used for combination.
        birthday (string): birthday to be combined with delimiters.

    Returns:
        list: A list of all possible combinations of birthday with delimiters.

    Example:
        delimiters = ['-', '_', '.', '']

        birthday = "31/12/1993"

        Output: ["-31", "-12", "-1993", "-93", "-3", ".31", ".12", ".1993", ".93", ".3", ..., "31-12-1993", "31.12.1993", ...]
    """
    dates = []

    days, months, years = get_possible_date_combinations(birthday)

    months = generate_string_combinations(delimiters, months)
    yearsWithdelimiters = generate_string_combinations(delimiters, years)
    for day in days:
        for month in months:
            for year in yearsWithdelimiters:
                if is_correct_date_combination(day, month, year, delimiters):
                        dates.append(day + month + year)
    dates.extend(years)

    dates = generate_string_combinations(delimiters, list(set(dates)))
    dates.append("")

    return dates