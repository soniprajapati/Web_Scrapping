from task_4 import movies_detailes
from task_12 import scrape_movie_cast
import json
l=[]
url="https://www.rottentomatoes.com/m/toy_story_4"

def scrape_cast():
    details= movies_detailes(url)
    cast=scrape_movie_cast(url)
    details["cast"]=cast
    l.append(details)
    with open("task13.json","w") as f1:
        json.dump(l,f1,indent=4)
scrape_cast()