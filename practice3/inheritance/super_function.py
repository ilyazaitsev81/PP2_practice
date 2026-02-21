#Python also has a super() function that will make the child class inherit all the methods and properties from its parent
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
    super().printname()
    print(self.course)
s1=Student("Ilya","Zaitsev",1)#create student object
s1.printname()