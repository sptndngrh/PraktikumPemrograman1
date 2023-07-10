# kelilingPersegi
# keliling_persegi 

# Prosedur menghitung keliling persegi
def keliling_persegi(sisi):
    return 4 * sisi

# Prosedur menghitung luas persegi
def luas_persegi(sisi):
    return sisi * sisi

masukkan = int(input("Masukkan sisi persegi: "))
print(f"Keliling persegi: {keliling_persegi(masukkan)}")
print(f"Luas persegi    : {luas_persegi(masukkan)}")


# def kota(cirebon):
#     print(cirebon)
    
# kota("Kota Cirebon, Jawa Barat, Indonesia")

def pengurangan(bil1, bil2):
    hasil = bil1 - bil2
    print("Hasilnya yaitu: ", hasil)
    
pengurangan(7, 5)