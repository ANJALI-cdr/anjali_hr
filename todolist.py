a=['read','write','sleep','exercise']
for i in a:
    b=input(f"the status of {i} is:")
    if b=="done":
       a.remove(i)
print(a) 