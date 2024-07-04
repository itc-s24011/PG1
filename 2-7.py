[2, 4, 8, 16]
print([2, 4, 8, 16] + [3, 6, 9, 12])
my_list = [2, 4, 8, 16]
print(my_list + [3, 6, 9, 12])
print(my_list)

my_list = [2, 4, 8, 16]
my_list.append(3)
my_list.append(6)
my_list.append(9)
print(my_list)

my_list.extend([12, 15])
print(my_list)

my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_list.reverse()
print(my_list)
