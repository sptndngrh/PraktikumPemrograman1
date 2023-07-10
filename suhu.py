#Program suhu
"""
Nama    : Septiandi Nugraha
Kelas   : S1SE 05 B
NIM     : 21104060
"""
suhu = int(input("Masukkan suhu: "))

if suhu <= 0:
    print(f"Pada suhu {suhu} derajat celcius, air akan berwujud padat(es)")

elif 0 < suhu < 100:
    print(f"Pada suhu {suhu} derajat celcius, air akan berwujud cair")

else:
    print(f"Pada suhu {suhu} derajat celcius, air akan berwujud gas")