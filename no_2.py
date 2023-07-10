# No 2
# User diminta melakukan input bilangan 2x. Buatlah fungsi/prosedur yang dapat
# memberitahukan user inputan yang mana yang lebih besar!
# Opsional: Buat output berbeda jika nilai inputan user ternyata sama!

def perbandingan_angka(bilsatu, bildua):
    if bilsatu < bildua:
        print("Bilangan", bilsatu, "lebih kecil dari", bildua)
    elif bilsatu > bildua:
        print("Bilangan", bilsatu, "lebih besar dari", bildua)
    elif bilsatu == bildua:
        print("Bilangan yang dimasukkan sama")
        

bilsatu = int(input("Masukkan bilangan pertama: "))
bildua = int(input("Masukkan bilangan kedua: "))
perbandingan_angka(bilsatu, bildua)