from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import array
import json
import re


file = open("test.xml","r")
xml_file = file.read()
file.close()
xml_page = soup(xml_file,"xml")
array = []
# print(xml_page)
drawing = xml_page.find('drawing')
for node in drawing.findChildren(recursive=False):
    data={}
    result = (node.find('label',recursive=False)!=None)
    if(result):
        data['label']=(node.find('label',recursive=False)).string
        data['value']=(node.find('value',recursive=False)).string
        array.append(data)

for x in array:
    print (x)
