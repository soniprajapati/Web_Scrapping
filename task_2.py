import json
from task_1 import scrap_top_list

scraped=scrap_top_list()

def group_by_year(movies):
    dic={}
    for i in movies:
        year=i["year"]
        movie=[]
        for j in movies:
            if j["year"]==year:
                movie.append(j)
        dic[year]=movie
    
    with open("task2.json","w+") as f:
        json.dump(dic,f,indent=4)

    return dic

year_=group_by_year(scraped)