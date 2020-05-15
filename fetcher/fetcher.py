import requests


def fetch_programming_languages(key):
    link = 'https://api.e-science.pl/api/azon/programminglanguages/'
    try:
        return requests.get(link, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e


def fetch_research_centers(key):
    link = 'https://api.e-science.pl/api/azon/databases/pwr_research_centers/'
    try:
        return requests.get(link, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e


def fetch_laboratories(key):
    link = 'https://api.e-science.pl/api/azon/databases/elaboratory/'
    try:
        return requests.get(link, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e
