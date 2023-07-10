#Huruf vokal dan konsonan
"""
Nama    : Septiandi Nugraha
Kelas   : S1SE 05 B
NIM     : 21104060
"""
print("Menentukan Huruf Vokal dan Konsonan")

huruf = str(input ("Masukkan sebuah huruf: "))
hurufvokal = ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O']
hurufkonsonan = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']


if huruf in hurufvokal:
    print(f"Huruf {huruf} merupakan huruf vokal")

elif huruf in hurufkonsonan:
    print(f"Huruf {huruf} merupakan huruf konsonan")

else:
    print(f"{huruf} Bukan merupakan huruf!")





