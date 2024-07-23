#表データの生成
data = [
    ['0001', 'Male', 'Yamada', 'Tarou', 25, 'Tokyo'],
    ['0002', 'Male', 'Satou', 'Takesi', 27, 'Kanagawa'],
    ['0003', 'Famale', 'Tanaka', 'Yuko', 25, 'Saitama'],
    ['0004', 'Male', 'Suzuki', 'Ichirou', 35, 'Hokkaido']
]
print(data)
#辞書変数生成
member_information = {}

#表データをレコード毎に格納する
for record in data:
    key = record[0]
    info = record[1:]
    member_information[key] = info

#結果を表示する
print('number', 'information',sep='\t')
for key, info in member_information.items():
    print(key, info)
