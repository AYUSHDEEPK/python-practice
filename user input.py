# user input in python
# the first way is=
inpt=input("enter your name and in will print it:")# it only return string.
print(inpt)
#another methods is=
prompt ="what is your name"
name=input(prompt)# this can also make a input using another veriable.
#we can use int in it for numerical input
# exercise=
number=int(input("enter a no between 1 to 10: "))
if number>0 and number<10:
    if 10%number==0:
        print("yes it is a multiple of 10 ")
    else:
        print("no this no. is not divisible by 10 ")
#exercise 2=
cars="""hello welcome to car rental we have no. of car to rent here are the list of cars
1. subaru             2.toyota corola
3. mustang            4.bmw s-class"""
print(cars)
rental_car= input("which one you like to rent=")
if rental_car=="1":
    print("so its a subaru twin turbo supercharge having 400hp with 300nm torque it a good choice for racing on street tracks. it will cost you around 200dollar per day")
if rental_car=="2":
    print("so its a toyota corola model 2012, its is fuel efficiant and good in long run this will cost you around 50 dollar a day")
if rental_car=="3":
    print("its a mustand model 1957 it a clasic version and the most famous of all time it will cost you around 300 dolloar a day")
if rental_car=="4":
    print("its a most advance car in our collection its has a self driving feature which give a imersive experience to the user and it also an electric so no gas prices, so it will cost you around 500 dollar a day")
choice=input("have you decided sir:")
if choice=="yes":
    print('okay sir here is your key, have a nice day sir.')