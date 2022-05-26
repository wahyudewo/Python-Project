a = ""
started = False
while True:
    a = input("command: ").lower()
    if a == "start":
        if started:
            print("Car already started..")
        else:
            started = True
            print("Car Started..")
    elif a == "stop":
        if not started:
            print("Car already stopped.")
        else:
            started = False
            print("Car Stopped.")            
    elif a == "help":
        print("""
start -> to start the car
stop -> to stop the car
quit -> to quit
              """)
    elif a == "quit":
        break
    else:
        print("Sorry, I don't Understand")