import sys
import math
''' 
    Дискримина́нт многочлена
    Polynomial discriminator
'''

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

# D = b^2 - 4 * a * c

D = (b ** 2) - (4 * a * c)


x_1 = int((-b + math.sqrt(D)) / (2 * a))
x_2 = int((-b - math.sqrt(D)) / (2 * a))
print(x_1)
print(x_2)