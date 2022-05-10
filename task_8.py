# from task_1 import scrap_top_list
# import json
# import os
# import requests

# t1 = scrap_top_list()
# print(t1)

# with open("task5.json", "r") as file:
#     a = json.load(file)
#     print(a)
# def text():
#     for i in a:
#         path = "/home/admin123/task8/task_8.py" + i["Movie_name"] + ".text"
#         # print(path)
#         path = "" + i["movie_name"] + ".text"
#         # print(path)
        
#         if os.path.exists(path):
#             pass
#         else:
#             create = open("/home/admin123/task8/task_8.py" + i["movie_name"] + ".text" , "w")
#             b = open(path, "w")
#             url = requests.get(i["url"])
            
#             create1 = create.write(url.text)
#             create.close()
            
                
# text()

import requests
import os
from task_1 import scrap_top_list
data=scrap_top_list()
movies=data[:10]
def get_scrap_movie_details():            
    for i in movies:
        path="/home/admin123/PYTHON/task_8/task.py"+i["name"]+"text"     
        if os.path.exists(path):
            pass
        else:
            create=open("/home/admin123/PYTHON/task_8/task.py"+i["name"]+"text","w+")
            # create=open(path,"w+")
            url=requests.get(i["url"])
            c=create.write(url.text)
            # create.close()
            
get_scrap_movie_details()