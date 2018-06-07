import math
n = int(input("n="))
p = 1
for k in range(1,n):
    p = p+((-1)**k*(k-7))/2*(math.factorial(n-k))
print(p)
