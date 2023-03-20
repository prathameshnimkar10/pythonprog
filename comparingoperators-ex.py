#name thing
name = input('What is your name pal? ')
print(name)

if len(name) < 3:
    print("Too short.")
elif len(name) >= 20:
    print("Too big! Got a nickname bruda?")
else:
    print("Nice name " + name + '!')