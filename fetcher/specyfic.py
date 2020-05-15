import requests


def fetch_data_with_link(key, link):
    try:
        return requests.get(link, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e
