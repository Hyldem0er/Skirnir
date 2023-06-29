import requests
from random import choice
import json

def retrieve_proxies_list():

    # Use requests to send a GET request to the proxy list
    r = requests.get('https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json', headers={"Content-Type":"application/json"})

    formatted_proxies_list = []

    for proxy in r.json():
        formatted_proxies_list.append("http://" + proxy["ip"] + ":" + str(proxy["port"]))
    return formatted_proxies_list


def get_proxy():
    """
    Retrieves a proxy from the list of available proxies.

    This function calls the 'retrieve_proxies_list()' function to obtain a list of proxies.
    It then randomly selects a proxy from the list using the 'choice()' function from the 'random' module.

    Returns:
        str: A randomly selected proxy from the list.

    Example:
        >>> get_proxy()
        '127.0.0.1:8080'
    """
    proxies_list = retrieve_proxies_list()
    return choice(proxies_list)
