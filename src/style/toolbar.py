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