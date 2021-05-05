car_input = ""
started = False

while True:
    car_input = input("> ").upper()  # setting the input to uppercase from here
    if car_input == "START":
        if started:
            print("Car already started!")
        else:
            started = True
            print("Car started... Ready to go!")

    elif car_input == "STOP":
        if not started:
            print("Car already stopped!")
        else:
            started = False
            print("Car stopped.")

    elif car_input == "HELP":
        print("""start - to start the car
stop - to stop the car
quit - to exit""")
    elif car_input == "QUIT":
        break
    else:
        print("I don't understand.")