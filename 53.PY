n=int(input("輸入n值:"))
list= []
for i in range(n):
    a= input("請輸入姓名：")
    e = input("請輸入電子郵件：")
    list.append([a,e])
dict1 = dict(list)
c= input("請輸入查詢電子郵件的姓名：")    
print(c,"電子郵件帳號為",dict1[c])