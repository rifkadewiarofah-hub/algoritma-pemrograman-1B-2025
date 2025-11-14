def hg ():
    nama = input("masukkan nama anda : ")
    jabatan = input("masukkan jabatan anda : ")
    gaji_pokok = int(input("masukkan gaji pokok anda : "))

    pajak = 0.05 * gaji_pokok

    if jabatan == "manager":
        tunjangan = 0.1 * gaji_pokok
    elif jabatan == "staff":
        tunjangan = 0.05 * gaji_pokok
    else: 
        tunjangan = 0

    gaji_bersih = gaji_pokok + tunjangan - pajak

    print("nama :", nama)
    print("jabatan :", jabatan)
    print("gaji pokok anda adalah :", gaji_pokok)
    print("tunjangan anda adalah :", tunjangan)
    print("pajak yang harus anda bayar adalah :", pajak)
    print("gaji bersih anda adalah :", gaji_bersih)

hg()
