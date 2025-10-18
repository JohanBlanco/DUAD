def only_numbers(func):
    def wrapper(*parameters):
        for number in parameters:
            if not isinstance(number, int) and not isinstance(number, float):
                raise ValueError(f"{number} is not a number")
        return func(parameters)
    return wrapper

@only_numbers
def sum_numbers(parameters):
    sum = 0
    for number in parameters:
        sum += number
    return sum

if __name__ == '__main__':
    try:
        sum_numbers(1,2,3,4,"5")
    except ValueError as e:
        print(e)

    print(sum_numbers(1,2,3,4,5))