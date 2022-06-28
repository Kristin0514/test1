from numpy import intp


a=int(input("請輸入一正整數(11<=n<=1000):"))
if a%2==0 and a%11==0 and a%5!=0 and a%7!=0:
    print("Yes")
else:
    print("No")