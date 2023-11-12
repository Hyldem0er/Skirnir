def format_url(url):
    """
    Formats a URL by replacing certain substrings.

    Args:
        url (str): The URL to be formatted.

    Returns:
        str: The formatted URL.

    Example:
        >>> format_url("https://www.example.com//fr/page")
        'https://www.example.com//www/page'
    """
    return url.replace("//m.", "//www.")
