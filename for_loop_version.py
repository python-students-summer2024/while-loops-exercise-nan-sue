def get_starting_number():
    num_bottle = input("How many bottles of beer on the wall? ")

    while not num_bottle.isdigit() or int(num_bottle) < 1:
        print("Please enter a valid integer 1 or greater.")
        num_bottle = input("How many bottles of beer on the wall?")
    return int(num_bottle)

def sing(num_bottle):
    for i in range(num_bottle, 0, -1):
        if i > 2:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i-1} bottles of beer on the wall.\n")
        elif i == 2:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i-1} bottle of beer on the wall.\n")
        else:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")

    