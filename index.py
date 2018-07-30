from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import array
import json
import re
# schema
# {
#     number: {type: Number,},
#     title: {type: String},
#     subtitle: {type: String},
#     details: {type: String}, // short details
#     category: {type: String},
#     price: {type: String},
#     rating: {type: String},
#     date: {type: String},
#     coverImage: {type: String},
#     slides: [{type: String}],
#     titleLink: {type: String},
#     subtitleLink: {type: String},
#     fileLink: {type: String},
#     imageLink: {type: String},
#     description: {type: String}, // long description
#     others: {type: String},
#     copyrightInfo: {type: String}
# }

# {
# 	title: string,
# 	subtitle: string,
# 	description: string,
# 	category: string,
# 	subcategory: string,
# 	typeMain: number,
#   date: date,
# 	covers: [string],
# 	copyrightInfo: string,
# 	sources: [string],
# 	tags: [string],
# 	data: [
# 		{
# 			data: string,
# 			link: string,
# 			type: number
# 		}
# 	]
# }

# def scrap_item(url):
#     url_req = uReq(url)
#     url_read = url_req.read()
#     url_req.close()
#     temp = {}
#     page = soup(url_read,"html.parser")
#     page_info = page.find("article",{"class":"news-article"})
#     title = page_info.header.h1.string
#     print("title: ", title)
#     author_list = []
#     for author in page_info.find_all("span",{"class":"by-author"}):
#         author_list.append(author.text.strip().replace(',',''))
#     print("authors: ", author_list)
#     date = page_info.find("time",{"class":"relative-date"}).get('datetime')
#     print("date: " ,date)
#     category = page_info.find("a",{"class":"category"}).string.strip()
#     print("category: ", category)
#     covers = page_info.find('img').get('src')
#     print("covers: ",covers)
    # for paragraph in pageinfo.find_all('p'):
    #     if(paragraph.)


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
header = soup_page.find("header")
content = soup_page.find("")
if(header.h1.string):
    title = header.h1.string
author_list = []
for author in header.find_all("span",{"class":"by-author"}):
    if(author):
        author_list.append(author.text.strip().replace(',',''))
if(header.div.h2.string):
    subtitle = header.div.h2.string
if(header.find("time")):
    time = header.find("time").string.strip()
if(header.find("a",{"class":"category"})):
    category = header.find("a",{"class":"category"}).string.strip()
# print(title)
# print(subtitle)
# print(author_list)
# print(time)
# print(category)
if(soup_page.find("div",{'class':'box'}).img):
    covers = [soup_page.find("div",{'class':'box'}).img["src"]]
print('COVERS: ',covers)
phone_list = []
content = soup_page.find("div",{'id':'article-body'})
for phone_title in content.find_all('h3'):
    if(phone_title.previous_sibling.img):
        imageLink = phone_title.previous_sibling.img['data-src']
        print ("IMAGE SRC: ",imageLink)
    title = phone_title.text.strip()
    print("TITLE: ",title)
    iterator = phone_title.next_sibling
    advan = []
    disadvan = []
    text =""
    while( iterator.next_sibling != None and iterator.next_sibling.name != 'h3'):
        if(iterator.name == 'aside'):
            price = iterator.find("div",{"class":"hawk-price-deal-price-container"}).text
            print("PRICE: ",price)
        if(iterator.has_attr("class")):
            if("subtitle" in iterator['class']):
                subtitle = iterator.text.strip()
                print("SUBTITLE: " ,subtitle)
        if(iterator.name == 'p' and iterator.previous_sibling.has_attr('class')):
            if('subtitle' in iterator.previous_sibling['class']):
                details = iterator.text.strip()
                print("DETAILS: ",details)
        if(iterator.name =='div' and 'icon-plus_circle' in iterator['class']):
            advan.append(iterator.text.strip())
            # print("ADVANTAGES: ", advan)
        if(iterator.name =='div' and 'icon-minus_circle' in iterator['class']):
            disadvan.append(iterator.text.strip())
            # print("DISADVANTAGES: ",disadvan)
        elif(iterator.name =='p' and iterator.text!=None):
            if(not "Read the full review" in iterator.text):
                text = text + iterator.text
        iterator = iterator.next_sibling
    print("ADVANTAGES: ", advan)
    print("DISADVANTAGES: ",disadvan)
    print("TEXT DETAILS: ",text)
    # print(subtitle)
    print("\n\n")
    # print("\n\n")
    # print("\n\n")
    # print("\n\n")
    continue

    # phone={}
    # # if(phone_title.previous_sibling.find("img")):
    # #     imageLink = []
    # #     for images in phone_title.previous_sibling.img['src']:
    # #         imageLink.append(images['src'])
    # #     phone['imageLink'] = imageLink
    # print(phone_title.previous_sibling.find('img')['src'])
    # iterator = phone_title.next_sibling
    # phone['title'] = phone_title.text.strip()
    # if('subtitle' in iterator['class']):
    #     phone['subtitle'] = iterator.text.strip()
    #     iterator = phone_title.next_sibling
    # # print (phone['imageLink'])
    # print (phone['title'])
    # # print (phone['imageLink'])

    # if("subtitle" in iterator['class']):
    #     list_subtitle = iterator.text.strip()
    # iterator = iterator.next_sibling


# for subt in content.find_all('div',{'class':'subtitle'}):
#     print ("SUBTITLE: ",subt.p.text)
#     if(subt.next_sibling.name == 'p'):
#         print ("DETAILS :",subt.next_sibling.text)
