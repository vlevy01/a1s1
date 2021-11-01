"""
Module that tests cs32/a1s1/read32.py

DIRECTIONS: Find and replace every instance of "FIXME" with the name of
the Python program you want to test.  Then fill out the `tests` list and
rewrite the routine `check_output`.
"""

# Test-specific paths and filenames
testme = "/Users/profsmith/cs32/a1s1/read32.py"
inputdir = "/Users/profsmith/cs32/a1s1"
testout = "tester.out"

# The tests. Tuple of input filename and expected output.
tests = [
    ['txts/Hat.txt', 'txts/Hat-soln1.txt'],
    ['txts/Importnt.txt', 'txts/Importnt-soln1.txt'],
    ['txts/Snowman.txt', 'txts/Snowman-soln1.txt'],
    ['txts/JustDavid-excerpt.txt', 'txts/JustDavid-excerpt-soln1.txt'],
    ['txts/TheThreeBears.txt', 'txts/TheThreeBears-soln1.txt']
]

def check_output(test, test_output):
    """
    Check the actual output (`test_output`) against the expected output for
    the indicated `test`, which is one of the list entries in `tests` above.
    Return a tuple, where the first item is whether the match was successful
    or not and the second item is any message you want printed for
    the user.
    """
    # This routine checks for string equality, and if unequal, reports the
    # index of the first mismatched character.
    with open(test[1], 'r') as f:
        expected_output = f.read()

    # Loop over the smaller of the two outputs
    n_test = len(test_output)
    n_expected = len(expected_output)
    n = min(n_test, n_expected)

    # Keep track of number of lines successfully compared to make
    # it easier to tell the user where a problem is.
    line_num = 1
    chars_before_cur_line = 0

    for i in range(n):
        if test_output[i] != expected_output[i]:
            char_num = i - chars_before_cur_line + 1
            err_msg = (test[0] + ': mismatch at line ' +
                       str(line_num) + ', char ' + str(char_num))
            return (False, err_msg)
        if test_output[i] == '\n':
            line_num += 1
            chars_before_cur_line = i + 1

    if n_test != n_expected:
            char_num = n - chars_before_cur_line + 1
            err_msg = (test[0] + ': mismatch at line ' +
                       str(line_num) + ', char ' + str(char_num))
            return (False, err_msg)

    return (True, f"{test[0]}")
