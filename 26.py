s=str(input("請輸入需要檢測的字串(end 結束):"))
a=str(input("請輸入檢測的單一字元:"))

if s=="end":
    print("檢測結束!")
else:
    print("字元",a,"出現次數為:",s.count(a))