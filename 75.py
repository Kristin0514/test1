a=0
while a>=0:
    b=input("請輸入事項(若已無事項,請輸入end):")
    a+=1
    if b=="end":
        break
    else:
        print(a,".",b)