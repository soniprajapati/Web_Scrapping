import json
import os
import requests
from bs4 import BeautifulSoup
import random
import time

f=open("task5.json","r+")
b=json.load(f)
f.close()

def text():
    a=random.randint(1,3)

    for i in b:
        path="/home/admin123/task_9/task.py"+i["movie_name"]+".json"
        if os.path.exists(path):
            pass
        else:
            data=open(path,"w+")
            json.dump(i,data,indent=4)

        #     with open("task9.json","w") as file:
        #         json.dump(path,file,indent=4)

        
        time.sleep(a)

text()


