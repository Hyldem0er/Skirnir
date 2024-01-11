import requests, sys
from .user_agents import get_useragent_mobile
from .Proxy import Proxy
from loguru import logger

logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")

import requests

def get(url, proxy = None, timeout=5, header=None):
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

    logger.info(url)
    
    # proxies = {'http': 'http://user:pass@10.10.1.10:3128/'}
    proxies_dict = {}

    if proxy:
        selected_proxy = proxy.get_proxy()
        if proxy.is_private_proxy():
            proxies_dict = {
                "https": "https://" + selected_proxy["Username"] + ":" + selected_proxy["Password"] + "@" + selected_proxy["IP Address"] + ":" + selected_proxy["Port"] + "/",
                "http":  "http://" + selected_proxy["Username"] + ":" + selected_proxy["Password"] + "@" + selected_proxy["IP Address"] + ":" + selected_proxy["Port"] + "/"
            }
        else:
            proxies_dict = {
                "https": selected_proxy["IP Address"] + ":" + selected_proxy["Port"],
                "http": selected_proxy["IP Address"] + ":" + selected_proxy["Port"]
            }

    headers = {"User-Agent": get_useragent_mobile()}
    if header:
        headers.update(header)

    print(proxies_dict)

    resp = requests.get(
        url=url,
        headers=headers,
        timeout=timeout,
        proxies=proxies_dict
    )
    resp.raise_for_status()
    logger.info(resp.status_code)
    return resp
