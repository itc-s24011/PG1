import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ch = random.choice(alphabet)
while True:
    val = input()
    if ch == val:
        print('OK')
        break
    else:
        print('NG')
