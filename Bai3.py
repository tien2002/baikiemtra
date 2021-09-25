n=int(input("Nhập một số n : "))
def giaithua(n):
    kq=1
    for i in range(1,n+1):
        kq *= i
    return kq
while n:
    if n>0:
        print(giaithua(n))
        break
    else:
       n=int(input("Nhập lại một số nguyên dương n : "))