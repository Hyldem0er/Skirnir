import requests, sys, time
# from .user_agents import get_useragent, get_useragent_mobile
# from .proxies import get_proxy
from loguru import logger
from requests_html import HTMLSession, HTML
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")

import requests

# def get(url, timeout=5, header=None):
#     """
#     Sends an HTTP GET request to the specified URL.

#     Args:
#         url (str): The URL to send the GET request to.
#         timeout (int, optional): The maximum number of seconds to wait for the server's response. Defaults to 5.
#         header (dict, optional): Additional headers to include in the request. Defaults to None.

#     Returns:
#         requests.Response: The response object containing the server's response to the GET request.

#     Raises:
#         requests.HTTPError: If the GET request returns a non-2xx status code.

#     Example:
#         >>> get("https://example.com")
#         <Response [200]>
#     """

#     logger.info(url)

#     # proxies_dict = {
#     #     "https": get_proxy(),
#     #     "http": get_proxy()
#     # }
    
#     # url += "&start=" + str(start)
#     # url += "&hl=" + lang 
#     # print("url: " + url)

#     headers = {"User-Agent": get_useragent()}
#     if header:
#         headers.update(header)

#     resp = requests.get(
#         url=url,
#         headers=headers,
#         timeout=timeout,
#         # proxies=proxies_dict
#     )
#     resp.raise_for_status()
#     logger.info(resp.status_code)
#     return resp

def get_html(url, timeout=5, header=None):
    logger.info(url)

    session = HTMLSession()
    # headers = {"User-Agent": get_useragent_mobile()}
    # if header:
    #     headers.update(header)

    resp = session.get(
        url=url
        # headers=headers,
        # timeout=timeout,
        # proxies=proxies_dict
    )
    session.close()

    resp.raise_for_status()
    logger.info(resp.status_code)
    return resp



def get_dynamic_content(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (without a visible browser)
    driver = webdriver.Chrome()

    try:
        driver.get(url)
        # Allow some time for dynamic content to load (you might need to adjust this)
        driver.implicitly_wait(10)
        time.sleep(10)
        # You can now access the page source with dynamically loaded content
        html_content = driver.page_source

        return html_content
    finally:
        driver.quit()

def parse_dynamic_content(html_content):
    try:
        # Create an HTML object from the content
        html = HTML(html=html_content)

        # Now you can use requests_html methods to extract information
        links = html.absolute_links
        for link in links:
            print(link)

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    try:
        resp = get_dynamic_content("https://duckduckgo.com/?q=%22Jean+Deriaux%22+site%3Afacebook.com&ia=web")
        parse_dynamic_content(resp)
    except Exception as e:
        logger.exception(e)
        return []

# main method
if __name__ == '__main__':
    main()