def selection_sort(my_list):
    for i in range(len(my_list)):
        min_index = i 
        
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j 
        
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

numbers = [64, 25, 12, 22, 11]
selection_sort(numbers)
print(numbers) 