# Buatlah program untuk menghitung luas lingkaran dan keliling dengan
# menggunakan method procedure. Jari-jari adalah masukkan dari pengguna
"""
Nama    : Septiandi Nugraha
Kelas   : S1SE 05 B
NIM     : 21104060
"""

# # Function Method
# print("Program menghitung luas dan keliling lingkaran")
# def keliling_lingkaran(jari_jari):
#     print(f"Keliling lingkaran adalah: {2 * 3.14 * jari_jari}")
# def luas_lingkaran(jari_jari):
#     print(f"Luas lingkaran adalah: {3.14 * (jari_jari * jari_jari)}")
    
# sisi = int(input("Masukkan jari-jari lingkaran: "))
# keliling_lingkaran(sisi)
# luas_lingkaran(sisi)

# Procedure Method 
print("Program menghitung luas dan keliling lingkaran")
def keliling_lingkaran(jari_jari):
    hasil1 = 2 * 3.14 * jari_jari
    return hasil1
def luas_lingkaran(jari_jari):
    hasil2 = 3.14 * (jari_jari * jari_jari)
    return hasil2

jari_jari = int(input("Masukkan jari-jari lingkaran: "))
print(f"Keliling lingkaran adalah: {keliling_lingkaran(jari_jari)}")
print(f"Luas lingkaran adalah: {luas_lingkaran(jari_jari)}")