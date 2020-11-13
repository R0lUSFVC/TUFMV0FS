import time
import sys
import os

# Get the size
# of the terminal
size = os.get_terminal_size()


# Print the size
# of the terminal
print(str(size))

def spinning_cursor():
  while True:
    for cursor in '\\|/-':
      time.sleep(0.1)
      # Use '\r' to move cursor back to line beginning
      # Or use '\b' to erase the last character
      sys.stdout.write('\r{}'.format(cursor))
      # Force Python to write data into terminal.
      sys.stdout.flush()

def progress_bar1():
    toolbar_width = 210

    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

    for i in range(toolbar_width):
        time.sleep(0.1) # do real work here
        # update the bar
        sys.stdout.write("#")
        sys.stdout.flush()

    sys.stdout.write("]\n") # this ends the progress bar


def progress_bar2():
  for i in range(100):
    time.sleep(0.1)
    s = sys.stdout.write('\r{:02d}: {}'.format(i, '#' * (i//2)))
    sys.stdout.flush()
    
if __name__ == '__main__':
    print(progress_bar1())
