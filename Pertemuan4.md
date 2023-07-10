# Pertemuan 4 (Asynchronous)

## Perulangan

*(Video pembelajaran pendamping dapat kalian temukan [disini](https://drive.google.com/file/d/18kpOogUXMkcAmHvomTzzQvU_kG8Jafr1/view?usp=sharing))*

Di bahasa Python, kita bisa membuat sebuah
perulangan dengan 2 cara:

1. For
2. While

## For

Perulangan `for` dibagi menjadi 3 jenis.

### Jenis 1

Perhatikan contoh berikut:

```Python
# range(max)
for i in range(5):
    print(f"Perulangan ke-{i}")

print()
```

Untuk `for` jenis pertama ini, kita masukan
banyaknya perulangan yang ingin dilakukan ke dalam
`range()`. Nilai variable `i` nantinya akan berubah,
dimulai dari 0 hingga bilangan yang kalian masukan
ke `range()` dikurangi satu.

#### Output

```
Perulangan ke-0
Perulangan ke-1
Perulangan ke-2
Perulangan ke-3
Perulangan ke-4
```

### Jenis 2

```Python
# range(min, max)
for i in range(1, 6):
    print(f"Perulangan ke-{i}")

print()
```

Untuk `for` jenis kedua, kita memasukan nilai
minimum dan maksimum perulangan. Nilai-nilai
yang kita masukan ini nantinya menentukan
berapa nilai variable `i` saat perulangan 
berlangsung.

Pada contoh di atas, perulangan akan terjadi 5x,
dengan nilai `i` yang akan berubah secara urut
dari 1 sampai 5. Nilai awal `i` akan sama selalu 
dengan nilai minimum yang dimasukan ke `range()`, 
sedangkan nilai akhir `i` adalah nilai maximum 
`range()` dikurangi satu.

#### Output
```
Perulangan ke-1
Perulangan ke-2
Perulangan ke-3
Perulangan ke-4
Perulangan ke-5
```

### Jenis 3

```Python
# range(min, max, step)
for i in range(10, 0, -1):
    print(f"Perulangan ke-{i}")

print()
```

Untuk `for` jenis terakhir ini, prinsipnya
sama dengan jenis kedua, hanya saja kita menentukan
lompatan bilangan nilai `i` untuk setiap perulangan.

Misalnya pada contoh di atas, nilai `i` di awal
adalah 10. Untuk setiap kali perulangan terjadi,
nilainya akan berkurang sebanyak `-1` hingga `i` 
memiliki nilai 1.

#### Output
```
Perulangan ke-10
Perulangan ke-9
Perulangan ke-8
Perulangan ke-7
Perulangan ke-6
Perulangan ke-5
Perulangan ke-4
Perulangan ke-3
Perulangan ke-2
Perulangan ke-1
```

## While

Jika kalian mengerti bahasa Inggris, perulangan
`while` sebenarnya lebih mudah dimengerti.
Masa sih? Iya, perhatikan potongan kode berikut:

```Python
while x > 2:
```

Cara membaca kode di atas adalah "Selama nilai
x lebih dari 2, lakukan perintah-perintah
di bawahnya!"

Jika pada perulangan `for` kita menentukan
program harus mengulang berapa kali, pada
perulangan `while` ini kita memberitahu
program untuk terus melakukan perulangan
hingga syarat yang kita tentukan bernilai 
`False`.

Syarat apa saja yang kita bisa atur? Banyak!
Syarat-syarat yang bisa kita gunakan pada
`if` bisa juga kita gunakan sebagai syarat
perulangan `while`.

Okay, cukup teori. Sekarang saatnya kita 
mainkan!

**Bonus: Anda bisa memberhentikan paksa sebuah
perulangan `for` dan `while` dengan perintah 
`break`!**

```Python
login_chance = 3

while login_chance > 0:

    username = input("Masukan username: ")
    password = input("Masukan password: ")

    login_success = (username == "admin") and (password == "admin")

    if login_success:
        print("Login berhasil!")
        break

    else:
        login_chance = login_chance - 1
        print(f"Login gagal! Kesempatan mencoba: {login_chance}")
```

Pada contoh di atas, kita membuat sebuah sistem login 
sederhana. Pertama-tama, kita membuat sebuah variable
`login_chance` yang menampung informasi banyaknya
percobaan yang diperbolehkan untuk seorang user
mencoba melakukan login.

Di bawahnya, perulangan `while` mulai digunakan. Tertulis
disana `while login_chance > 0` (selama user masih memiliki
kesempatan login), program akan meminta user memasukan
username dan password mereka. Selanjutnya, program akan
mengecek kebenaran username dan password yang diinputkan
user melalui pengecekan `if` sederhana. 

Jika login berhasil, program akan mencetak "Login berhasil!"
dan dengan perintah `break`, ia akan menghentikan perulangan 
secara paksa **walaupun** sebenarnya nilai `login_chance` 
masih lebih dari 0.

Jika login gagal, program akan mengurangi nilai variable
`login_chance` sebesar -1. Jika user kehabisan kesempatan
login (nilai `login_chance` mencapai 0), program akan keluar.

## Tugas
(Sama seperti di modul)

1. Buatlah sebuah program dengan statement perulangan dimana 
dapat menghitung total nilai dari suatu bilangan yang 
diinputkan. Dengan tampilan output sebagai berikut:

```
Masukan bilangan: 5
Total nilai = 5 + 4 + 3 + 2 + 1 = 15
```

2. Buatlah sebuah program dengan statement perulangan, dimana 
dapat menghitung hasil pangkat suatu bilangan. Dengan tampilan 
output sebagai berikut:

```
Masukan bilangan: 2
Masukan pencacah: 3
Hasil pangkat   : 8
```

3. Buatlah sebuah program dengan statement perulangan untuk 
menentukan KPK dari dua buah bilangan bulat. Sebagai contoh 
KPK dari 8 dan 12 adalah 24. Untuk lebih jelasnya perhatikan 
table KPK di bawah ini:

| 8   | 16   | (24) | 32  | 40  | 48  | ... | 
|-----|------|------|-----|-----|-----|-----|
| 12  | (24) | 36   | 48  | 60  | 72  | ... |

Program tersebut mempunyai output sebagai berikut:

```
Masukan bilangan pertama: 12
Masukan bilangan kedua  : 8
KPK                     : 24
```

## Laporan Praktikum & Submission di LMS

Seperti biasa, kalian diminta untuk membuat laporan
praktikum. Isi dari laporan yang kalian buat antara
lain:

- Cover
- Pembahasan kode-kode yang kalian buat disertai
screenshot output

Kode apa saja yang perlu dibahas?

- **For.py** (berisikan 3 jenis perulangan `for`)
- **While.py** (berisikan program login sederhana yang
memanfaatkan perulangan `while`)
- Kode-kode untuk jawaban 3 soal tugas di atas.

> Q: "Kode-kode latihan yang ada di modul di LMS bagaimana?"
>
> A: "Karena kode-kode disana saya rasa kurang *beginner 
> friendly*, boleh kalian *skip* saja."

Setelah itu, bungkus laporan praktikum beserta
kode-kode yang sudah kalian kerjakan ke dalam
*archive* yang sama, dengan format penamaan:
**Pertemuan4_NIM_Nama.rar**

Deadline **Kamis, pukul 23:59**. 

Good luck have fun! ;)