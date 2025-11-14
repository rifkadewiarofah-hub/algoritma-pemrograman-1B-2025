t1 = (3, 1, 4)
t2 = (1, 5, 9)

gabung = ()
for i in t1:
    gabung += (i,)
for j in t2:
    gabung += (j,)

unik = ()
for angka in gabung:
    ada = False
    for x in unik:
        if angka == x:
            ada = True
            break
    if not ada:
        unik += (angka,)
 
unik = list(unik)  
for i in range(len(unik)):
    for j in range(i + 1, len(unik)):
        if unik[i] < unik[j]:
            unik[i], unik[j] = unik[j], unik[i]

hasil = ()
for x in unik:
    hasil += (x,)

print(hasil)