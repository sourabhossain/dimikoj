cnt = 0

for i in range(1000, 0, -1):
    print(str(i) + "\t", end = "")
    
    cnt += 1
    
    if(cnt == 5):
        print()
        cnt = 0
