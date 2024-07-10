import random
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sample4 = random.sample(numbers, k=4)
num4 = ''.join(sample4)
while True:
    val = input()
    if val == num4:
        print('OK')
        break
    else:
        print(val, ': NG')

