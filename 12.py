a=str(input("請輸入一整數數列:"))
b=a.split(" ")
for i in range(0,len(b)):
    if int(b.count(b[i]))>len(b)/2:
        a=int(b[i])
        print("過半元素為:",a)
        break
    else:
        print("過半元素為:No")
        break
