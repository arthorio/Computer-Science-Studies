def show_magicians(magicians):
    for magician in magicians:
        print(magician)
    print("\n")


def make_great(magicians):
    index = 0
    while(index < len(magicians)):
        magicians[index] = f"The Great {magicians[index]}"
        index += 1

    return magicians


def make_great_again(magicians):
    for index in range(len(magicians)):
        magicians[index] += " the Great"

    return magicians





