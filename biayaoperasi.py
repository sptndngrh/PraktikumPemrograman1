#Identifikasi biaya operasi penyakit
"""
Nama    : Septiandi Nugraha
Kelas   : S1SE 05 B
NIM     : 21104060
"""
print("Biaya Operasi Penyakit") 
print("Daftar Biaya Operasi Yang Tersedia: ")
print("1. Biaya Operasi Mata")
print("2. Biaya Operasi Jantung")

pilihan_operasi = int(input("Masukkan Pilihan: "))

if pilihan_operasi == 1:
    print("Jenis Penyakit Mata: ")
    print("1. Biaya Katarak")
    print("2. Biaya Plus / Minus")
    print("3. Biaya Silinder")
    
    b_opr_katarak = "Rp 7.500.000"
    b_opr_plusminus = "Rp 5.000.000"
    b_opr_silinder = "Rp 4.000.000" 
    
    operasi_mata = int(input("Jenis penyakit mata yang akan di operasi: "))
    if operasi_mata == 1:
        print(f"Biaya operasi Katarak adalah {b_opr_katarak}")
    elif operasi_mata == 2:
        print(f"Biaya operasi Plus / Minus adalah {b_opr_plusminus}")
    elif operasi_mata == 3:
        print(f"Biaya operasi Silinder adalah {b_opr_silinder}")
    else:
        print("Tidak tersedia dalam pilihan")
    
elif pilihan_operasi == 2:
    print("Jenis Penyakit Jantung: ")
    print("1. Biaya Jantung Koroner")
    print("2. Biaya Katup Jantung")
    print("3. Biaya Otot Jantung")
    
    b_opr_jantungkoroner = "Rp 500.000.000"
    b_opr_katupjantung = "Rp 350.000.000"
    b_opr_ototjantung = "Rp 450.000.000"
    
    operasi_jantung = int(input("Jenis penyakit mata yang akan di operasi: "))
    if operasi_jantung == 1:
        print(f"Biaya operasi Jantung Koroner adalah {b_opr_jantungkoroner}")
    elif operasi_jantung == 2:
        print(f"Biaya operasi Katup Jantung adalah {b_opr_katupjantung}")
    elif operasi_jantung == 3:
        print(f"Biaya operasi Otot Jantung adalah {b_opr_ototjantung}")
    else:
        print("Tidak tersedia dalam pilihan")