class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):#student is a child of person class now student inherits all properties and method of person
    pass
x = Student("Mike", "Olsen")
x.printname()#Mike Olsen
