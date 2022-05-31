class j:
    def add(self,a,b):
        i = 0
        l=[]
        global v
        self.h = a
        self.n = b
        a = self.h[i]-self.h[i+1]
        b = self.n[i]-self.n[i+1]
        c = self.h[i]-self.n[i]
        d = self.h[i+1]-self.n[i+1]
        e = self.h[i]-self.n[i+1]
        f =self.h[i+1]-self.n[i]
        k = [abs(a),abs(b),abs(c),abs(d),abs(e),abs(f)]
        v= min(k)      
v= 0
q = [[10,20],[25,100]]
k = j()
for i in range(len(q)-1):
    k.add(q[i],q[i+1])
print(v)



