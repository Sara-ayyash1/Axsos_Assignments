def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        key = my_list[i]  
        j = i - 1
      
        while j >= 0 and key < my_list[j]:
            my_list[j + 1] = my_list[j]
            j -= 1
        
        my_list[j + 1] = key

data = [5,6, 2, 1, 9, 4, 3, 7,10,8]
insertion_sort(data)
print(data)