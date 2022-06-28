f=int(input("請輸入計算方式(1=keys&values、2=items):"))
a=int(input("輸入比數:"))
b=int(input("金"))
c=int(input("銀"))
d=int(input("銅"))
e=int(input("優"))
medals={"金":b,"銀":c,"銅":d,"優":e}
item=medals.items()
if f==1:
    print(medals)
else:
    for n,m in item:
        print('%s牌得到%d面' % (n,m))
