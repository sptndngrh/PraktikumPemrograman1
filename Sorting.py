"""
Nama    : Septiandi Nugraha
Kelas   : S1SE 05 B
NIM     : 21104060
"""
import timeit


def insertion_sort(array):
    start = timeit.default_timer()
    
    for i in range(1, len(array)):
        item = array[i]
        j = i - 1
        
        while j >= 0 and array[j] > item:
            array[j + 1] = array [j]
            j -= 1
            
        array[j + 1] = item
        
    stop = timeit.default_timer()
    print (f"Insertion Sort successful Elapsed time: {stop - start}")
    
    return array


def bubble_sort(array):
    start = timeit.default_timer()
    
    for i in range(len(array)):
        for j in range(len(array)- i - 1):
            if array[j] < array [j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    stop = timeit.default_timer()
    print (f"Bubble Sort successful Elapsed time   : {stop - start}")
    
    return array


def selection_sort(array):
    start = timeit.default_timer()
    
    for i in range(len(array)):
        min_index = i
        
        for j in range(i + 1, len(array)):
            if array[min_index] < array[j]:
                min_index = j
                
        array[i], array[min_index] = array[min_index], array[i]
    
    stop = timeit.default_timer()
    print(f"Selection Sort successful Elapsed time   : {stop - start}")
    
    return array


# Uji Coba
list_a = [4, 1, 2, 5, 3, 7, 8]
list_b = [5, 6, 2, 1, 9, 8, 7]
list_c = [4, 6, 9, 3, 1, 2, 4]

#Pembuktian Insertion Sort
print(f"Before: {list_a}")
insertion_sort(list_a)
print(f"After : {list_a}")

print("==============================================================")

#Pembuktian Bubble Sort
print(f"Before: {list_b}")
bubble_sort(list_b)
print(f"After : {list_b}")

print("==============================================================")

#Pembuktian Selection Sort
print(f"Before: {list_c}")
selection_sort(list_c)
print(f"After : {list_c}")

