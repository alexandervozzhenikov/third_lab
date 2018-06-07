import math
n = int(input("Кол-во элементов в последовательности n="))
z = 0
x = 0
for i in range(1, n+1):
    if i % 2 == 0:
        z = z+i**2
    else:
         x = x+i**3
print('сумма квадратов чётных элементов:', z)
print('сумма кубов не четных элементов:', x)
print('общая сумма z+x =', z+x)
