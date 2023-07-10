"""
3. Buatlah program untuk menginput nama buku lalu muncul pilihan jenis
sorting (dengan Insertion Sort).
"""

book = []
def add_book():
    jumlah = int(input("Masukkan Total Buku : "))
    for i in range(jumlah):
        jdl = input(f"Masukkan Judul Buku ke{i + 1} : ")
        book.append(jdl)
        jumlah = jumlah - 1
    while(True):
        jumlah = jumlah - 1
        if(jumlah<0):
            break
        
def ascending_buku(Nbook):
    book = Nbook
    for i in range(1, len(book)):
        item = book[i]
        j = i - 1
        while j >= 0 and item < book[j]:
            book[j + 1] = book[j]
            j -= 1
        book[j + 1]= item
        
    print("Sorting Buku Secara Ascending")
    for x in range(len(book)):
        print(f"indeks Buku ke-{x+1} : %s" %book[x])

def descending_book(Nbook):
    book = Nbook
    for i in range(1, len(book)):
        item = book[i]
        j = i - 1
        while j >= 0 and item > book[j]:
            book[j + 1] = book[j]
            j -= 1
        book[j + 1]= item
    print("Sorting Buku Secara Descending")
    for x in range(len(book)):
        print(f"Judul Buku ke-{x+1} : %s" %book[x])


add_book()

print (" ")
print("<==========Urutkan?=========>")
print("1. Insertion Ascending")
print("2. Insertion Descending")
pilih = int(input("Pilih: "))
print(" ")

if(pilih==1):
    ascending_buku(book)
elif(pilih==2):
    descending_book(book)
else:
    print("Pilihan tidak ada dalam program")
        