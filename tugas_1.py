# Buatlah program untuk menampilkan nilai bilangan ganjil atau genap dari bilangan
# yang dimasukkan dengan menggunakan method function
"""
Nama    : Septiandi Nugraha
Kelas   : S1SE 05 B
NIM     : 21104060
"""
# Function Method
print("Program untuk menampilkan bilangan ganjil atau genap")
def bilangan(angka):
    if angka % 2 == 0:
        print("Bilangan yang anda masukkan adalah Genap")
    else:
        print("Bilangan yang anda masukkan adalah Ganjil")
    
angka = int(input("Masukkan Bilangan: "))
bilangan(angka)

# Prosedure Method
def bilangan(angka):
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"
    
angka = int(input("Masukkan Bilangan: "))
print(f"Biangan yang anda masukkan adalah {bilangan(angka)}")