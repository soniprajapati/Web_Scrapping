# import json
# import requests
# from bs4 import BeautifulSoup

# url="https://www.rottentomatoes.com/m/toy_story_4"

# raw=requests.get(url)

# soup=BeautifulSoup(raw.text,"html.parser")

# def scrap_movie_cast():
#     main_div=soup.find("div",class_="castSection")
#     ancor=main_div.find_all("a",class_="unstyled articleLink")
#     dict={}
#     for i in ancor:
#         list=[]
#         actor=i.text.strip()
#         dict["cast_name"]=actor
#         list.append(dict)
#         print(list)
#     with open("task12.json","a+") as file:
#         json.dump(dict,file,indent=4)

# scrap_movie_cast()
        
# print(ancor)


from bs4 import BeautifulSoup
import requests,json
def scrape_movie_cast(URL):
    req=requests.get(URL)
    shop=BeautifulSoup(req.text,"html.parser")
    main_d=shop.find("div",class_="castSection")
    d1=main_d.find_all("div",class_="cast-item media inlineBlock")
    d2=main_d.find_all("div",class_="cast-item media inlineBlock moreCasts hide")
    l=[]
    for i in d1:
        dic={}
        a=i.find("a")["href"][11:]
        dic["name"]=a
        l.append(dic)
    # print(l)
    for j in d2:
        dic1={}
        a1=j.find("a")["href"][11:]
        dic1["name"]=a1
        l.append(dic1)
    with open("task12.json","w+") as file:
        json.dump(l,file,indent=4)
        return l
scrape_movie_cast("https://www.rottentomatoes.com/m/toy_story_4")