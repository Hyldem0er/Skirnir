import webbrowser

import webbrowser

def open_social_network_login_page(instagram, facebook, twitter, linkedin, tiktok):
    """
    Opens the login page for selected social networks in a web browser.

    Args:
        instagram (bool): Open Instagram login page if True.
        facebook (bool): Open Facebook login page if True.
        twitter (bool): Open Twitter login page if True.
        linkedin (bool): Open LinkedIn login page if True.
        tiktok (bool): Open TikTok login page if True.
    """
    if instagram:
        webbrowser.open("https://www.instagram.com/accounts/login/")
    if facebook:
        webbrowser.open("https://www.facebook.com/login")
    if twitter:
        webbrowser.open("https://twitter.com/i/flow/login")
    if linkedin:
        webbrowser.open("https://www.linkedin.com/login/")
    if tiktok:
        webbrowser.open("https://www.tiktok.com/login")
