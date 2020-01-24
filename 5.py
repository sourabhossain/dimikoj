T = int(input())

for i in range(T):
    n = int(input())

    for j in range(n):
        for k in range(n):
            print("*", end="")
        print("")

    if i + 1 < T:
        print("")
