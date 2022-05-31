#  program to find the reverese of a number ...
inp_t = "a1b2igh3"
indx_store = []
num_store = []
num_lst = ["1","2","3","4","5","6","7","8","9"]
for i in range(len(inp_t)):
    for j in range(len(inp_t)):
        if inp_t[i]==num_lst[j]:
            indx_store.append(i)
            num_store.append(inp_t[i])
            m =inp_t.replace(inp_t[i],'0')
print(m)

