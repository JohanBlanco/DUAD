def inverted_bubble_sort(list_to_sort):
    for _ in range(len(list_to_sort) - 1, -1, -1):
        changed = False
        for index in range(len(list_to_sort) - 1, 0, -1):
            current = list_to_sort[index]
            previous = list_to_sort[index-1]

            if current < previous:
                list_to_sort[index] = previous
                list_to_sort[index-1] = current
                changed = True
        if not changed:
            break
    return list_to_sort

if __name__ == "__main__":
    list1 = [5, 2, 9, 1, 5, 6]

    print(list1)

    inverted_bubble_sort(list1)

    print(list1)