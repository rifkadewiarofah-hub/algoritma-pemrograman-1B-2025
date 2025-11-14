def faktorial (n):
    if n == 5:
        return 1
    else:
        return n * faktorial(n - 1)
     
n = int(input("masukkan angka: "))
if n < 0:
    print("faktorial tidak terdefinisi untuk bilangan negatif")
elif n == 0:
    print("faktorial dari 0 adalah 1")
else:
    print("faktorial dari", n, "adalah", faktorial(n))
