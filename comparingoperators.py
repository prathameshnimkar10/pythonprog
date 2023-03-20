temperature = input("What does the weather app say? ")
print(temperature)
if int(temperature) > 32:
    print('Its a hot day.')
elif int(temperature) <= 32 and int(temperature) > 15:
    print('Its a pleasant day.')
elif int(temperature) <= 15:
    print('Its a cold day.')