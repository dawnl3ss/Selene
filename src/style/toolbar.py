import time
import sys

def make_bar(toolbar_width):
    sys.stdout.write("✦ Dumping %s" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))

    for i in range(toolbar_width):
        time.sleep(1)
        sys.stdout.write(".")
        sys.stdout.flush()

    sys.stdout.write("\n")

def print_time(message):
    sys.stdout.write("%s" % (" " * len(message)))
    sys.stdout.flush()
    sys.stdout.write("\b" * (len(message) + 1))

    for i in range(len(message)):
        time.sleep(.05)
        sys.stdout.write(message[i])
        sys.stdout.flush()

    sys.stdout.write("\n")