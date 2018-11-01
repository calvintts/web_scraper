from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import array
import json
import re

def get_html_format (url):
    html_page = uReq(url)
    get_html = html_page.read()
    html_page.close()
    return soup(get_html,"html.parser")

chicken_recipe_html = get_html_format("https://www.allrecipes.com/recipes/201/meat-and-poultry/chicken/")
all_articles = chicken_recipe_html.find(id="main-content").find_all('article')
links = []
for article in all_articles:
    if(article.find('a')!=None):
        links.append(article.find('a')['href'])
# print (links)

item_list = []
def validate_link(somestring):
    return "video" in somestring or "www" not in somestring

for link in links:
    item = {}
    if(validate_link(link)):
        continue
    recipe_page = get_html_format(link)
    print(link)
    if(recipe_page.find(id='recipe-main-content') != None):
        item['name'] = recipe_page.find(id='recipe-main-content').text
    if(recipe_page.find(id="polaris-app") != None):
        ingredient_box = recipe_page.find(id="polaris-app")
        ingredients_list = []
        if(ingredient_box.find_all('li') !=None):
            for ingredients in ingredient_box.find_all('li'):
                if(ingredients.text.strip() != "Add all ingredients to list"):
                    ingredients_list.append(ingredients.text.strip())
                    item['ingredients'] = ingredients_list
    if(recipe_page.find("div",class_="directions--section")!=None):
        directions_list = []
        direction_box = recipe_page.find("div",class_="directions--section")
        # print(direction_box)
        if(direction_box.find_all('ol',class_="recipe-directions__list")!=None):
            direction = direction_box.find('ol',class_="recipe-directions__list")
            direction = direction.find_all('span',class_='recipe-directions__list--item')
            for step in range(0, len(direction)):
                directions_list.append(("Step "+ str(step+1) +": "+direction[step].text.replace("Watch Now","")).strip())
            item['directions']= directions_list
    item_list.append(item)

for x in item_list:
    print(x['name'])
    print(x['ingredients'])
    print(x['directions'])
