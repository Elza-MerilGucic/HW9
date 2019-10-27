print("Welcome to distance unit converter")

while True:
    kilometers = float(input("Please enter number of kilometers: "))

    miles = 0.621371 * kilometers
    print(str(kilometers) + " kilometers equals " + str(miles) + " miles")
    repeat = input("Do you want to do another conversion? (yes / no): ")
    if repeat == "yes":
        continue
    else:
        print("Thank you and goodbye")
        break
