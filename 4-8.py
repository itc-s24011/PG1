def show_how_it_works(func):
    def my_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return my_function

def add_two_numbers(a, b):
    return a + b

add_two_numbers(1, 8)
