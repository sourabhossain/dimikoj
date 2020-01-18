import math

T = int(input())

for i in range(T):
    n = int(input())
    x = int(math.sqrt(n))

    if x * x == n:
        print("YES")
    else:
        print("NO")
