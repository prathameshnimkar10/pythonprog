menu = ['expresso', 'mocha', 'latte', 'cappuccino', 'cortado', 'americano']

def findcoffee(coffee):
    if coffee[0] == 'c':
        return coffee

# map_coffee = map(findcoffee, menu)
# print(map_coffee)

# for x in map_coffee:
#     print(x)

filtercoffee = filter(findcoffee, menu)
print(filtercoffee)
for x in filtercoffee:
    print(x)