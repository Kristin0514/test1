c=int(input("國文:"))
e=int(input("英文:"))
m=int(input("微積分:"))
p=int(input("體育:"))
pr=int(input("程式設計:"))
avr=(c+e+m+p+pr)/5
print("平均分數",avr)
print("最高分數:",max(c,e,m,p,pr))
print("最低分數:",min(c,e,m,p,pr))

