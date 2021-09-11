print("Nhap so nguyen a: ")
a = int(input())
flag = True
if a < 2:
    flag = False
elif a == 2:
    flag = True
else:
    for i in range(2, a, 2):
        if a%i == 0:
            flag = false
if flag == True:
    print(a, "la so nguyen to")
else:
    print(a, "khong la so nguyen to")