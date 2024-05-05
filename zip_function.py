# Zip is an in-built function in Python used to iterate over multiple iterables. It takes corresponding elements from all the iterable passed to it and merges them in a tuple.
for i in zip(range(10),(1,2,3,4,5)):#if one item is less than another than it do not through error what it do is that it run till one of the them is run out of value.
    print(i)
print(type(i))#it always return in tuple.
#strict in zip
x=list(zip(('a', 'b', 'c'), (1, 2, 3), strict=True))#be using strict it enable the python to through error when one of any one of itereable in long than another
print(x)
x = [1, 2, 3]
y = [4, 5, 6]
z=list(zip(x, y))
print(z)
x2, y2 = zip(*zip(x, y))#this is used to inzip the list.
print(x2,y2)
x == list(x2) and y == list(y2)

x=[1,2,3,4,5]
y=[5,6,7,8,8]
z=dict(zip(x,y))
a,b=zip(*zip(x,y))#like in above this is also use to unzip the list.
print(a,b)
print(z)