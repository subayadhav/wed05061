import math
a1,b1=map(int,input().split())
c=a1*b1
root = math.sqrt(c)
if int(root + 0.5) ** 2 == c:
    print("yes")
else:
    print("no")
