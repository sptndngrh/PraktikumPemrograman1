#Validasi Nilai
"""
Nama    : Septiandi Nugraha
Kelas   : S1SE 05 B
NIM     : 21104060
"""
print("Validasi nilai dari data nilai yang dimasukkan")

bilangan_1 = int(input("Masukkan sebuah bilangan yang akan dibagi: "))
bilangan_2 = int(input("Masukkan bilangan pembagi: "))
hasil_bagi = (bilangan_1 / bilangan_2)

if hasil_bagi :
    print("Hasil Bagi: ", hasil_bagi)

elif hasil_bagi == 0:
    print("Pembagi tidak boleh 0")