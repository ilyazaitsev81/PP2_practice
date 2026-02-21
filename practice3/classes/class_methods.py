#Methods are functions that belong to a class. They define the behavior of objects created from the class.
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def happy_birthsay(self):#method that changes property value
        self.age+=1
        print(f"happy birthday. Now you are {self.age} yeas old")
    def __str__(self):#The __str__() method is a special method that controls what is returned when the object is printed
        return f"Name: {self.name}, age:{self.age}"
    def greeting(self):#usual method
        print(f"hello, {self.name}")
Ilya=person("Ilya",18)
Ilya.greeting()#hello, Ilya
print(Ilya.age)#18
Ilya.happy_birthsay()#happy birthday. Now you are 19 yeas old
print(Ilya.age)#19
print(Ilya)#Name: Ilya, age:19
del person.greeting#deletes method