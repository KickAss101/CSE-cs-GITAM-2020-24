class Stack:
    top = -1
    def __init__(self,n):
        self.num = n
    def push(self,n):
        self.top+=1
        self.num[self.top]=n
    def pop(self):
        self.top-=1
    def replace(self,n,a):
        for i in range(self.top+1):
            if self.num[i]==n:
                self.num[i]= a
                
    def display(self):
        for i in range(self.top+1):
            print(self.num[i],end="")
        print()
list = [None]*5   
ref = Stack(list)
ref.push(3)
ref.push(4)
ref.push(5)
ref.push(6)
ref.push(6)
ref.display()
ref.replace(4,0)
ref.display()