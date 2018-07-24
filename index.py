from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import array
import json

myurl = "https://www.phonearena.com/"

something = uReq(myurl)
html_page = something.read()
something.close()
#html parsing
soup_page = soup(html_page, "html.parser")
items = soup_page.findAll("div",{"class":"ln-item"})
array = []
#grabs each product
for item in items:
    data = {}
    data['title'] = item.div.h3.a.text
    data['image'] = item.div.img["src"]
    data['author'] = item.findAll("span",{"class":"author"})
    array.append(data)
print(array[0])
