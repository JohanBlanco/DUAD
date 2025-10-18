def decorator(func):
    def wrapper(*parameters):
        print(f"Parameters from Wrapper before the function: {parameters}")
        func(parameters)
        print(f"Parameters from Wrapper after the function: {parameters}")
    return wrapper

@decorator
def decorated_function(parameters):
    print(f"Parameters from the Function: {parameters}")

if __name__ == '__main__':
    decorated_function(1,2,3,4,5)