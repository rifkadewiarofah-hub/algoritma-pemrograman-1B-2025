data = []
id_antrian = 1

while True:
    print("\n1. Tambah Kunjungan")
    print("2. Lihat Daftar Kunjungan")
    print("3. Hapus Kunjungan")
    print("4. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Nama Pengunjung: ")
        santri = input("Nama Santri: ")
        asal = input("Daerah Asal (Sumatra/Kalimantan/Jawa): ").capitalize()
        data.append([id_antrian, nama, santri, asal])
        print("Data berhasil ditambah, ID:", id_antrian)
        id_antrian += 1

    elif pilih == "2":
        if not data:
            print("Belum ada data.") 
        else:
            print("\nDaftar Kunjungan:")
            for asal_daerah in ["Sumatra", "Kalimantan", "Jawa"]:
                for d in data:
                    if d[3] == asal_daerah:
                        print(f"ID {d[0]} | {d[1]} menjenguk {d[2]} dari {d[3]}")

    elif pilih == "3":
        hapus = int(input("Masukkan ID yang ingin dihapus: "))
        ketemu = False
        for d in data:
            if d[0] == hapus:
                data.remove(d)
                ketemu = True
                print("Data dihapus.")
                break
        if not ketemu:
            print("ID tidak ditemukan.")

    elif pilih == "4":
        print("Keluar dari program.")
        break

    else:
        print("Pilihan salah.")