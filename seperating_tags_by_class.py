from bs4 import BeautifulSoup
from urllib.request import urlopen


html = urlopen('https://pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')

# find all span tags with the class green
name_list = bs.findAll('span', {'class', 'green'})

names = []

for name in name_list:
    n = str(name.get_text())
    names.append(n)

print(f"{len(names)} Items")
print(names)
