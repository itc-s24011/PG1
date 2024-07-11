import random
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
num4 = ''.join(random.sample(numbers, k=4))
while True:
    val = input()
    if val == num4:
        break
    if len(val) != 4:
        print('input 4 numbers.')
        continue
    answer = ''
    for i in range(4):
        if num4[i] == val[i]:
            answer += num4[i]
        else:
            answer += 'X'
    print('-> ' + answer)

