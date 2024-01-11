import webbrowser

def open_social_network_login_page(instagram, facebook, twitter, linkedin, tiktok):
    
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
