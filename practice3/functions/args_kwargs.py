#By default, a function must be called with the correct number of arguments.
#but *args and **kwargs allow functions to accept a unknown number of arguments.

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
#using *args we can give as mush arguments as we want. Fucntion ill recieve them as tuple
#we can use *args with usual parameters
def my_functionb(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")#usual parameters must come first
'''result:
Hello Emil
Hello Tobias
Hello Linus
'''
#If you do not know how many keyword arguments will be passed into your function
#  add two asterisks ** before the parameter name.
def kwargs_example(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

kwargs_example(name = "Tobias", age = 30, city = "Bergen")#function recievse our key-values as dictionary
'''result
Type: <class 'dict'>
Name: Tobias
Age: 30
All data: {'name': 'Tobias', 'age': 30, 'city': 'Bergen'}
'''
#we can use ordinary argumens with kwargs. usul parameters must be first
#we can unpack args
def args_unpack(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = args_unpack(*numbers) # Same as: my_function(1, 2, 3)
print(result)
#we can unpack kwargs
def kwargs_unpack(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
kwargs_unpack(**person) # Same as: my_function(fname="Emil", lname="Refsnes")