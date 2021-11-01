with open('Snowman.txt') as my_open_book:
    # Set our FSM to the start state
    looking_for_open_quote = True

    while True:
        the_line = my_open_book.readline()

        if the_line == '':
            # We've read the entire book!
            print("\nThe End.")
            break

        # new pseudocode goes here
        if looking_for_open_quote:  # in state S0
            i = the_line.find('"')
            if i != -1:
                # Found an open quote
                dialog = the_line[i:]
                if '"' not in dialog[1:]:
                    looking_for_open_quote = False
                else:
                    # Grab entire dialog from this line ...
                    short_dialog = dialog[1:].split('"')[0]
                    print("\nACTOR: " + '"' + short_dialog + '"')
                    # ... and stay in state S0

        else:
            i = the_line.find('"')
            if i != -1:
                # Found a close quote
                dialog += the_line[:i+1]
                print("\nACTOR:", dialog)
                looking_for_open_quote = True
            else:
                dialog += the_line
            # FIXME! Is this all the work in state S1?
