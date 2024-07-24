prefectures = ['Hokkaido', 'Hokkaido', 'Tokyo', 'Kanagawa']
cities = ['Sapporo', 'Hakodate', 'Minato', 'Yokohama']
populations = [100, 200, 300, 400]
population_dict = {(state, city): population for state, city, population in zip(prefectures, cities, populations)}
print(population_dict)
multiplicated_xy_setdict = {frozenset([x, y]): x*y for x in range(2) for y in range(2)}
print(multiplicated_xy_setdict)
print({0: {0: 0, 1: 0, 2: 0}, 1: {0: 0, 1: 1, 2: 2}, 2: {0: 0, 1: 2, 2: 4}})
multiplicated_xy_dict = {}
I = 3
J = 3
for i in range(I):
    multiplicated_xy_dict[i] = {}
    for j in range(J):
        multiplicated_xy_dict[i][j] = i*j
print(multiplicated_xy_dict)
I = 3
J = 3
multiplicated_xy_dict = {i:{j:(i*j) for j in range(J)} for i in range(I)}
print(multiplicated_xy_dict)
#表データの生成
data = [
    ['01', '0001', 'Male', 'Yamada', 'Tarou', 25, 'Tokyo'],
    ['01', '0002', 'Male', 'Satou', 'Takeshi', 27, 'Kanagawa'],
    ['01', '0003', 'Female', 'Tanaka', 'Yuko', 25, 'Saitama'],
    ['02', '0001', 'Male', 'Smith', 'Mike', 22, 'NewJersey'],
    ['02', '0002', 'Male', 'Turner', 'Tom', 27, 'Kansas'],
    ['02', '0003', 'Male', 'Jackson', 'David', 22, 'Florida']
]
print(data)
# 辞書変数生成
member_information = {}
# 表データをレコード毎に格納する
for record in data:
    key = (record[0], record[1])
    info = record[2:]
    member_information[key] = info
# 結果を表示する
print('number', 'informaton', sep='\t')
for key, info in member_information.items():
    print(key, info)
