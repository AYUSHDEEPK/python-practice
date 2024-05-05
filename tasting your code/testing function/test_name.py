#this is a example of testing code.
#note: always make sure the folder name should start with test_,pytest only read a file which have name start with test_
from name import format_name
def test_first_last_name():
    '''do names like ayush deepak'''
    formated_name=format_name("ayush","deepak")
    assert formated_name =="Ayush Deepak"
    #if the get error like if the user write middle name also then we should repair and made the like if the user write the middle name then also or if not then also it print the output.
# print("Enter 'q' at any time to quit.")
# while True:
#     first= input("\nPlease give me a first name: ")
#     if first == 'q':
#         break
#     last = input("Please give me a last name: ")
#     if last == 'q':
#         break
#     formated_name=format_name(first,last)
# print( formated_name)