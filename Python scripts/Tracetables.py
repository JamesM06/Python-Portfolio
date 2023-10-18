items = [24, 16, 35, 42, 7]
'''lowest = items[0]
for current in range(1, len(items)):
    print(lowest, current)
    if lowest < items[current]:
        lowest = items[current]
'''

lowest = items[0]
for current in range(1, len(items)):
    if lowest < items[current]:
        lowest = items[current]
