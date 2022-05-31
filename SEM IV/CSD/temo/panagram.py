inpt = input()
m=inpt.lower()
j = m.replace(" ","")
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
setalpha = set(alpha)
inptlst = set(str(i) for i in j)
k=inptlst-setalpha
h = setalpha-inptlst
if k ==h:
    print("panagram")
else:
    print("not panagram")