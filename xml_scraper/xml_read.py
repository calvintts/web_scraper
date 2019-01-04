from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import array
import json
import re
import tablib
import os
def add_attachment_extension(att_file_name,index):
    return att_file_name.replace('.','_attachment_'+chr(ord('A')+index)+'.')
def extract(filename):
    file = open(filename,"r")
    xml_file = file.read()
    file.close()
    xml_page = soup(xml_file,"xml")
    array = []
    needed = ['ID','Document','Revision','Submitted','Created','Issued To','Status','Due Date','REASON','Date Approved','COMMENT BY AUTHORITY','Notice of prohibition','Notice of improvement','Non conformance report (NCR)','Observation','Other','No of notices','No notice issued','Date']
    # print(xml_page)
    body = xml_page.find('authority_visit')
    for node in body.findChildren(recursive=False):
        data={}
        if (node.name == 'projectcode'):
            continue
        result = (node.find('label',recursive=False)!=None)
        if(result and (node.find('label',recursive=False)).string in needed):
            data['label']=(node.find('label',recursive=False)).string
            data['value']=(node.find('value',recursive=False)).string
            array.append(data)
        if(node.name == 'attachments_list'):
            attachments = node.find_all('filename')
            for index, a in enumerate(attachments):
                data['label']='Document File Name'
                data['value']=add_attachment_extension((a.find('value',recursive=False)).string,index)
                array.append(data)
    return array

print (extract('authority_att.xml'))
temp = []
for x in extract('authority_att.xml'):
    item = object()
    placeholder = str(x['label'])
    item.placeholder=x['value']
    # item.(x['label'])=x['value']
    # temp.append(item)
for x in temp:
    print (x)

# d = tablib.Dataset()
# # d.headers = ('firstname','lastname')
# # d.append(('Calvin','Tey'))
# # d.headers = arra
# # for a in array:
# lbl = []
# val = []
# for item in array:
#     lbl.append(item['label'])
#     val.append(item['value'])
# print (lbl)
#
# d.headers = lbl
# d.append(val)
#
# print (d.dict)
# d.export('xls')
#
# with open('output2.xls','wb') as f:
#     f.write(d.xls)
