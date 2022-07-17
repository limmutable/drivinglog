# import modules used here -- sys is a very standard one
import sys
import random
from datetime import datetime
from datetime import timedelta
import csv

def generateRandom():
        a = random.random()
        # generate a random integer between 0 - 3
        #print(a)
        #print(int(a*4))
        return (int(a*4))


# Generating a driving record file (csv format)
# Date (YYYY-MM-DD), From, To, Distance
# Example of a raw: "2022-07-24, 집, 회사, 24"

def generateReport():
    # initialization and user inputs
    # Enter start date here and how many days to run
    startdate = datetime(2022, 1, 1)
    howmanydays = 10

    # console output
    print("Generating a report from " + startdate.strftime('%Y-%m-%d') + " for " + str(howmanydays) + " days")
    
 
    with open('output.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # csv header row
        header = ['Date', 'From', 'To', 'Distance']
        # write the header
        writer.writerow(header)

        day = 0
        d = startdate

        for day in range(howmanydays):
            # print("writing " + d.strftime('%Y-%m-%d'))

            # base work-home route = 24km, then add some extra random distance
            entry1 = [d.strftime('%Y-%m-%d'), 'Home', 'Work', str(24+generateRandom())]
            entry2 = [d.strftime('%Y-%m-%d'), 'Work', 'Home', str(24+generateRandom())]
            # write the data from Home to Work
            writer.writerow(entry1)
            # write the data from Work to Home
            writer.writerow(entry2)

            d = d + timedelta(days = 1)
            day = day + 1

# Gather our code in a main() function
def main():
    generateReport()


# Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
    main()

