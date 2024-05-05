#a dictionary in python is a collectuon of key value pairs.
# to add new key value pair in dictionary do as follows.
dict={1:1,2:2,3:3}
dict["hello"]="ayush"# this will add a new key value pair in the ditionary. and if the key is already present then it will replace the old value with the new value. 
print(dict)
#removing key value pairs.
# so to remove the key value pair we can use del statement.
#example:=
dict={1:1,2:2,3:3,4:4}
del dict[1]# this will delete the pair.
dict.pop(3)# this can also delete the pair but when thir is no parameter is provided then it will remove the last key value pair.
print(dict)
#a dictionary with similar objects.
#example:=
dict={1:1,2:2,3:1}# we can store same object with diffrent keys but we cant make same keys,if we do then it will change the old one into new pair wit diffrent object.
print(dict[1])
print(dict[3])
# for increasing reability we can assign the parameters in this format=
dic={
    1:1,# this is also correct and it will help is readiblity your code.
    2:3,
    3:3,
}
# if we print any key value pair which is not present,then it will through an error and program will stop their so to prevent that we can use get()method.
print(dict.get("hello"))# it will return none if the key is not present.
# methods in dictionary=
#keys()=it will print all the keys present in the dictionary.
#values()= it will print all the values present in the dictionary.
#items()= it will print both keys and values present in the dictionary.
#looping through all the values in a dictionary.
#example=
dict={
    "ayush":"commerce",
    "rajveer":"bio",
    "puneet":"bio"
}
for dictionary in dict.keys():
    print(f"hello {dictionary} welcome ")
# same we can do it with a values.
for dictionary in dict.values():
    print(f"{dictionary}  ")
# nesting the dictionarys.
#example=
dict1={"color":"red","code":"11"}
dict2={"color":"green","code":"22"}
dict3={"color":"ellow","code":"33"}
dict=dict1,dict2,dict3
print(dict)
#we can use slicing as a range()
#example=
dic=[]
for i in range(10):
    new_dict={"color":"ellow","code":"33"}
    dic.append(new_dict)
for dict in dic[:5]:#here we give range as a slice of a list.
    print(dict)
# we can also make a list in dictionery and also give one key of that list as a range.
#example=
pizza={
    'crust':"thin",
    "topping":["mushroom","pineapple"]
} 

print(f"you have ordered a {pizza['crust']} with the following toppings:")
for toping in pizza["topping"]:
    print(f"\t{toping}")
#making dictionary in a dicitonary.
dict={
    "ayush":{
        "class":"11",
        "sec":"c/commerce"
    },
    "puneet":{
        "class":"11",
        "sec":"b/bio"
    }
}
for username ,user_info in dict.items():
    print(f"\nusername:{username}")
    fullname=f"study in class {user_info['class']} sec {user_info['sec']}"
    print(fullname.title())
#dictonary comparehentions
dict={x:x**x for x in (1,2,3,4,5, 6)}
print(dict)
#more dict comparehentions
dict={x:y for x in (1,2,3) for y in [1,2,3] if x!=y and x<y}
print(dict)
#zip in dict.
c = tuple(zip(['one', 'two', 'three'], [1, 2, 3]))
print(c)