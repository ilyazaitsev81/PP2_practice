import math
n=int(input())
isprime=True
nums=list(map(int,input().split()))
for i in range(n):
    for j in range(2,int(math.sqrt(nums[i]))):
        if nums[i]%j==0:
            isprime=False
    if isprime:
        print(nums[i])
    isprime=True