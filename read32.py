"""
read32.py is a slightly extended and polished version of the script we
developed together (i.e., `seuss6.py`).

Handout code for CS32 pset 1, part 1.
"""
import sys

# Grab the filename of the book we want to read from the command line
if (len(sys.argv) == 2):
    book = sys.argv[1]
else:
    sys.exit("Usage: python3 read32.py book.txt")

with open(book) as my_open_book:
    # Set our FSM to the start state
    looking_for_open_quote = True

    while True:
        the_line = my_open_book.readline()

        if the_line == '':
            # We've read the entire book!
            print("\nThe End.")
            break

        if looking_for_open_quote:  # in state S0
            i = the_line.find('"')
            if i != -1:
                # Found an open quote.  Optimistically grab the
                # rest of the buffer as dialogue.
                dialog = the_line[i:]
                if '"' not in dialog[1:]:
                    # Rest of line was the dialogue.  Transition to S1.
                    looking_for_open_quote = False
                else:
                    # Grab and print the dialogue from this line.  Stay
                    # in state S0.
                    short_dialog = dialog[1:].split('"')[0]
                    print("\nACTOR: " + '"' + short_dialog + '"')

        else:                       # in state S1
            i = the_line.find('"')
            if i != -1:
                # Found a close quote.  Grab the last bit of the line of
                # dialogue we've been collecting, and print it.
                # Transition to S0.
                dialog += the_line[:i+1]
                print("\nACTOR:", dialog)
                looking_for_open_quote = True
            else:
                # No close quote in the line buffer
                dialog += the_line
