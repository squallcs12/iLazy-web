import requests
from urllib.parse import urlparse, parse_qs


def vbb_new_reply(url):
    url = "%s&goto=newpost" % url
    response = requests.get(url)
    location = response.url

    query = urlparse(location).query
    query = parse_qs(query)
    return query
