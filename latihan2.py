#Cara saya sendiri
kata = []
apa_aja_terserah = input("Masukkan Jumlah Kata: ")

for i in range(0,int(apa_aja_terserah)):
    terserah_deui = input("Masukkan kata: ")
    kata.append(terserah_deui)
    
dicari = input("Masukkan kata yang dicari: ")


for a in kata:
    if a == dicari:
        print(f"{dicari} ditemukan pada indeks ke-{kata.index(a)}")
        break
else:      
    print("kata tidak ditemukan!")