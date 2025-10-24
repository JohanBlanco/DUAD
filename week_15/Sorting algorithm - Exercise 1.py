def bubble_sort(list_to_sort):
    for _ in range(0, len(list_to_sort) - 1):
        changed = False
        for index in range(0, len(list_to_sort) - 1 - _):
            current = list_to_sort[index]
            next = list_to_sort[index+1]

            if current > next:
                list_to_sort[index] = next
                list_to_sort[index+1] = current
                changed = True
        if not changed:
            break


if __name__ == "__main__":
    list1 = [5, 2, 9, 1, 5, 6]

    print(list1)

    bubble_sort(list1)

    print(list1)