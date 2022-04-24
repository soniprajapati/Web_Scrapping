from  task_2 import*

dec_arg= group_by_year(scraped)
moviedec={}
list1=[]

def group_by_decade(movies):
    moviedec={}
    list1=[]
    for index in movies:#years
        mod=index%10#mod=3
        decade=index-mod#decade 1970
        if decade not in list1:
            list1.append(decade)#it is creating list of decades

    list1.sort()
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10=i+9#dec10=1959
        for x in movies:
            if x <=dec10 and x >=i:#dec10=e.g 1959 or i =1950
                for v in movies[x]:
                    moviedec[i].append(v)


    with open("task3.json","w+") as f:
        json.dump(moviedec,f,indent=4)

    
    return(moviedec)
print(group_by_decade(dec_arg))