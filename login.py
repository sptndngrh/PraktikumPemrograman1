#untuk login ke sebuah situs atau website dan aplikasi
login_chance = 3

while login_chance > 0:

    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    login_success = (username == "admin") and (password == "admin")

    if login_success:
        print("login berhasil!")
        break

    else:
        login_chance = login_chance - 1
        print(f"Login gagal! kesempatan mencoba: {login_chance}")