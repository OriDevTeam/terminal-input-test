# Standard Imports
import sys

# External Imports
import readchar

if __name__ == '__main__':
    # This tests the 'Emulation -> Run with Python Console' option
    # Test this with 'Run' (Shift + F10) and then 'Debug' (Shift + F9)

    # This won't work in both Run / Debug and termios (on linux) will exception with
    # > termios.error: (25, 'Inappropriate ioctl for device')
    # which upon reading the docs, it roughly means that a terminal variable was not set

    key = readchar.readchar()

    assert (key == 'a')
    print("Got the expected A")

