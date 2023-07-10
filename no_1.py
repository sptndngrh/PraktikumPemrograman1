# No 1
# Buatlah fungsi/prosedur untuk menghitung luas segitiga!

# Fungsi
def luas_segitiga(panjang, tinggi):
    print(f"Luas segitiga yaitu: {(panjang * tinggi) *1/2}")
    
panjang_input = int(input("Masukkan panjang: "))
tinggi_input = int(input("Masukkan tinggi: "))
luas_segitiga(panjang_input, tinggi_input)

# Prosedur
def luas_segitiga(panjang, tinggi):
    return (panjang * tinggi) * 1/2

masukkan_panjang = int(input("Masukkan panjang: "))
masukkan_tinggi = int(input("Masukkan tinggi: "))
print(f"Luas segitiga yaitu: {luas_segitiga(masukkan_panjang, masukkan_tinggi)}")

