from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10]
l2=list(map(lambda x: x**2,l))
print(l2)
l3=list(filter(lambda x: x%2==0,l))
print(l3)
num=reduce(lambda x,y:x+y,l)
print(num)