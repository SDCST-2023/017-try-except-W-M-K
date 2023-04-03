#!python3
#try...except to read an integer

while True:
    inp = input("Please enter an integer")
    try:
        print("Now going to try and convert to an integer")
        inp = int(inp)
        print("We have successfully converted to an integer")
        break
    except Exception as e:
        print("There was an error. Please try again\n")

print(f"You entered {inp}")