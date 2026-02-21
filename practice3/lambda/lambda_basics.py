#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
#lambda syntax: lambda args: expression
x = lambda a : a + 10
print(x(5))#15
x = lambda a, b : a * b
print(x(5, 6))#30