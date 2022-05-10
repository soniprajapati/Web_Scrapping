import json
import requests
from bs4 import BeautifulSoup

with open("task5.json","r") as file:
    a=json.load(file)

def analyse_movies_director():
    dict={}
    for i in a:

        if "director" in i:
            director=i["director"]

            for i in director:
                if i not in dict:
                    dict[i]=1

                else:
                    dict[i]+=1

    with open("task7.json","w") as f:
        json.dump(dict,f,indent=4)
    
analyse_movies_director()   