import os
os.system('cls')

def insertion_sort(data):
    for i in range(1, len(data)):
        item = data[i]
        j = i - 1

        while j >= 0 and data[j] > item:
            data[j + 1] = data[j]
            j -= 1
        
        data[j + 1] = item
    
    return data

def convert_data_to_string(data):
    converted_data = []

    for i in data:
        converted_data.append(str(i).lower())
    
    return converted_data

def binary_search(keyword, data):
    converted_data = convert_data_to_string(data)
    sorted_data = insertion_sort(converted_data)
    print(f"Data (sorted): {sorted_data}")
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if sorted_data[mid] == keyword.lower():
            print(f"NIM '{keyword}' ditemukan dalam kelas. Pada index ke-{mid}")
            return mid
        elif str(sorted_data[mid]) < str(keyword).lower():
            left = mid + 1
        else:
            right = mid - 1
    
    print(f"NIM '{keyword}' tidak ditemukan dalam kelas!")
    return -1


data = [12102002, 121002004, 12102001, 12102003, 12102005, 12102008, 12102007,
12102006, 12102009, 121020013, 12102010, 12102012, 12102011]
keyword = input("Search something: ")
binary_search(keyword, data)