class emp:
    def __init__(self,first_name,last_name,annual_salary):
        self.first_name=first_name
        self.last_name=last_name
        self.annual_salary=annual_salary
    def give_raise(self,amount):
        self.annual_salary+=amount
        return self.annual_salary
    def result(self):
        print(f"{self.first_name} {self.last_name},{self.annual_salary},{self.give_raise}")
