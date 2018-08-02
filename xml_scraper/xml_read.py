from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import array
import json
import re
import tablib


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

d = tablib.Dataset()
# d.headers = ('firstname','lastname')
# d.append(('Calvin','Tey'))
# d.headers = arra
# for a in array:
lbl = []
val = []
for item in array:
    lbl.append(item['label'])
    val.append(item['value'])
print (lbl)

d.headers = lbl
d.append(val)

print (d.dict)
d.export('xls')

with open('output.xls','wb') as f:
    f.write(d.xls)
