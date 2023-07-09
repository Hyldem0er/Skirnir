import requests
from .user_agents import get_useragent
from .proxies import get_proxy

import requests

def get(url, timeout=5, header=None):
    """
    Sends an HTTP GET request to the specified URL.

    Args:
        url (str): The URL to send the GET request to.
        timeout (int, optional): The maximum number of seconds to wait for the server's response. Defaults to 5.
        header (dict, optional): Additional headers to include in the request. Defaults to None.

    Returns:
        requests.Response: The response object containing the server's response to the GET request.

    Raises:
        requests.HTTPError: If the GET request returns a non-2xx status code.

    Example:
        >>> get("https://example.com")
        <Response [200]>
    """

    print(url)
    proxies_dict = {
        "https": get_proxy(),
        "http": get_proxy()
    }
    
    # url += "&start=" + str(start)
    # url += "&hl=" + lang 
    # print("url: " + url)

    headers = {"User-Agent": get_useragent()}
    if header:
        headers.update(header)

    resp = requests.get(
        url=url,
        headers=headers,
        timeout=timeout,
        proxies=proxies_dict
    )
    resp.raise_for_status()
    return resp
