#if statement is a condition statement which is used to put condition in a program. for example:=
#if statement are of diffrent type:
#simple if,if else,if elif else
car=["audi","bmw","subaru","toyota"]
for i in car:
    if i=='bmw':
        print(i.upper())
    else:
        print(i.title())
#cheaking for cases:
# here are some some funtion which is used to check the case of values:
#==:is for equality
#islower:is for checking wheather the given value is in lower case.
#isupper: is for checking wheather the given value is in upper case
# they all return bollian (either True or False)
#checking whether a value is in a list.
list=["hello","i","am","ayush"]
print("ayush"in list)