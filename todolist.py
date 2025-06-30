L={'read':'pending','write':'pending','sleep':'done','exercise':'done'}
for key,value in L.items():
   status = input(f"enter the status of the task  {key}:" )
   L[key]=status
print("The status of task are:",L)

