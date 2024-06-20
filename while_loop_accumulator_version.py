def get_starting_number():
    num_bottle = input("How many bottles of beer on the wall? ")

    while not num_bottle.isdigit() or int(num_bottle) < 1:
        print("Please enter a valid integer 1 or greater.")
        num_bottle = input("How many bottles of beer on the wall?")
    return int(num_bottle)

def sing(num_bottle):
    while num_bottle > 0:
        if num_bottle > 1:
            print(f"{num_bottle} bottles of beer on the wall, {num_bottle} bottles of beer.")
            if num_bottle - 1 == 1:
                print(f"Take one down, pass it around, {num_bottle-1} bottle of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, {num_bottle-1} bottles of beer on the wall.\n")
        else:
            print(f"{num_bottle} bottle of beer on the wall, {num_bottle} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
        num_bottle -= 1