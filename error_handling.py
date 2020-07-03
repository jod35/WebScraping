from urllib.request import urlopen
from urllib.error import HTTPError, URLError

# try this
try:
    html = urlopen('https://github.com/jod35/WebScraping')


# if it fails to locate the website, do this
except HTTPError as e:
    print(e)

# if it fails to locate the server
except URLError as e:
    print(e)

# if successful,
else:
    print("Everything is just too good.")
