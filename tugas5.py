#Membuat sebuah program untuk menghitung nilai rerata beserta predikatnya dengan persyaratan
print("Nilai Rerata")

jumlah_mata_kuliah = int(input("Masukkan jumlah Mata Kuliah: "))

print()

data = []
jum = 0

for i in range(0, jumlah_mata_kuliah):
    nilai_matkul = int(input("Masukkan nilai mata kuliah ke-%d: " % (i+1)))
    data.append(nilai_matkul)
    jum += data[i]
    rata_rata = jum / jumlah_mata_kuliah
    
if 100 > rata_rata >= 90:
    print("\nHasil Predikat A dengan nilai: ")
elif 90 > rata_rata >= 70:
    print("\nHasil Predikat B dengan nilai: ")
elif 70 > rata_rata >= 50:
    print("\nHasil Predikat C dengan nilai: ")
elif 50 > rata_rata >= 30:
    print("\nHasil Predikat D dengan nilai: ")
elif 30 > rata_rata >= 0:
    print("\nHasil Predikat E dengan nilai: ")
else:
    print("\nNilai tidak valid!")
    
for i in range(jumlah_mata_kuliah):
    print("Mata kuliah ke-{}: {}".format(i,data[i]))

print(f"\nRata-Rata = {rata_rata}")    