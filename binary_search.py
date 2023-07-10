def insertion_sort(data):
    
    for i in range(1, len(data)):
        item = data[i]
        j = i - 1
        
        while j >= 0 and data[j] > item:
            data[j + 1] = data[j]
            j -= 1
            
        data[j + 1] = item
        
    return data

def convert_data_ke_string(data):
    convert_data = []
    
    for i in data:
        convert_data.append(str(i).lower())
        
    return convert_data

def binary_search(keyword, data):
    converted_data = convert_data_ke_string(data)
    sorted_data = insertion_sort(converted_data)
    low = 0
    high = len(data) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if sorted_data[mid] == keyword.lower():
            print(f"Keyword '{keyword}' is found at index {mid}")
            return mid
        elif str(sorted_data[mid]) < str(keyword).lower():
            low =  mid + 1
        else:
            high = mid - 1
            
    print(f"Error: Keyword '{keyword}' is not found!")
    return -1

data = [409, 509, 14, "Siti", "Maimunah", "Haji Maun", 15, 67, 89, 74]
keyword = input("Search something: ")
binary_search(keyword, data)