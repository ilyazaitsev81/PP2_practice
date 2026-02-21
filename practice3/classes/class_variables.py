#Properties are variables that belong to a class. They store data for each object created from the class.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(p1.age)#printing property

p1.age = 26#modify property
print(p1.age)
del p1.age#deliting variable
p1.city="Almaty"#adding new property
print(p1.city)