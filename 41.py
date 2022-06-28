t=int(input("搭了幾次電梯:"))
f= 1
m= 0
if 1<=t<=10:
    for i in range(t):
        b = int(input())
        if b>f:
            m = m + (b-f)*20
        else:
            m= m + (f-b)*10
        f = b

print(m,"元")