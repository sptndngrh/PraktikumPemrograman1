"""
1. Pada suatu kelas terdapat 5 mahasiswa. Pada akhir semester mereka menerima lembar Indeks
Prestasi Semester (IPS), masing-masing mahasiswa tersebut memiliki IPS sebagai barikut 
yaitu: {3.8, 2.9, 3.3, 4.0, 2.4}. Buatlah program untuk mengurutkan IPS mahasiswa tersebut dari
yang terbesar hingga terkecil dengan menggunakan algoritma Bubble Sort !
"""

def bubble_sort(array):
    
    for i in range(len(array)):
        for j in range(len(array)- i - 1):
            if array[j] < array [j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    return array

list_nilai = [3.8, 2.9, 3.3, 4.0, 2.4]

print("==== Mengurutkan Nilai Indeks Prestasi Siswa====")
print(f"Nilai sebelum pengurutan : {list_nilai}")
bubble_sort(list_nilai)
print(f"Nilai sesudah pengurutan : {list_nilai}")