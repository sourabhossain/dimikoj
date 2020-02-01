T = int(input())

for i in range(T):
    n = int(input())
    zero = 0

    while n > 4:
        zero += n // 5
        n //= 5

    print(zero)
