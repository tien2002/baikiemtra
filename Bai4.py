def TongCacSo(n):
    Tong = 0;
    while (n > 0):
        Tong = Tong + n % 10;
        n = int(n / 10);
    return Tong;


n = int(input("Nhập số nguyên dương: "));
print("Tổng các chữ số của", n, "là", TongCacSo(n));