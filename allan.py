import random

def gamble():
     options=["rock","paper","scissors"]
     count=1
     while count<=3:
       random_rps=random.choice(options)
       count+=1
       user_input=input("choose rock, paper, scissors?")
       if random_rps==user_input:
          print(f"AI CHOICE: {random_rps}  YOUR CHOICE: {user_input}")
          print("ITS A DRAW")
       elif (random_rps=="rock" and user_input=="scissors") or (random_rps=="scissors" and user_input=="paper") or (random_rps=="paper" and user_input=="rock"):
            print(f"AI CHOICE: {random_rps}  YOUR CHOICE: {user_input}")
            print("AI WON THIS ROUND ^_^ ")
            
       elif  (random_rps=="scissors" and user_input=="rock") or (random_rps=="paper" and user_input=="scissors") or (random_rps=="rock" and user_input=="paper"):
             print(f"AI CHOICE: {random_rps}  YOUR CHOICE: {user_input}")
             print(f"{name_input} WON THIS ROUND $$$")
            
       else:
           print("INVALID CHOICE!!!")

name_input=input("enter your name: ")
age_input=input("enter your age: ")
age=int(age_input)
tries=3
if age>=18:
    print("adult")
    print("play rock paper scissors")
    gamble()
else:
    print("minor")
