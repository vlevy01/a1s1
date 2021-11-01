import os
import sys

# Import the appropriate test-specific file
from testread32 import *
from testcount32 import *

# Default paths and filenames
python = "/usr/local/bin/python3"

# Class for helping to print with color in the terminal window.  Use
# by writing `print(color.RED + "output text" + color.END)`
class color:
    BLACK = '\033[1;30;48m'
    RED = '\033[1;31;48m'
    GREEN = '\033[1;32;48m'
    YELLOW = '\033[1;33;48m'
    BLUE = '\033[1;34;48m'
    PURPLE = '\033[1;35;48m'
    CYAN = '\033[1;36;48m'
    BOLD = '\033[1;37;48m'
    UNDERLINE = '\033[4;37;48m'
    END = '\033[1;37;0m'


def test_failed(msg):
    """
    Let the user know that a particular test failed and how
    it failed.  The name of the test should be embedded in
    the `msg` string.
    """
    print(color.RED + "FAILED:" + color.END, end=" ")
    print(msg)


def test_passed(msg):
    """
    Let the user know that a particular test passed successfully.
    The name of the test should be embedded in the `msg` string.
    """
    print(color.GREEN + "PASSED:" + color.END, end=" ")
    print(msg)


def launch_test(cmdline):
    """
    Given a cmdline that is a test_prog and its args list, run the
    cmdline in a child process and return the child's pid
    to the caller.
    """
    pid = os.fork()
    if pid == 0:
        # child process

        # Redirect stdout
        fd = os.open(testout, os.O_WRONLY | os.O_CREAT | os.O_TRUNC)
        os.dup2(fd, 1)
        os.close(fd)

        # Launch the program to test
        os.execvp(cmdline[0], cmdline)

        # It's an error if we get here
        print(f"ERROR: execlp failed for {cmdline[0]}", file=sys.stderr)
        os._exit(0)

    # parent process continues here
    return pid


def main():
    """python3 tester.py [-v]

    Runs specific tests based on the coded configuration in the
    `tester-{module}.py` file.  If the optional `-v` flag is used,
    the output of each test is printed.
    """
    if len(sys.argv) == 2:
        verbose = True
    else:
        verbose = False
    
    for test in tests:
        # Create the test command line
        inputfile = os.path.join(inputdir, test[0])
        cmdline = [python, testme, inputfile]

        # Let the user know what we're doing
        print(f"\nRunning: {' '.join(cmdline)}")
        
        #  Start the tested program
        child_pid = launch_test(cmdline)

        # Wait for the tested program to complete its work
        pid, status = os.waitpid(child_pid, 0)
        if not os.WIFEXITED(status) or os.WEXITSTATUS(status) != 0:
            test_failed(f"test `{test[0]}` exited abnormally " +
                        f"with status {os.WEXITSTATUS(status)}")
            continue
        # else tested program completed so let's check its output

        # Grab the output of the tested program
        with open(testout, 'r') as f:
            try:
                contents = f.read()
            except OSError:
                test_failed(f"unable to read output of test `{test[0]}`")
                continue
        
        if verbose:
            # Let the user see the tested program's output
            print(contents)

        # Check actual output against expected output.
        output_ok, msg = check_output(test, contents)
        if output_ok:
            test_passed(msg)
        else:
            test_failed(msg)

if __name__ == '__main__':
    main()
