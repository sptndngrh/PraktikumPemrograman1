"""
Nama    : Septiandi Nugraha
Kelas   : S1SE 05 B
NIM     : 21104060

A. Buatlah sebuah program penerimaan mahasiswa. Fitur dari program tersebut dapat menambah data 
mahasiswa, menghapus data mahasiswa, urutkan data berdasarkan NIM, dan cetak seluruh data.
"""

array_mahasiswa = []

def add_mahasiswa():
    jumlah = int(input("Jumlah Mahasiswa: "))
    mahasiswa = []
    while(jumlah > 0):
        nama = input("Nama Mahasiswa: ")
        mahasiswa.append(nama)
        jumlah = jumlah - 1
    while(True):
        panggil(mahasiswa)
        jumlah = jumlah - 1
        if(jumlah < 0):
            break
        
def remove_mahasiswa(array_mahasiswa):
    mahasiswa = array_mahasiswa
    print("Data Mahasiswa %s" %array_mahasiswa)
    mahasiswa.remove(input("Hapus Mahasiswa: "))
    print("Data Mahasiswa %s" %mahasiswa)
    panggil(array_mahasiswa)
    
def asc_mahasiswa(array_mahasiswa):
    mahasiswa = array_mahasiswa
    mahasiswa.sort()
    print(mahasiswa)
    panggil(array_mahasiswa)

def view_mahasiswa(array_mahasiswa):
    mahasiswa = array_mahasiswa
    for x in mahasiswa:
        print("Nama Mahasiswa: %s" %x)
    panggil(array_mahasiswa)
        
def panggil(array_mahasiswa):
    print("<================ Data Mahasiswa ================")
    print("1. Tambah Data Mahasiswa"                         )
    print("2. Hapus Data Mahasiswa"                          )
    print("3. Urutkan Data Mahasiswa"                        )
    print("4. Lihat Data Mahasiswa"                          )
    print("5. Tutup"                                         )
    print("HARAP MEMASUKKAN PILIHAN DENGAN NOMOR 1 SAMPAI 5" )
    
    pilih = int(input("Pilih: "))
    if(pilih == 1):
        add_mahasiswa()
    elif(pilih == 2):
        remove_mahasiswa(array_mahasiswa)
    elif(pilih == 3):
        asc_mahasiswa(array_mahasiswa)
    elif(pilih == 4):
        view_mahasiswa(array_mahasiswa)
    else:
        print("Selesai")
        
panggil(array_mahasiswa = array_mahasiswa)