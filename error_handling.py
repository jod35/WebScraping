from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

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
    bs = BeautifulSoup(html, 'html.parser')

# in case the tag is not in existence
try:
    # gets the tag that is not existing
    bad_content = bs.find('nonExistentTag')

except AttributeError as e:
    print('Tag doesnot exist')

else:
    if bad_content == None:
        print("Tag was not found!")

    else:
        print(bad_content)
