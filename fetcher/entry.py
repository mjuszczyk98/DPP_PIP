import requests


def fetch_entries_page(key, page=0):
    link = 'https://api.e-science.pl/api/azon/entry/filter/?limit=100&offset=' + str(page) +'00'
    try:
        return requests.get(link, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e


def fetch_author_entries(key, pk):
    link = 'https://api.e-science.pl/api/azon/authors/entries/' + str(pk) + '/'
    try:
        return requests.get(link, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e
