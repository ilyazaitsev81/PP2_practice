#we can override inherited method
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname,course):
    super().__init__(fname, lname)#inherit parent init method
    self.course=course
  def printname(self):
    print(f"hello: {self.firstname} {self.lastname}, you are a {self.course} year student")#overriding method
Ilya=Student("Ilya","Zaitsev",1)
p1=Person("NN","nn")
Ilya.printname()#inherited method was overrided so it print out another string
p1.printname()