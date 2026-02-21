def func(a,b):
    c=a+b
    return c#giving the result using return
print(func(5,3))#8
#Functions can return any data type, including lists, tuples, dictionaries, and more.
def my_function():
  return ["apple", "banana", "cherry"]#we return a list
def my_functionb():
  return (10, 20)#returning a tuple

x, y = my_functionb()
print("x:", x)
print("y:", y)

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])