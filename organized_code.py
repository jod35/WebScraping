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
        title = bs.h1

    except AttributeError as e:
        return None

    return title


title = get_title('https://jod35.netlify.app')


if title == None:
    print('Title could not be found')
else:
    print(title)

"""
<h1 class="name white-text text-center">
            Hello! I am <span class="red-text">Ssali Jonathan</span>
</h1>
"""
