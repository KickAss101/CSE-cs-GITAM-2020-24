X = int(input("enter length of intervals:"))
j = []
c=[]
k = []
q = []
d=[]
for i in range(X):
    a = list(map(int,input("enter two numbers of a interval : ").split()))
    j.append(a)
    for i in range(len(a)):
        c.append(a[i])
for i in range(len(c)):
    for j in range(i+1,len(c)):
        if c[i]==c[j]:
            k.append(c[i])
        m =set(k)
        b = list(m)
for i in range(len(b)):
    cot = c.count(b[i])
    q.append(cot)
for i in range(len(q)):
    j = q[i]+q[i]
    d.append(j)
s= sum(d)
if s==len(c):
    print("the number of pins required is :  ",len(q))
else:
    if s==0:
        z = len(c)-s
        a= z//2
        print("number of pins required is :",a)
    else:
        z = len(c)-s
        a= z/2
        print("the number of pins required is",a+1)
