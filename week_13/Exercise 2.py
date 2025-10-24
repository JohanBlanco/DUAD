def only_numbers(func):
    def wrapper(*args, **kwargs):
        error = ""

        for number in args:
            if not isinstance(number, int) and not isinstance(number, float):
                error += f"\t{number} is not a number\n"

        for key, number in kwargs.items():
            if not isinstance(number, int) and not isinstance(number, float):
                error += f"\t{key}:{number} is not a number\n"

        if len(error) != 0:
            raise ValueError("Errors: \n" + error)
        
        return func(*args, **kwargs)
    return wrapper

@only_numbers
def sum_numbers(*args, **kwargs):
    sum = 0
    for number in args:
        sum += number

    for number in kwargs.values():
        sum += number
    
    return sum

if __name__ == '__main__':
    try:
        sum_numbers(1,{"two": 2},"3",[4], five = "5")
    except ValueError as e:
        print(e)

    print(sum_numbers())
    print(sum_numbers(1,2,3,4,5))
    print(sum_numbers(1,2,3,4, five = 5))
    print(sum_numbers(one=1, two=2, three=3, four=4, five=5))