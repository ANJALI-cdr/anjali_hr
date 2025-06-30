a=['read','write','sleep','exercise']
b=[]
for i in a:
    status=input(f"the status of {i} is:")
    if status=="done":
       continue
    else:
      b.append(i)
print("pending works:",b)
