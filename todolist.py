L={'read':'pending','write':'pending','sleep':'done','exercise':'done'}
for key,value in L.items():
   status = input(f"enter the status of the task  {key}:" )
   L[key]=status
while True:
   a=input('any other tasks (yes/no)?')
   if a=='yes':
      L['dance']='under progress'
   else:
      print("Thats fine")
      break
print("The status of task are:",L)

