# import modules used here -- sys is a very standard one
import sys
import random
from datetime import datetime
import csv

def getToday():
    return datetime.today().strftime('%Y-%m-%d')

def generateRandom():
    print ('Running', sys.argv[0], "...")
    print ('Generating', sys.argv[1], 'random number(s) ...')
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored
    i=0

    repeat = sys.argv[1]
    for i in range(int(repeat)):
        a=random.random()
        print(a)
        i = i + 1

# Generating a driving record file (csv format)
# Date (YYYY-MM-DD), From, To, Distance
# Example of a raw: "2022-07-24, 집, 회사, 24"

def generateReport():
    print("Generating a report...")
    
    header = ['Date', 'From', 'To', 'Distance']
    data1 = [getToday(), 'Home', 'Work', '24']
    data2 = [getToday(), 'Work', 'Home', '22']

    with open('output.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write the data from Home to Work
        writer.writerow(data1)

        # write the data from Work to Home
        writer.writerow(data2)

# Gather our code in a main() function
def main():
    getToday()
#    generateRandom()
    generateReport()


# Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
    main()

