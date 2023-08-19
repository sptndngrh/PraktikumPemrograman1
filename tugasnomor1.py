print("Program perulangan menghitung total nilai dari suatu bilangan yang di input")

total_angka = 0
a = int(input("Masukkan Bilangan: "))

print("Total nilai =", end = " ")
for b in range(a, 0, -1):
    print(b, end = " ")
    if b == 1:
        print("=", end = " ")
    else:
        print("+", end = " ")
    total_angka = total_angka + b

print(total_angka)