import json
from bs4 import BeautifulSoup
with open("task5.json","r")as file:
    a=json.load(file)
    # print(a)
def movies_langusge():
    dict={}
    for i in a:
        # print(i)
        if "Language" in i:
            language=i["Language"]
            # print(language)
            for i in language:
                if i not in dict:
                    dict[i]=1
                else:
                    dict[i]+=1
    with open ("task6.json", "w+") as file:
        json.dump(dict,file, indent=4)
    # return list
movies_langusge()