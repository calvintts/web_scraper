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
    # if(node.find('value',resursive=False)!=None):
    #     print(node.find("value",recursive=False))
for x in array:
    print (x)


# for node in drawing:
#     data={}
#     print(node.find('label',recursive=False))
    # if (node.find('label',recursive=False)):
    #     data['label'] = node.find("label",recursive=False).text
    #     data['value'] = node.find("value",recursive=False).text
    #     array.append(data)
# print(array)




# for child in root:
#     data={}
#     if(child.tag == "attachments_list" or child.tag == "history_list" or child.tag == "approvedby"):
#         continue
#     data['label'] = child.find('label').text
#     data['value'] = child.find('value').text
#     print(data)
#     array.append(data)
