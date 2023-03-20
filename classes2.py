class House:
    num_ofrooms = 5
    bathrooms = 2
    
    def costofliving(self, rate):
        cost = rate * self.num_ofrooms
        return cost
        
house1 = House()
print(house1.num_ofrooms)
#print(House.num_ofrooms)
house1.num_ofrooms = 7
print(house1.num_ofrooms)
print(House.costofliving(house1, 7))