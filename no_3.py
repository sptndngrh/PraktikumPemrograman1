# No 3
# User diminta memasukkan bilangan X. Program lalu memasukkan bilangan sebanyak X.
# Buatlah fungsi/prosedur untuk menghitung rata-rata dari bilangan-bilangan
# yang di-inputkan user!

def average_from(x):
    bil = []
    for a in range(x):
        bil.append(input(f"Masukkan bilangan ke-{a + 1}: "))
        
    sum = 0
    for y in range (len(bil)):
        sum += int(bil[y])
        
    return sum / len(bil)
x = int(input("Masukkan jumlah bilangan yang akan dimasukkan: "))
print(average_from(x))