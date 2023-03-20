weight = input('Weight in pounds: ')
unit = input('Kilograms(K) or Stones(S): ')
if unit.upper() == 'K':
    weight = float(weight) * 0.453
    print(float(weight))
elif unit.upper() == 'S':
    weight = float(weight) * 0.0714
    print(float(weight))
else:
    print('Enter valid unit.')