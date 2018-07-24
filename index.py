from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myurl = "https://www.phonearena.com/"

something = uReq(myurl)
html_page = something.read()
something.close()
#html parsing
soup_page = soup(html_page, "html.parser")
#grabs each product
items = soup_page.findAll("div",{"class":"ln-item"})
print(len(items))
