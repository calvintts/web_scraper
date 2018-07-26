from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import array
import json
import re

def scrap_item(url):
    url_req = uReq(url)
    url_read = url_req.read()
    url_req.close()
    temp = {}
    page = soup(url_read,"html.parser")
    page_info = page.find("article",{"class":"news-article"})
    title = page_info.header.h1.string
    print("title: ", title)
    author_list = []
    for author in page_info.find_all("span",{"class":"by-author"}):
        author_list.append(author.text.strip().replace(',',''))
    print("authors: ", author_list)
    date = page_info.find("time",{"class":"relative-date"}).get('datetime')
    print("date: " ,date)
    category = page_info.find("a",{"class":"category"}).string.strip()
    print("category: ", category)
    covers = page_info.find('img').get('src')
    print("covers: ",covers)
    for paragraph in pageinfo.find_all('p'):
        if(paragraph.)


    # temp['text'] = content.text.strip()
    # print(temp['text'])
    # if(content.find_all('img')):
    #     temp['image']= []
    #     for pic in content.find_all('img'):
    #         temp['image'].append(pic.get('src'))
    # if(content.find_all('iframe')):
    #     temp['videos']= []
    #     for vid in content.find_all('iframe'):
    #         temp['videos'].append(vid.get('src'))
    # if(page_info.h1):
    #     temp['title'] = page_info.h1.text
    # if(page_info.find("p",{"class":"s_date"}).timcleare):
    #     temp['date'] = page_info.find("p",{"class":"s_date"}).time.text
    # if(page_info.find("p",{"class":"s_date"})):
    #     dummy = page_info.find("p",{"class":"s_date"}).text.split("by")
    #     temp['author'] = dummy[len(dummy)-1].strip()
    # return temp

myurl = "https://www.techradar.com/news/phone-and-communications/mobile-phones/best-cheap-smartphones-payg-mobiles-compared-1314718"

something = uReq(myurl)
html_page = something.read()
something.close()
#html parsing
soup_page = soup(html_page, "html.parser")
container = soup_page.findAll("div",{"id":["main"]})
array = []
scrap_item(myurl)
#grabs each article from homepage
# for article in articles:
#     data = {}
#     data['title'] = article.div.h3.a.text
#     #data['image'] = article.div.img["src"]
#     data['link']= myurl + article.a["href"]
#     #data['info']= scrap_item(data['link'])
#     try:
#         data['information']=scrap_item(data['link'])
#         array.append(data)
#     except:
#         print(data['title']+ 'page is skipped')

#
# for item in array:
#     print(item)
#     print()
#     print()

# testitem = array[0]
# print(testitem)




    # details_page = details.read()
    # details.close()
    # page_info = soup(details_page,"html.parser")
    # page_content = page_info.find("div",{"class":"s_static"})
    # data['image'] = page_content.div.img["src"]
    # data['text'] = page_content.find("div",{"id":"article-content"}).find(recursive=False).text
    # date_and_author_box = page_info.find("p",{"class":"s_date"})
    # data['date'] = date_and_author_box.time.text
    # dummy = date_and_author_box.text.split("by")
    # data['author'] = dummy[len(dummy)-1].strip()
