# Standard Imports
import sys

# External Imports
import readchar


if __name__ == '__main__':
    # This tests the 'Emulation -> Emulate Terminal In Output Console' option
    # Test this with 'Run' (Shift + F10) and then 'Debug' (Shift + F9)
    # Only 'Run' behavior is working properly, 'Debug' doesn't because it doesn't
    # return after a single key press

    # Let's try to read a single character like »A«, as expected
    # Press the »A« key if on 'Run'
    # If on 'Debug' it won't return so press »A« then »ENTER«

    # sys.stdin.flush()  # Uncomment flushing just in case if you think it makes a difference

    key = readchar.readchar()

    assert(key == 'a')
    print("Got the expected A")

