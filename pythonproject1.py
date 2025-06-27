count=0
i=0
while i<2:
    print("national animal of india is?")
    a=input("the national animal of india is:")
    b=a.lower()
    if b=='tiger':
        count+=1
    i+=1
    print("national bird of india is?")
    c=input("the national bird of india is:")
    d=c.lower()
    if c=='peacock':
        count+=1
    i+=1
        
print("total score is:",count)
