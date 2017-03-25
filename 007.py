#Import math for sqrt function E29
from math import sqrt

x = 10001
p = [2]
n = 3

while (len(p) < x):
    div = 3
    i = 1
    limit = sqrt(n)+1
    isPrime = True
    while (div < limit):
        if n%div == 0:
            isPrime = False
            div = limit
        else:
            div += 2
    if isPrime == True:
        p.append(n)
    n += 2
print p[len(p)-1];
