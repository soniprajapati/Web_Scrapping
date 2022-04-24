import json
import requests
from bs4 import BeautifulSoup

url="https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/"
res=requests.get(url)

soup=BeautifulSoup(res.text,"html.parser")

def scrap_top_list():
    list=[]
    main_div=soup.find("div",class_="container")
    div2=main_div.find("div",class_="panel-body content_body allow-overflow")
    table=div2.find("table",class_="table")
    table_row=table.find_all("tr")
    for i in table_row:
        dic={}
        td=i.find_all("td")
        for k in td:
            movie_name=i.find("a",class_="unstyled articleLink")["href"][3:]
            dic["name"]=movie_name
            movie_rank=i.find("span",class_="tMeterScore").get_text()[1:3]
            dic["rate"]=movie_rank
            all_year=i.find("a",class_="unstyled articleLink").get_text()
            year=all_year.strip()
            dic["year"]=int(year[-5:-1])
            url=i.find("a",class_="unstyled articleLink")["href"]
            one="https://www.rottentomatoes.com/"+url
            dic["url"]=one
        list.append(dic)
        if {} in list:
            list.remove({})
        myfile=open("task1.json","w")
        json.dump(list,myfile,indent=4)
        myfile.close()
    return list
        


scraped=scrap_top_list()
print(scraped)


# print(res.text)

