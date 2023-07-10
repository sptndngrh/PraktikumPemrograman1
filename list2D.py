buah = [
    ["Apel", "Jeruk", "Anggur", "Pisang"],
    ["Nanas", "Melon", "Manggis", "Sawo"]
]

# #Cara mencetak list di dalam list (secara sederhana)
# print(buah)

# #Cara mencetak list di dalam list (lebih rapih)
# for i in buah:
#     print(buah)

#Cara mengurutkan list ke dalam list (berurutan sesuai abjad)    
buah.sort()
for i in buah:
    i.sort()
    print(i)