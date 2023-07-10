# Buatlah sebuah kalkulator sederhana untuk melakukan kalkulasi 2 bilangan
# dengan menggunakan method function atau procedure

"""
Nama    : Septiandi Nugraha
Kelas   : S1SE 05 B
NIM     : 21104060
"""

def pengurangan (a, b):
    return a - b
def penjumlahan (a, b):
    return a + b
def perkalian (a, b):
    return a * b
def pembagian (a, b):
    a / b
def pangkat (a, b):
    a ** b

print("         KALKULATOR          ")
print("                             ")
print("1. Penjumlahan               ")
print("2. Perkalian                 ")
print("3. Pembagian                 ")
print("4. Pengurangan               ")
print("1. Pangkat                   ")


pilihan_menu = input("Masukkan Pilihan: ")

bilangan_1 = int(input("Masukkan bilangan pertama: "))
bilangan_2 = int(input("Masukkan bilangan kedua  : "))

if   pilihan_menu == "1":
    print(f"Hasil Penjumlahan   : ", penjumlahan (bilangan_1, bilangan_2))
elif pilihan_menu == "2":
    print(f"Hasil Perkalian     : ", perkalian (bilangan_1, bilangan_2))
elif pilihan_menu == "3":
    print(f"Hasil Pembagian     : ", pembagian (bilangan_1, bilangan_2))
elif pilihan_menu == "4":
    print(f"Hasil Pengurangan   : ", pengurangan (bilangan_1, bilangan_2))
elif pilihan_menu == "5":
    print(f"Hasil Pangkat       : ", pangkat (bilangan_1, bilangan_2))
else:
    print("Input yang dimasukkan tidak valid!")