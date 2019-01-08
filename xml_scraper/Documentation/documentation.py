from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os
import pandas as pd
import re

def restructure_kv_pair(x):
    for item in x:
        item['value'] =  int(item['value']) if str(item['value']).isdigit() else item['value']
        item['value'] =  '-' if item['value']==None else item['value']
    return {item['label']:item['value'] for item in x}

def add_attachment_extension(att_file_name,index):
    return att_file_name.replace('.','_attachment_'+chr(ord('A')+index)+'.')

def extract(filename):
    file = open(filename,"r")
    xml_file = file.read()
    file.close()
    xml_page = soup(xml_file,"xml")
    array = []
    needed = ['ID','Document','Subject','Revision','Created','Created By User','Issued To','Status','Month','Year','Comment','Department']
    # print(xml_page)
    body = xml_page.find('documentation')
    for node in body.findChildren(recursive=False):
        data={}
        if (node.name == 'projectcode'):
            continue
        result = (node.find('label',recursive=False)!=None)
        if (result and (node.find('label',recursive=False)).string in needed):
            data['label']=(node.find('label',recursive=False)).string
            data['value']=(node.find('value',recursive=False)).string
            array.append(data)
        if node.name == 'attachments_list' :
            attachments = node.find_all('filename')
            data['label']='Document File Name'
            data['value']=[]
            for index, a in enumerate(attachments):
                data['value'].append(add_attachment_extension((a.find('value',recursive=False)).string,index))
                array.append(data)
    return array

files = os.listdir()
final_array = []
col=['ID','Document','Subject','Revision','Created','Created By User','Issued To','Status','Month','Year','Comment','Department','Document File Name','Document Name']
for file in files:
    t = file.split('.')
    ext = t[-1]
    if('documentation'in file.lower() and ext=="xml"):
        data = restructure_kv_pair(extract(file))
        print(data)
        filename = "".join(t[:-1])
        filename_with_extension = "".join(t[:-1]) + ".pdf"
        data['Document Name']=filename
        if('Document File Name' in data):
            all_attachments = data['Document File Name']
            for att in all_attachments:
                new_dict = dict(data)
                new_dict['Document File Name']=att
                print(new_dict['Document File Name'])
                final_array.append(new_dict)
        data['Document File Name']=filename_with_extension
        final_array.append(data)
    result = pd.DataFrame(final_array,columns=col)
    result.to_csv("Documentation1.csv")
    # del t[-1]
    # name = "".join(t)
    # print("Name: "+name)
    # print("Extension: "+ext)
