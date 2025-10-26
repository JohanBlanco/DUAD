def bubble_sort(list_to_sort):
    if not isinstance(list_to_sort, list):
        raise ValueError(f'The parameter data type is {type(list_to_sort)}, but it must be a list')
    
    result = list_to_sort.copy()
    for _ in range(0, len(result) - 1):
        changed = False
        for index in range(0, len(result) - 1 - _):
            current = result[index]
            next = result[index+1]

            if current > next:
                result[index] = next
                result[index+1] = current
                changed = True
        if not changed:
            break
    return result