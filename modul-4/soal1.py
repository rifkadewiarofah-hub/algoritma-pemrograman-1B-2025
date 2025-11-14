baris = int(input("Masukkan jumlah baris lampu: "))

for i in range(1, baris + 1):
    jumlah = int(input(f"Masukkan jumlah lampu pada baris ke-{i}: "))
    print(f"\nBaris ke-{i}")
    for j in range(1, jumlah + 1):  
        if j % 3 == 0:
            print(f"Lampu ke-{j} pada baris {i} rusak")
        else:
            print(f"Lampu ke-{j} pada baris {i} menyala")
    if j == jumlah:
        print("Periksa sambungan daya utama")

print("\nSelesai mengecek semua lampu.")