# 1)Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
def biggie_size(my_list):
    for i in range (len(my_list)):
        if my_list[i]>1:
            my_list[i] = "big"
    return my_list

print(biggie_size([-1, 3, 5, -5]))


# 2)Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values.
# (Note that zero is not considered to be a positive number).
def count_positives(my_list):
    count = 0
    for item in my_list:
        if item > 0:
            count +=1
    my_list[-1] =count #the last value in the list access by => my_list[len(my_list)-1] or my_list[-1]
    return my_list

print (count_positives([-1,1,1,1]))
print (count_positives([1,6,-4,-2,-7,-2]))


# 3)Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
def sum_total(my_list):
    sum = 0
    for item in my_list:
        sum+=item
    return sum

print (sum_total([1,2,3,4]))
print (sum_total([6,3,-2]))


# 4)Average - Create a function that takes a list and returns the average of all the values.
def average(my_list):
    return sum_total(my_list)/len(my_list)

print(average([1,2,3,4]))


# 5)Length - Create a function that takes a list and returns the length of the list.
def length(my_list):
    count = 0
    for item in my_list:
        count +=1
    return count

print(length([37,2,1,-9]))
print(length([]))


# 6)Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
def minimum(my_list):
    if len(my_list) == 0 :
        return False
    
    min_val = my_list[0]
    for item in my_list:
        if item < min_val :
            min_val = item
    return min_val

print(minimum([37,2,1,-9]))
print(minimum([]))


# 7)Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
def maximum(my_list):
    if len(my_list) == 0 :
        return False
    
    max_val = my_list[0]
    for item in my_list:
        if item > max_val :
            max_val = item
    return max_val

print(maximum([37,2,1,-9]))
print(maximum([]))


# 8)Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def ultimate_analysis(my_list):
   my_dict = {'sumTotal': sum_total(my_list), 'average': average(my_list), 'minimum': minimum(my_list), 'maximum': maximum(my_list), 'length': length(my_list)}
   return my_dict

print(ultimate_analysis([37,2,1,-9]))

# 9)Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list.
def  reverse_list(my_list):
    left =0
    right = len(my_list)-1

    while left < right:
        temp= my_list[left] 
        my_list[left] =my_list[right]
        my_list[right] = temp
        left+=1
        right-=1
    return my_list
 
print (reverse_list([37,2,1,-9]))

