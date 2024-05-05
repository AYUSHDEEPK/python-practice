import random
x="hello welcome to the rock papper siccour game"
print(x.center(130))
print("""                                  as everyone know what is rock,paper and sissour so there is no need of telling the rules 
The compition will be in between you and computer""")
print("""1 is for rock.
2 is for paper.
3 is for sissour""")
user=int(input("enter thr from the folllowing option given above: "))
if user>3 or user<1:
   raise ValueError
comp=random.randint(1,3)
print("the comp choice is ",comp)
for i in range(1,4):
   if user==i and comp==i:
      print("match draw")
if user==1 and comp==2:
   print("computer wins")   
elif user==1 and comp==3:
   print("congrats you won")
elif user==2 and comp==1:
   print("congrats you won")   
elif user==2 and comp==3:
   print("computer wins")
elif user==3 and comp==1:
   print("computer wins")   
elif user==3 and comp==2:
   print("congrats you won")

x=input("did you like the game write (yes or no)")
y=x.lower()
if y=="yes":
   print("thanks for your feedback.")
elif y=="no":
   print("sorry for the problem we will try to improve this game,thank you.")
elif y=="":
   print(x)
