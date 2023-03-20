command = ''
started = False
while True:
    command = input("> ")

    if command == "start":
        if started:
            print('Car has already started.')
        else:
            started = True
            print('Car started, vroom!!')        

    elif command == "stop":
        if not started:
            print('Car has already stopped.')
        else:
            started = False
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