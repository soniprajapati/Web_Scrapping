import json
from task_5 import get_movie_list_details

# movie_d=get_movie_list_details

with open("task5.json","r") as f:
    a=json.load(f)

def analyse_movies_genre():
    dic={}
    for i  in a:
        # print(i)
        if "Genre" in i:
            Genre=i["Genre"]
            # print(Genre)
            for i in Genre:
                if i not in dic:
                    dic[i]=1
                else:
                    dic[i]+=1


    with open("task11.json","w") as file:
        json.dump(dic,file,indent=4)      

movie_genra=analyse_movies_genre()
print(movie_genra)
