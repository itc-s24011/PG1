def list_del_nth(list_, index):
    try:
        del list_[index]
    except IndexError:
        print('Index Not Found')
    except:
        print('Unexpected Error')
    else:
        print('Successfully')

my_list = ['a', 'b', 'c', 'd']
list_del_nth(my_list, '5')
list_del_nth(my_list, 5)
list_del_nth(my_list, 0)

my_list

def square(x):
    if not isinstance(x, (int, float)):
        if isinstance(x, str) and x.isdigit():
            x = int(x)
        else:
            raise ValueError('square', x)
    return x ** x

print(square(2))
print(square('a'))
