#here we are going to make fibonachi
#i will do by both loop and while.
def fib(n):
    a=0
    b=1
    for i in range(0,n):
        a,b=b,a+b
        print(a)
def fibo(m):
    n=0
    a,b=0,1
    while n<=m:
        print(a,end=" ")
        a,b=b,a+b
        n+=1
    print()

# Note: For efficiency reasons, each module is only imported once per interpreter session. Therefore, if you change your modules, you must restart the interpreter – or, if it’s just one module you want to test interactively, use importlib.reload(), e.g. import importlib; importlib.reload(modulename).