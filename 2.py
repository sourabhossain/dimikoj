T = int(input())

for i in range(T):
    n = input()

    if int(n[len(n) - 1]) % 2 == 0:
        print("even")
    else:
        print("odd")
