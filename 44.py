a=int(input("請輸入班級數(1<=a<=10):"))
b=0
for i in range(a):
    c=int(input())
    if c >b:
        b=c
print("電腦數量:",b)