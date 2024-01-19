# import modules used here -- sys is a very standard one
import sys
import random
import datetime
from datetime import timedelta
import holidays
import csv

# Generating a driving record file (csv format)
# Date (YYYY-MM-DD), From, To, Distance
# Example of a raw: "2022-07-24, Home, Office, 24"

def generateReport():
    # initialization and user inputs
    # Define the date range (December 1st to December 31st, 2023)
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 12, 31)
    # console output
    print("Generating a report from " + start_date.strftime('%Y-%m-%d') + " to " + end_date.strftime('%Y-%m-%d') + ".")

    # Initialize the list of US national holidays
    kr_holidays = holidays.KR()
    #us_holidays = UnitedStates(years=[2023])
    
    # Define the typical commute distance and error percentage
    typical_distance = 28  # km
    error_percentage = 0.20  # allow 20% error

    # Generate the driving log
    driving_log = []

    current_date = start_date
    while current_date <= end_date:
         # Check if the current date is a weekday (Monday to Friday) and not a holiday
        if current_date.weekday() < 5 and current_date not in kr_holidays:
            # Calculate the actual distance with random error
            actual_distance1 = typical_distance * (1 + random.uniform(-error_percentage, error_percentage))
            # Add the log entry
            log_entry1 = {
            "Date": current_date.strftime("%Y-%m-%d"),
            "Departure": "Home",
            "Destination": "Office",
            "Distance Driven": round(actual_distance1, 2),
            }
            driving_log.append(log_entry1)
            
            actual_distance2 = typical_distance * (1 + random.uniform(-error_percentage, error_percentage))
            # Add the log entry
            log_entry2 = {
            "Date": current_date.strftime("%Y-%m-%d"),
            "Departure": "Office",
            "Destination": "Home",
            "Distance Driven": round(actual_distance2, 2),
            }
            driving_log.append(log_entry2)
        # Move to the next day
        current_date += datetime.timedelta(days=1)

    # Print the driving log
    for entry in driving_log:
        print(f"Date: {entry['Date']}, Departure: {entry['Departure']}, Destination: {entry['Destination']}, Distance Driven: {entry['Distance Driven']} km")
 
    with open('output.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # csv header row
        header = ['Date', 'From', 'To', 'Distance']
        # write the header
        writer.writerow(header)
        for entry in driving_log:
            line = [entry['Date'], entry['Departure'], entry['Destination'], entry['Distance Driven']]
            # write the data from Home to Work
            writer.writerow(line)
    print("saved the output in output.csv")
            
# Gather our code in a main() function
def main():
    generateReport()


# Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
    main()

