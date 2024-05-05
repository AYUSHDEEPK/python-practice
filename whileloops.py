#while loop is totaly diffrent from for.while does not need range it can run as long as conditon is true.
#using flag in while 
promt="tell me somthing and i will repat it for you: "
active=True
while active:
    message=input(promt)
    if message=="quit":
       active=False
    else:
        print(message)
# we can also use break statement to jump out the loop
# use of continue statement 
current_no=0
while current_no<10:
    current_no+=1
    if current_no %2 ==0:
        continue
    print(current_no)
# moving  iteams form one list to another using while.
unconfirmed_user=["ayush","puneet","rajveer"]
cunfirmed_user=[]
while unconfirmed_user:
    current_user=unconfirmed_user.pop()
    print(f"verifying user {current_user.title()}")
    cunfirmed_user.append(current_user)
print("the following user has been confirmed here is the list:")
for confirm in cunfirmed_user:
    print(confirm)
# removing all instances of spcific value from the list:
numbers=[1,2,1,2,1,2,1,2,1,2,1,2,1]
while 1 in numbers:
    numbers.remove(1)
print(numbers)
# more example
number=[1,2,3,4,5,6]
while number:
    number.pop()
    print(number)
# while loop using dictionery:
responses={}
poling_active=True
while poling_active:
    name=input("what is your name")
    response=input("what do you to do in your free time.")
    responses[name]=response
    repeat=input("would you like another person to respond: ")
    if repeat=="no":
        poling_active=False
print("\t--poll result--")
for name,response in responses.items():
    print(f"{name} would you like to {response}")