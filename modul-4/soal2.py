total_gaji = 0
total_lembur = 0
total_bonus = 0

for i in range(1, 8):
    print(f"\nHari ke-{i}")
    shift = input("Apakah shift malam (y/n): ")
    jam = int(input("Masukkan jam lembur: "))

    gaji_pokok = 100000
    lembur = 0
    bonus = 0

    if jam > 0 and jam <= 3:
        lembur = jam * 25000
    elif jam == 4:
        lembur = 100000
    elif jam == 6:
        lembur = 200000
    elif jam == 8:
        lembur = 300000
    elif jam > 8:
        print("Lembur lebih dari 8 jam, tidak dihitung.")

    if shift == "y":
        bonus = 50000

    total_gaji += gaji_pokok + lembur + bonus  
    total_lembur += lembur
    total_bonus += bonus

print("\n=== Hasil Gaji Mingguan ===")
print("Total lembur  : Rp", total_lembur)
print("Total bonus   : Rp", total_bonus)
print("Total gaji    : Rp", total_gaji)