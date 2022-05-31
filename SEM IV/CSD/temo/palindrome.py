
def palindrome(n):
    reverse = 0
    x = n
    while n > 0: 
        digit = n % 10
        reverse = reverse * 10 + digit 
        n = n // 10
    if x==reverse:
        print(reverse)
    else:
        d = x+reverse
        palindrome(d)
o = int(input("enter a number :"))      
n = palindrome(o)


    