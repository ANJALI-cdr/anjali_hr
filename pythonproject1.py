count=0
def quiz(question,option,solution):
   global count
   print(question)
   for key , value in option.items():
      print (f"{key}) {value}") 
   user_option=input("enter the options a/b/c/d:").lower()
   if user_option==solution:
         count+=1
         print("wow!correct answer.")
   else:
         print("wrong, the correct option is:",solution)
quiz("1) Which company developed the Windows operating system?",{'a':'Apple','b':'Google','c':'Microsoft',
        'd':'IBM'},'c')
quiz("2) Which of the following is an operating system?",{'a':'Google','b':'Linux','c':'Intel',
         'd':'Firefox'},'b')
quiz("3)What does HTTP stand for?",{'a':'HyperText Transfer Protocol','b':'HighText Transfer Protocol',
       'c':'HyperText Transmission Protocol','d':'High Transfer Text Protocol'},'b')
quiz("4) Which of the following is used to store data permanently?",{'a':'RAM','b':'ROM','c':'CPU',
      'd':'Cache'},'b')
quiz("5) What does IP stand for in networking?",{'a':'Internal Protocol','b':'Internet Process',
      'c':'Internet Protocol','d':' Input Program'},'b')
print("The score is:",count)
percentage = (count / 5) * 100
print("your percentage:",percentage)
if percentage == 100:
    print("Excellent! You got all questions right.")
elif percentage >= 60:
    print("Good job! You passed.")
else:
    print("Keep practicing. You can do better!")
        



