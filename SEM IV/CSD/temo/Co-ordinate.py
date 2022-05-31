class j:
    def add(self,a,b):
        i = 0
        global c
        self.h = a
        self.n = b
        a = (self.h[i]-self.n[i])
        b = (self.h[i+1]-self.n[i+1])
        c = abs(a)+abs(b)+c       
c= 0
q = [[3,2],[4,-4],[5,0]]
k = j()
for i in range(len(q)-1):
    k.add(q[i],q[i+1])
k.add(q[i],q[len(q)-1])
print(c)

    

        