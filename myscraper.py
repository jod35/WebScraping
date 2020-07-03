from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_title(url):

    try:
        html = urlopen(url)

    except HTTPError as e:
        return None

    try:
        bs = BeautifulSoup(html, 'html.parser')
        title = bs.body.h1

    except AttributeError as e:
        return None

    return title


title = get_title('https://github.com/jod35')

if title == None:
    print(" Title doesnot exist")
else:
    print(title)
