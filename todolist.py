L={'read':'pending','write':'pending','sleep':'done','exercise':'done'}
for key,value in L.items():
   status = input(f"enter the status of the task  {key}:" )
   L[key]=status
while True:
   a=input('any other tasks (yes/no)?')
   if a=='yes':
      task=input(" enter the task:")
      b=input("enter the status:")
      L[task]=b
   elif a=='no':
      print("Thats fine")
      break
   else:
      print('invalid input')
      continue
for key, value in L.items():
   print(f"{key} : {value}")
#print("The status of task are:",L)

