with open('txts/CatInTheHat.txt') as my_open_book:
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
          # do some work
          for i in range(len(the_line)):
              if the_line[i] == '"':
                  dialog = the_line[i:]
                  break
          if '"' in the_line:
              looking_for_open_quote = False