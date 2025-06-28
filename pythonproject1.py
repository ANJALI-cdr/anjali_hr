count=0
i=0
while i<6:
#quesion1
    print("Which company developed the Windows operating system?")
    o={'a':' Apple','b':'Google','c':'Microsoft','d':'IBM'}
    for key,value in o.items():
        print (f"{key}) {value}")
    user_choice = input("enter the options a/b/c/d:")
    if o[user_choice]=='Microsoft':
         count+=1
    i+=1
#question 2
    print("Which of the following is an operating syste?")
    o={'a':' Google','b':'Linux','c':'Intel','d':'Firefox'}
    for key,value in o.items():
        print (f"{key}) {value}")
    user_choice = input("enter the options a/b/c/d:")
    if o[user_choice]=='Linux':
         count+=1
    i+=1
#question3
    print("What does HTTP stand for?")
    o={'a':'HyperText Transfer Protocol','b':'HighText Transfer Protocol',
       'c':'HyperText Transmission Protocol','d':'High Transfer Text Protocol'}
    for key,value in o.items():
        print (f"{key}) {value}")
    user_choice = input("enter the options a/b/c/d:")
    if o[user_choice]=='HyperText Transfer Protocol':
         count+=1
    i+=1
#question4
    print("Which of the following is used to store data permanently?")
    o={'a':'RAM','b':'ROM','c':' CPU','d':' Cache'}
    for key,value in o.items():
        print (f"{key}) {value}")
    user_choice = input("enter the options a/b/c/d:")
    if o[user_choice]=='ROM':
         count+=1
    i+=1
#question5
    print("What does IP stand for in networking?")
    o={'a':'Internal Protocol','b':'Internet Process','c':'Internet Protocol','d':' Input Program'}
    for key,value in o.items():
        print (f"{key}) {value}")
    user_choice = input("enter the options a/b/c/d:")
    if o[user_choice]=='Internet Protocol':
         count+=1
    i+=1
print("total score is:",count)
