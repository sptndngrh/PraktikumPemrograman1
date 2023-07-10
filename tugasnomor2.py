print("Program perulangan menghitung hasil pangkat suatu bilangan")

input_bilangan = int(input("Masukkan Bilangan: "))
bilangan_pencacah = int(input("Masukkan Pencacah: "))

hasil_bilangan = input_bilangan

for i in range(bilangan_pencacah - 1):
    hasil_bilangan = hasil_bilangan * input_bilangan

print(f"Hasil pangkat    : {hasil_bilangan}")

