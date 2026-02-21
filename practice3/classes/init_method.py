#The __init__() method is used to assign values to object properties
#, or to perform operations that are necessary when the object is being created
class person:
    def __init__(self,name,age):#init fucntion that gives name and age to objects when we create it
        self.name=name
        self.age=age
person1=person("Ilya",18)
print(person1.name)
print(person1.age)
