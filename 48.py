n=int(input("輸入筆數:"))
a=dict()
for i in range(n):
    b=input()
    c=b.split()
    a[c[0]]=c[1]
d=input("輸入欲查詢單字:")
if d in a:
    print(d,"的中文意思為",a.get(d))