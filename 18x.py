p=input("請輸入五張牌1~K(A,J,Q,K):")
sum=0
for i in range(5):
    if p[i]=="A":
        sum=sum+1
    elif p[i]=="J":
        sum=sum+11
    elif p[i]=="Q":
        sum=sum+12
    elif p[i]=="K":
        sum=sum+13
    else:
        sum=sum+int(p[i])
print(sum)