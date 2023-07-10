print("Program menghitung Kelipatan Persekutuan Terkecil (KPK)")

bilangan_1 = int(input("Masukkan Bilangan Pertama: "))
bilangan_2 = int(input("Masukkan Bilangan Kedua "))

hasil = bilangan_1 
while (hasil % bilangan_2) != 0:
    hasil = hasil + bilangan_1
    
print(f"KPK: {hasil}")