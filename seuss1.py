my_open_book = open('CatInTheHat.txt')

while True:
    the_line = my_open_book.readline()
    print(the_line, end='')
    if the_line == '':
        # We've read the entire book!
        print("\nThe End.")
        break

my_open_book.close()
