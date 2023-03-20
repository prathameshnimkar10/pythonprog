command = ''
while command != "quit":
    command = input("> ")
    if command == "start":
         print('Car started, vroom!!')
    elif command == "stop":
        print('Car stopped, screeeech!!')
    elif command == "help":
        print("""
    start to start the car
    stop to stop the car
    help for help
    quit to quit""")    
    elif command == "quit":
        print("*ignition off*")    
    else:
        print("Ehh??")      