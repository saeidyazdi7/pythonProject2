def my_max(lst):
    max_element = lst[0]
    for element in lst[1:]:
        if element > max_element:
            max_element = element
    return max_element

lst = [5, 3, 7, 9, 2, 4]
print(my_max(lst))