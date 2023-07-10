"""
2. Pada suatu organisasi memiliki 10 anggota dengan nama masing-masing: Pain, Konan,
Tobi, Zetsu, Sasori, Hidan, Deidara, Kisame, Kakuzu dan Itachi. Supaya mudah dalam
melaksanakan pencarian. Ketua organisasi akan mengurutkan nama-nama tersebut sesuai
dengan alfabet. Buatlah program untuk membantu Pain dengan menggunakan algoritma 
Selection Sort!
"""

def selection_sort(array):
    
    for i in range(len(array)):
        min_index = i
        
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
                
        array[i], array[min_index] = array[min_index], array[i]
    
    return array
    
anggota = ["Pain", "Konan", "Tobi", "Zetsu", "Sasori", "Hidan", "Deidara", "Kisame", "Kakuzu", "Itachi"]

print("==== Program Mengurutkan Anggota Organisasi ====")
print(f"Anggota Terdiri Dari: {anggota}")
selection_sort(anggota)
print(f"Urutan Anggota Yaitu: {anggota}")