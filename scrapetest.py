from urllib.request import urlopen
from bs4 import BeautifulSoup


# opening the html document
html = urlopen('http://pythonscraping.com/pages/page1.html')

# parsing it as clean HTML
bs = BeautifulSoup(html.read(), 'html.parser')

print(bs.h1)
