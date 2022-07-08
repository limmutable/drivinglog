# import modules used here -- sys is a very standard one
import sys
import random

# Gather our code in a main() function
def main():
    print ('Running', sys.argv[0], "...")
    print ('Generating', sys.argv[1], 'random number(s) ...')
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored
    i=0
    repeat = sys.argv[1]
    for i in range(int(repeat)):
        print(random.random())
        i = i + 1

# Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
    main()