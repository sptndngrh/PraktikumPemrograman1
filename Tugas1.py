import os
os.system('cls')

def linear_search(keyword, data):
    print(f"Data: {data}")

    for i in range(len(data)):
        if str(data[i]).lower() == keyword.lower():
            print(f"Nomor plat kendaraan '{keyword}' ditemukan dalam database index {i}")
            return i
    
    print(f"Nomor plat kendaraan '{keyword}' tidak ditemukan dalam database!")
    return -1

data = ['R 300 SR', 'R 1234 DJ', 'R 701 LP', 'R 3218 RR]', 'R 007 TU', 'R 3 ST', 'R 999 RT', 'R 210 RO', 'R 1111 II', 'R 4987 LH']
keyword = input("Search something: ")
linear_search(keyword, data)