import math
a = float(input())
b = float(input())
c = float(input())
if a == 0:
    if b == 0:
        print("Phuong trinh vo nghiem")
    else:
        print("Phuong trinh co 1 nghiem x = ", -c/b)
delta = b*b - 4*a*c
if delta >0:
    x1 = (float)((-b + math.sqrt(delta))/(2*a));
    x2 = (float)((-b - math.sqrt(delta))/(2*a));
    print("Phuong trinh co 2 nghiem x1 = ", x1, "va x2 = ", x2)
elif delta ==0:
    x1 = x2 = -b/(2*a)
    print("Phuong trinh co nghiem kep x1 = x2 = ", x1)
else:
    print("Phuong trinh vo nghiem")