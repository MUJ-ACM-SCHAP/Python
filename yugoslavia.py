# printing perfect squares in the range 1 to 500 using for loops

x = range(1,500+1)
import math
for i in x:
    k = math.sqrt(i)
    m = math.floor(k)
    if (k-m==0):
        print(i)
