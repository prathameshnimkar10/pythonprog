def sum_of(**kwargs):
    sum = 0
    for x, y in kwargs.items():
        sum += y
    return round(sum, 2)

print(sum_of(coffee = 179.99, straw = 0.99, muffins = 80))