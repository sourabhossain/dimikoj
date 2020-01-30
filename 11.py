import math

T = int(input())

for i in range(T):
    n = int(input())
    result = 1
    
    while n > 1:
        result *= n
        n -= 1
    
    print(result)
