#list is data sturure which is used to element,where data are seperated by comma and its mutable mean we can be change it.
magician=["alice","david","caroluna"]
for magic in magician:
    print(f"{magic.title()} you have done a great job.")
    print(f"i cant wait to see more,{magic.title()}.\n")
print("thank you everyone thats a great magic show.")
num=list(range(5))# this is a range fuction,if you want to make a list of number,you can convert the results of range()directly into list using list() function.
print(num)
#the below code it written using for loop.
#we can use append function for example.
num=[]
for i in range(5):
    num.append(i)
print(num)
#min and max in list.
#simple statistics.
num=[1,2,3,4,5,6,7]
print(num)
print(min(num))
print(max(num))
print(sum(num))
#list comprehensions.
# to generating list of squares consisted of using three or four line of code.but this make it in one line,,like for exmaple
squre=[i**2 for i in range(1,11)]#this is one line of code for making list consist of squres of numbers 
print(squre)
#for copying a list we use so many mathods like are as follows.
l=[1,2,3,4]
b=l.copy()
print(b)
#or 
l=[1,2,3,4,5]
b=l[:]
print(b)
#using if with multiple list:
toppings_avail=["mashroom","olives","pineapple","green peppers"]
toppings_request=["mashroom","olives","onion","green peppers"]
for i in toppings_request:
    if i in toppings_avail:
        print(f"adding {i}")
    else:
        print(f"sorry {i} is not available.")
print("your pizza is ready")
#exercise:=
current_user=["ayush","kumar","deepak","puneet","rajveer"]
new_user=["madhesiya","kumar","Deepak","Ayush","rajveer"]
for i in range(5):
    if new_user[i].lower() in current_user:
        print(f"sorry {new_user[i]} this name is already been taken.")
    else:
        print(f"{new_user[i]} is not taken and you can name it.")
# always style your statement because it improve readibility of your code.
#we can use slicing as a range()
#example=
dic=[]
for i in range(10):
    new_dict={"color":"ellow","code":"33"}
    dic.append(new_dict)
for dict in dic[:5]:#here we give range as a slice of a list.
    print(dict)
#shortcut of using list.
list=[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y and x+y==5]#this method is given in data structure as list comprehension.
print(list)
#if we write the above list without using list comprehension
#this is how we write
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(combs)
#more in list comprehensions
from math import pi
s=[str(round (pi,i)) for i in range(1,6)]
print(s)
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9],]
x=[[row[i] for row in matrix] for i in range(3)]
print(x)
#if i do it without apply list comprehensions,then i will do it like this. 
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9],]
transposed=[]
for i in range(3):
    transposed_row=[]
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)
#in real world,we should use built in functions to complex flow statements. like zip() function would do a great job for this use case.
x=tuple(zip(*matrix))
print(x)