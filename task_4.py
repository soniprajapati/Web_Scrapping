import requests
import json
from bs4 import BeautifulSoup
from task_1 import *


movie_url="https://www.rottentomatoes.com/m/toy_story_3"


def movies_detailes(movie_url):
    page=requests.get(movie_url)
    soup=BeautifulSoup(page.text,"html.parser")
    
    movie_name=soup.find("h1",class_="scoreboard__title").get_text()
    main_div=soup.find_all("li",class_="meta-row clearfix")
    dict={}
    list1=[]
    dict["movie_name"]=movie_name
    dict["Url"]=movie_url
    for i in main_div:
        a=i.text
        b=a.split()
        # print(movie_name)
        if "Rating:" in b:
            dict["Rating"]=b[1]
            # print(dict)
        elif "Language:" in b:
            list1.append(b[-1])
            dict["Language"]=list1
            # print(dict)
        elif "Genre:"in b:
            dict["Genre"]=b[1:]
            # print(dict)
        elif "Director:" in b:
            i = 0
            list2 = []
            while i < len(b):
                if i == 0:
                    i += 1
                    continue
                list2.append(b[i])
                # print(list2)
                i += 1
            s=""
            for i in list2:
                for j in i:
                    if j==" ":
                        continue
                    else:
                        s+=j
            list3=s.split(",")
            dict["director"] = list3
            # print(dict)
        elif "Producer:" in b:
            dict["Producer"]=b[1:]
            # print(dict)
        elif "Runtime:" in b:
            run_time=[]
            for j in b:
                # print(type(j))
                if j != "Runtime:":
                    t=j[:-1]
                    # print(t)
                    run_time.append(int(t))
                for i in range(len(run_time)):
                    if i==0:
                        min=run_time[i]*60
                    elif i==1:
                        min=run_time[0]*60+run_time[i]
            dict['Runtime']=min
            # print(dict)
    with open ("task4.json", 'w') as task4_file:
        json.dump(dict, task4_file, indent=6)
        return(dict)
movies_detailes(movie_url)