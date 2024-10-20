# list = [3,1,2,3,4,5,6,3,4,5,7,6,5,4,3,4,5,4,3, 'Привіт', 'анаконда']

def remove_duplicates(lst):
    return list(set(lst))

def sort_list(lst):
    numbers = [x for x in lst if isinstance(x, (int, float))]
    strings = [x for x in lst if isinstance(x, str)]
    
    numbers.sort()
    strings.sort()
    
    return numbers + strings

input_list = [3, 1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']

unique_list = remove_duplicates(input_list)
print("Список без повторень:", unique_list)

sorted_list = sort_list(unique_list)
print("Відсортований список:", sorted_list)