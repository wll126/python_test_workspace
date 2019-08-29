import requests


def get_page(url):
    response=requests.get(url)
    return response.text

