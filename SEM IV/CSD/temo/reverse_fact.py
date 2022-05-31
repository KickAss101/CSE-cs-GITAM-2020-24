num = int(input())
div = 1
for i in range(2,num):
    div = num/i
    num = div
    if div ==1:
        print(i)
    elif div<1:
        print("no reverse factorial")