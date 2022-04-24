import requests
import json
# from bs4 import BeautifulSoup
from task_1 import *
from task_4 import movies_detailes
# with open("task1.json","r")as file:
#     data=json.load(file)
movies=scrap_top_list()
def get_movie_list_details():
    list=[]
    for i in movies:
        a=i["url"]
        b=movies_detailes(a)
        list.append(b)
    with open ("task5.json", "w+") as f:
        json.dump(list,f, indent=4)
    return list
get_movie_list_details()