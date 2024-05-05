#set in python.it also a data type 
#set is a unordered colloection with no duplucate elementes 
#basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
#it use with curly braces{}
#demonstration
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
#the above code is bac=sic one now some cool thing about set
# Demonstrate set operations on unique letters from two words
a=set("hellzo")
b=set("heilllo")
print(a)
print(b)
#now some example with unique character because it support unique charater
print(a-b)#it used to print the which is present in a but not in b.
print(a|b)#print those letters which are present in both a or b or both 
print(a&b)#it print the letter whiich are present in both a and b
print(a^b)# it used to print the letter which are in a or b but not in both 
#set comparehensions
a = {(x,x**x)for x in [1,2,3,4,5]}
print(a)