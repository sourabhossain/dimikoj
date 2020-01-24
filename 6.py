T = int(input())

while T > 0:
    n = int(input())
    print("Sum =", (n // 10000) + (n % 10))
    T -= 1
