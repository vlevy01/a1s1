with open('txts/CatInTheHat.txt') as my_open_book:
    while True:
        the_line = my_open_book.readline()

        if the_line == '':
            # We've read the entire book!
            print("\nThe End.")
            break

        # new pseudocode goes here