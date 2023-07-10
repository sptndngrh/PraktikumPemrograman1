#Data Individu
"""
Nama    : Septiandi Nugraha
Kelas   : S1SE 05 B
NIM     : 21104060
"""

#Input Data Individu
nama = input("Nama:  ")
gender = input("jenis kelamin: (L/P)  ")
agama = input("agama :  ")

#Output Data Individu
print("Nama:  ",nama)
if(gender == "L", "l"):
    print("Jenis kelamin : Laki-laki")
    if(agama == "1", "Islam", "islam"):
        print("agama:  Islam")
    elif(agama == "2", "Kristen", "kristen"):
        print("agama:  Kristen")
    elif(agama == "3", "Katolik", "katolik"):
        print("agama:  Katolik")        
    elif(agama == "4", "Hindu", "hindu"):
        print("agama:  Hindu")
    elif(agama == "5", "Budha", "budha", "Buddha", "buddha"):
        print("agama:  Buddha")
    else:
        print("Tidak ditemukan agama yang terdeteksi")
elif(gender == "P", "p"):
    print("Jenis kelamin:  Perempuan")
    if(agama == "1", "Islam", "islam"):
        print("agama:  Islam")
    elif(agama == "2", "Kristen", "kristen"):
        print("agama:  Kristen")
    elif(agama == "3", "Katolik", "katolik"):
        print("agama:  Katolik")    
    elif(agama == "4", "Hindu", "hindu"):
        print("agama:  Hindu")
    elif(agama == "5", "Budha", "budha", "Buddha", "buddha"):
        print("agama:  Buddha")
    else:
        print("Tidak ditemukan agama yang terdeteksi")
else:
    print("tidak ada dalam pilihan")