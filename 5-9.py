mountain_in_japan = {'fuji': 3776, 'kitadake': 3193, 'okuhodakadake': 3190}
mountain_in_japan_sorted = sorted(mountain_in_japan.items(), key=lambda x: x[0])
for key, val in mountain_in_japan_sorted:
    print(key, val)
mountain_in_japan = {'fuji': 3776, 'kitadake': 3193, 'okuhodakadake': 3190}
mountain_in_japan_sorted = sorted(mountain_in_japan.items(), key=lambda x: x[1])
for key, val in mountain_in_japan_sorted:
    print(key, val)
for key, val in reversed(mountain_in_japan_sorted):
    print(key, val)
mountain_in_japan = {'fiji':3776, 'kitadake': 3193, 'okuhodakadake': 3190, 'dummy': 0}
mountain_in_japan_sorted = sorted(mountain_in_japan.items(), key=lambda x: x[1], reverse=True)
print(mountain_in_japan_sorted)
