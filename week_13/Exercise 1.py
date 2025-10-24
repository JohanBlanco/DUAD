def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Args from Wrapper before the function: {args}, {kwargs}")
        returned_value = func(*args, **kwargs)
        print(returned_value)
        print(f"Parameters from Wrapper after the function: {args}, {kwargs}\n")
    return wrapper

@decorator
def decorated_function(*args, **kwargs):
    return f"Parameters from the Function: {args}, {kwargs}"

if __name__ == '__main__':
    decorated_function()
    decorated_function(1,2,3,4)
    decorated_function(key1="value1",key2="value2")
    decorated_function(1,2,3,4,key1="value1",key2="value2")