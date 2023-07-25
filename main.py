def my_min(lst):
    min_element = lst[0]
    for element in lst[1:]:
        if element < min_element:
            max_element = element
    return min_element


lst = [5, 3, 7, 9, 2, 4]
print(min(lst))
