# A match statement takes an expression and compares its value to successive patterns given as one or more case blocks.
# example
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:# the “variable name” _ acts as a wildcard and never fails to match. If no case matches, none of the branches is executed.
            return "Something's wrong with the internet"
        
def http(statuss):
    match statuss:
       case 401 | 403 | 404:#You can combine several literals in a single pattern using | (“or”):
         return "Not allowed"

print(http(401))
#if we are using class to structure  data then we can use the class mane followed by an argument list resembling a constructor.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
c=Point(1,5)
where_is(c)
# We can add an if clause to a pattern, known as a “guard”. If the guard is false, match goes on to try the next case block. 
# match point:
#     case Point(x, y) if x == y:
#         print(f"Y=X at {x}")
#     case Point(x, y):
#         print(f"Not on the diagonal")
print(1 + 3j)