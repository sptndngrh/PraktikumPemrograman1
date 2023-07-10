
# Fungsi menghitung keliling persegi
def hitung_keliling_persegi(sisi):
    print(f"Keliling persegi: {4 * sisi}")


# Fungsi menghitung luas persegi
def hitung_luas_persegi(sisi):
    print(f"Luas persegi: {sisi * sisi}")


user_input = int(input("Masukkan sisi persegi: "))
hitung_keliling_persegi(user_input)
hitung_luas_persegi(user_input)