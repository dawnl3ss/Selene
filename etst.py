import time
import sys

toolbar_width = 3

# setup toolbar
sys.stdout.write("✦ Dumping %s" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in range(toolbar_width):
    time.sleep(1) # do real work here
    # update the bar
    sys.stdout.write(".")
    sys.stdout.flush()

sys.stdout.write("\n") # this ends the progress bar