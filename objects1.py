class Recipe():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time
    
    def contents(self):
        # print('The '+ self.dish + 'has' +self.items + \
        #     'and takes about '+self.time + 'minutes to prepare.')
        print('The '+ self.dish + 'has' +str(self.items) + 'and takes about '+str(self.time) + 'minutes to prepare.')

vadapav = Recipe('Vada Pav ', ['vada', 'pav', 'chutney', 'chilli'], 15)
coffee = Recipe('Hot Coffee ', ['milk', 'coffee powder', 'stove', 'sugar', 'crockery'], 20)

print(vadapav.items)
print(coffee.time)
print(vadapav.contents())
print(coffee.contents())