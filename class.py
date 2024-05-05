#class is a part of oops(object orienting programimg)
#it makes  life easier of your and other programmers
#creating and using a class.
#creating a dog class
#this is the simple example of how class is prepared 
class dog:
    '''a simple class of a dog'''
    def __init__(self,name,age):#this part is complsery,you always have to give self to run to its own.
        self.name=name
        self.age=age
    def sit(self):
        """giving a order to dog to sit"""#this part is called doc string which tells about the program,and it is not visible when the function is run so its basically like comment but bit diffrent.
        print(f"the {self.name} is now sitting.")
    def bark(self):
        """giving order to dog to bark"""
        print("woof")
dog=dog("tommy","23")#parameter should be given 2 not three because self is use to run the own function so it cannot be taken as a parameters.
dog.sit()
dog.bark()
#instence in class
#also know as variable of a class
#like in above it written dog=dog("tommy","23")
#we can make thousand of inctence with diffrent name and can use it diffrently like we can make the thousand of dogs name and age only using one class.
#it makes it easy to manage lots of data only using one class
#seting a defalt value for an attribute.

class car:
    def __init__(self,name,make,model):
        """intializing the attribute to describe a car"""
        self.name=name
        self.make=make
        self.model=model
        # self.year=year
        self.odometer_reading=0
    def ger_decription(self):
        """return a format info of car"""
        print(f"the name of the car is {self.name} make by {self.make} model no is {self.model} ")
    def odo(self):
        print(f"the car had run around {self.odometer_reading} kilometer")
car=car("miata","mazda","dfak343")
car.odometer_reading="3434"
car.ger_decription()
car.odo()
#inheritence in python
#we make new class from scratch so to save time in building a class we can use parent class function and import them in child class by using super method.
#defing arributes and method for the child
#so for making a child class we need to do this=
#class childclass_name(parent_class):
#   _snip_

#incentences as attributes
# by this we can make large class into smaller classes that work together,this approach is called composition.
class battery:
    """a simple attemt to model a batteru for an electric"""
    def __init__(self,battry_size):
        self.battry_size=battry_size()#this way you can create attribute as an inctence.
    def describe_battery(self):
        print(f"this car has a battery size of{self.battry_size}")
class electric_car(car):
    def __init__(self,name,make,model):
        """inftialize attribute of the parent class then intialize attributes specific to an electric car"""
        super().__init__(self,name,make,model)
        self.battry=battery()