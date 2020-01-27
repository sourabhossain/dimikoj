T = int(input())

for i in range(1, T + 1):
    a, b, c = map(int, input().split())
    
    if a > b:
        a, b = b, a
    
    if a > c:
        a, c = c, a
    
    if b > c:
        b, c = c, b
    
    print("Case " + str(i) + ": " + str(a) + " "+ str(b) + " " + str(c))
