prefecture_of_japan = {1: 'Hokkaido', 2: 'Aomori', 3: 'Iwate'}
print(prefecture_of_japan)
print(prefecture_of_japan[1])
print(prefecture_of_japan.get(0))
print(prefecture_of_japan.get(1))
print(prefecture_of_japan.get(0, 'Not Found'))
prefecture_of_japan[4] = 'Miyagi'
print(prefecture_of_japan)
print(1 in prefecture_of_japan)
del prefecture_of_japan[4]
print(prefecture_of_japan)
print(prefecture_of_japan.pop(3))
print(prefecture_of_japan)
prefecture_of_japan.clear()
print(prefecture_of_japan)
prefecture_of_japan = {1: 'Hokkaido', 2: 'Aomori', 3: 'Iwate'}
for x in prefecture_of_japan:
    print(x)
for x in prefecture_of_japan.keys():
    print(x)
for x in prefecture_of_japan.values():
    print(x)
for key, x in prefecture_of_japan.items():
    print(key, x)
