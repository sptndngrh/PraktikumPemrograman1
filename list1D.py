# Pembuatan list "buah"
buah = ["Apel", "Jeruk", "Anggur", "Pisang"]

# mencetak nilai "buah" dengan cara 1
for i in buah:
    print(i)
    
# mencetak nilai "buah" dengan cara 2
buah = ["Apel", "Jeruk", "Anggur", "Pisang"]
print(buah)

# mendefinisikan array dengan indeks tertentu
buah = ["Apel", "Jeruk", "Anggur", "Pisang"]
print(buah[0])

# menambah item baru ke list "buah"
buah = ["Apel", "Jeruk", "Anggur", "Pisang"]
buah.append("Mangga")
print(buah)

# mengosongkan list buah
buah = ["Apel", "Jeruk", "Anggur", "Pisang"]
buah.clear()
print(buah)

# menghapus data index tertentu dari list "buah"
buah = ["Apel", "Jeruk", "Anggur", "Pisang"]
buah.pop(2)
print(buah)

# menghapus sebuah data tertentu dari list "buah"
buah = ["Apel", "Jeruk", "Anggur", "Pisang"]
buah.remove("Pisang")
print(buah)

# membalikan urutan
buah = ["Apel", "Jeruk", "Anggur", "Pisang"]
buah.reverse()
print(buah)

# mengurutkan isi list "buah"
buah = ["Apel", "Jeruk", "Anggur", "Pisang"]
buah.sort()
print(buah)