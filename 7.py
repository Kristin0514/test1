s=int(input("請輸入月租費形式(186,386,586,986):"))
t=int(input("請輸入通話時間:"))
if s==186:
    if (t*0.09)<=372:
        print("通話費:",round(t*0.09*0.9))
    else:
        print("通話費:",round(t*0.09*0.8))
elif s==386:
    if (t*0.09)<=772:
        print("通話費:",round(t*0.08*0.8))
    else :
        print("通話費:",round(t*0.08*0.7))
elif s==586:
    if (t*0.09)<=1172:
        print("通話費:",round(t*0.07*0.7))
    else:
        print("通話費:",round(t*0.07*0.6))
elif s==986:
    if (t*0.09)<=1972:
        print("通話費:",round(t*0.06*0.6))
    else:
        print("通話費:",round(t*0.06*0.5))