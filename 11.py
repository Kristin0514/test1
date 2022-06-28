m=int(input("請輸入月份:"))
d=int(input("請輸入日期:"))

if m==1:
    if 21<=d:
        print("Aquarius")
    else:
        print("Capricornus")
elif m==2:
    if 18>=d:
        print("Aquarius")
    else:
        print("Pisces")
elif m==3:
    if 20>=d:
        print("Pisces")
    else:
        print("Aries")
elif m==4:
    if 20>=d:
        print("Aries")
    else:
        print("Taurus")
elif m==5:
    if 21>=d:
        print("Taurus")
    else:
        print("Gemini")
elif m==6:
    if 21>=d:
        print("Gemini")
    else:
        print("Cancer")
elif m==7:
    if 22>=d:
        print("Cancer")
    else:
        print("Leo")
elif m==8:
    if 23>=d:
        print("Leo")
    else:
        print("Virgo")
elif m==9:
    if 23>=d:
        print("Virgo")
    else:
        print("Libra")
elif m==10:
    if 23>=d:
        print("Libra")
    else:
        print("Scorpio")
elif m==11:
    if 22>=d:
        print("Scorpio")
    else:
        print("Sagittarius")
elif m==12:
    if 21>=d:
        print("Sagittarius")
    else:
        print("Capricornus")
