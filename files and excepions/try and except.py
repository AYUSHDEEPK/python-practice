def fun1():
    try:
        l=[1,2,3,4]
        i=int(input("enter any no"))
        print(l[i])
        return 1
    except :
        print("some error occured")
        
    finally:#this code always run no matter whether the code having error or not.
        print("i always execute")
print("this print wont work in fuction")#this code always run no matter whether the code having error or not but it won't work with function.
x=fun1()
print(x)