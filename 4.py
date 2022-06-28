from cmath import sqrt


x=int(input("X軸座標:"))
y=int(input("Y軸座標:"))

if x>0 and y>0:
    print("該點位於第一象限,離原點距離為"+str(sqrt(pow(x,2)+pow(y,2))))
elif x<0 and y>0:
    print("該點位於第二象限,離原點距離為"+str(sqrt(pow(x,2)+pow(y,2))))
elif x<0 and y<0:
    print("該點位於第三象限,離原點距離為"+str(sqrt(pow(x,2)+pow(y,2))))
else:
    print("該點位於第四象限,離原點距離為"+str(sqrt(pow(x,2)+pow(y,2))))

