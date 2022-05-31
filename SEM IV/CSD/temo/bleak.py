inpt = int(input())
list = []
count = 0
p=0
for i in range(inpt):
    binary = format(i,"b")
    count = binary.count("1")
    sum = i+count
    list.append(sum)
for i in range(len(list)):
    if inpt==list[i]:
        p+=1
        break
if p>0:
    print("not bleak")
else:
    print("its bleak")