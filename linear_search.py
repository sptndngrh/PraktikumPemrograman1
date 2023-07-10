def linear_search(data, keyword):
    
    for i in range(len(data)):
        if str(data[i]).lower() == keyword.lower():
            print(f"Keyword {keyword} is found at index {i}")
            return i
        
    print("Error 404: Keyword {keyword} not found!")
    return -1

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

data = [409, 509, 14, "Siti", "Maimunah", "Haji Maun", 15, 67, 89, 74]
keyword = input("Search something: ")
linear_search(data, keyword)