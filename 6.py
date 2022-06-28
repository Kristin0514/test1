a=str(input("請輸入數值:"))
b=a.split(",")
b.sort()
c=sorted(b,reverse=True)
d=""
e=""
for i in range(0,5):
    d+=str(c[i])
    e+=str(b[i])
    f=int(d)-int(e)
print(f)