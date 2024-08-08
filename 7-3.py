import sys

class MyValueLimitError(Exception):
    def __init__(self, x1, x2, limit_number):
        self.x1 = x1
        self.x2 = x2
        self.limit_number = limit_number

    def __stra__(self):
        return '値の取りうる範囲を超えています {0}{1}{2}'.format(self.x1, self.x2, self.limit_number)

def multiplication_limit(x1, x2, limit_number):
    try:
        x = x1 * x2
        if x > limit_number:
            raise MyValueLimitError(x1, x2, limit_number)
        return x
    except MyValueLimitError as vle:
        print(vle)
        return limit_number
    except:
        print('Unexpected Error:', sys.exc_info())
        return None

limit_number = 10000
multiplication_limit(100, 101, limit_number)
