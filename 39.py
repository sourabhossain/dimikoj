T = int(input())

for i in range(T):
    n = input()
    
    if n == n[::-1]:
        print("Yes! It is Palindrome!")
    else:
        print("Sorry! It is not Palindrome!")
