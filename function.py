#funtion in python are the block of code which return the specific task is given as a prameter it only run when it call.
#it is a user defined function.
#example=
def greet_user(username):# in paralthisis username is goven for function to accept any one argument specify 
    print(f"hello, {username}")
    username="hello"
greet_user("ayush")
# arguments and parameter can be interchangeble.
#function can we use multiple time.by changing diffrent parameters everytime.
#order always matter while giving arguments.

# default arguments
def naam(fname="", mname="kumar", lname="deepak"):
    print("hello", fname,mname, lname)
naam("ayush")
#we can call define a argument in a diffrent way while calling them for example.
#keyword argument=in above call we directly directly give the parameter but we can also use like 
#naam(fname="ayush")

# required arguments
def name(fname, mname, lname):
    print("hello", fname, mname, lname)
name("ayush", "kumar", "")

# arbitrary arguments
def nam(*name):
    print("hello",name[2],name[1],name[0])
nam("deepak","kumar","ayush")
#return value in a diffrent way.
# a fuction does not always have to display its output directily instead it can be prosess some data and then return a value or set of values.
def name(first_name,middle_name,last_name):
    '''return a full name,neatly formated.'''
    full_name=f"hello {first_name} {middle_name} {last_name}"
    return full_name.title()
coder=name("ayush","kumar","deepak")
print(coder)
#sometimes we dont need a middle name or last name so for that we can write a fuction like this.
def naam(first_name,last_name,middle_name):
    """return a full name ,neatly formated"""
    print("hello",first_name[0],middle_name[1],last_name[2])
print("ayush")#even if you pass empty parameter then also it wont give error,you can only give your first parameter also.
#or 
def nam(first_name,last_name,middle_name=""):
    if middle_name:
        full_name=f"{first_name} {middle_name} {last_name}"
    else:
        full_name=f"{first_name} {last_name}"
    print(full_name.title())
nam("ayush","deeapk","kumar")#here middle name is optional.
#returning a dictionary
def built(first_name,last_name):
    person={f"""first_name:{first_name},"last_name":{last_name}"""}
    print(person)
built("ayush","deepak")
#using function with while loop.
def format_name(first_name,last_name):
    full_name=f"{first_name} {last_name}"
    print(full_name)
active=True
while active:
    print("please tell me your name")
    f_name=input("first name: ")
    l_name=input("last name: ")
    repeat=input("do want others to say their name:")
    if repeat!="yes":
        active=False
    format=format_name(f_name,l_name)
print(format)
#passing a list using list.
#we can also pass list using function.
def greet_user(names):
    """"print a single greeting to each user in the list."""
    for name in names:
        msg=f"hello {name.title()}"
        print(msg)
username=["ayush","kumar","rajveer"]
greet_user(username)
#modifying a list in a function.
#lets start with some design that neeeded to be printed

def design(unprinted_design,completed_design):
    orignal=unprinted_design[:]
    while unprinted_design:
        current_design=unprinted_design.pop()
        print(f"printing models are:",current_design)
        completed_design.append(current_design)
    print("\nThe following models have been printed")
    for complete in completed_design:
        print(complete)
    # print("this is the orignal list",orignal)
design(["phone case","robot print","dore dore"],[])
#arbitrary number.
# by using argument in function with starting "*" star symbol, we can give multiple parameters using one variable.
