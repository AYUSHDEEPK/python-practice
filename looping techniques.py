
#uses of iteams() in loop
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
#uses of enumerate().this function is used to print the loop along with its positional indexing
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
#using loop over two or more sequences at the same time
#it can be done with zip()function
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
#using reversed loop.
for i in reversed(range(1, 10)):
    print(i)
for j in range(10,0,-1):
    print(j)
#both code on above can print in reverse.
#now for shorted()function 
#what sorted do is it return a new sorted list while leaving the source unaltered.
# example
basket=[1,3,2,4,5,7,6,8,7,9]
for i in sorted(basket):
    print(i,end="")
print(basket)
#we can use set() on a sequence which removes the multi element.
#we can use sorted with set in a loop
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
# It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filter_data = []
for value in raw_data:
    if not math.isnan(value):
        filter_data.append(value)
print(filter_data)
#the above code basically do is that it return append the values which is not 'nan' and then in new list and after that it print the the new list which do not have the nan value.
#more on conditions
# The conditions used in while and if statements can contain any operators, not just comparisons.

# The comparison operators in and not in are membership tests that determine whether a value is in (or not in) a container. The operators is and is not compare whether two objects are really the same object. All comparison operators have the same priority, which is lower than that of all numerical operators.
print((1, 3, 3) < (7, 2, 4))
print([4, 2, 3] > [1, 2, 4])
print('ABC' < 'C' < 'Pascal' < 'Python')
print((1, 2, 3, 4) < (1, 2, 4))
print((1, 2) < (1, 2, -1))
print((1, 2, 3) == (1.0, 2.0, 3.0))
print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))