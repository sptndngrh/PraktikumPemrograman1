#Panggilan berdasarkan status
"""
Nama    : Septiandi Nugraha
Kelas   : S1SE 05 B
NIM     : 21104060
"""
status_gender = str(input ("Perempuan atau laki-laki ? (L/P) : "))
status_perkawinan = str(input("Anda sudah menikah atau belum ? (Y/N) : "))

if (status_gender.upper() == "P" and status_perkawinan.upper() == "N"):
    print(f"Halo Mbak")
elif (status_gender.upper() == "P" and status_perkawinan.upper() == "Y"):
    print(f"Halo Bu")
elif (status_gender.upper() == "L" and status_perkawinan.upper() == "N"):
    print(f"Halo Mas")
elif (status_gender.upper() == "L" and status_perkawinan.upper() == "Y"):
    print(f"Halo Bapak")
else:
    print("Tidak ada dalam pilihan")
