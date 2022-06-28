p=int(input("輸入一個數(2<=n<=10):"))
d=[int(input("輸入n個整數(1<=k<=1000):")) for i in range(p)]
for a,b in enumerate(d):
    if b%9==0 or b%11==0:
        print(f"第{a+1}個點 {b}")