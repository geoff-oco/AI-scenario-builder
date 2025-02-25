import random

def roomNumber(size):

    rooms = 0

    if size == "small":
        rooms = random.randint(4, 6)
    elif size == "medium":
        rooms = random.randint(7, 9)
    elif size == "large":
        rooms = random.randint(10, 15)

    return rooms
