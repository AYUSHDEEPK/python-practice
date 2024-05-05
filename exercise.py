# squre=[i**2 for i in range(1,11)]
# print(squre)

# current_user=["ayush","kumar","deepak","puneet","rajveer"]
# new_user=["madhesiya","kumar","Deepak","Ayush","rajveer"]
# for i in range(5):
#     if new_user[i].lower() in current_user:
#         print(f"sorry {new_user[i]} this name is already been taken.")
#     else:
#         print(f"{new_user[i]} is not taken and you can name it.")
#updating tuple although its unmutable
# buffet=("dal","chawal","sabji","rayta")
# for j in buffet:
#     print(j)
# list=list(buffet)
# list[3]="chokha"
# buffet=tuple(list)
# for i in buffet:
#     print(i)
numbers=[1,2,1,2,1,2,1,2,1,2,1,2,1]
while 1 in numbers:
    numbers.remove(1)
print(numbers)