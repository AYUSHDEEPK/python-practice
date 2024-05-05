#contacts list 
#so to make this, we want to put several specs like add the contact,search the contact,delete a contact.
#so here it begin
class contact_list:
    def __init__(self,name):
        self.dic={}
        self.name=name
        print(f'hello {self.name}')
    def add(self,name,number):
        self.dic[name]=number
    def search(self,name):
        self.name=name
        for key in self.dic.keys():
            if key==name:
                print("already present")
            elif key!=name:
                print("it is not present")
                # a=input("do you want to put it in contact list? ")
                # if a=="yes":
                #     nam=input("nam? ")
                #     no=int(input("enter number "))
                #     self.dic[nam]=no
    def delete(self,name):
        self.name=name
        self.dic.pop(self.name)
    def contact_list(self):
        for item in self.dic.items():
            print(item)
a=contact_list("ayush")
a.add("papa",8299672112)
a.add("mummy",8090191219)
a.add("niraj",7457983927)
a.search("niraj")
# a.delete(") 
a.contact_list()
#completed








