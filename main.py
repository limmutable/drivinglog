# import modules used here -- sys is a very standard one
import sys
import random
import datetime
from datetime import timedelta
import holidays
import csv
from dateutil.parser import parse

# Generating a driving record file (csv format)
# Date (YYYY-MM-DD), From, To, Distance
# Example of a raw: "2022-07-24, Home, Office, 24"

def get_date_from_user(prompt, default_date=None):
    # If user just presses enter, use the default date
    while True:
        default_str = f" [{default_date.strftime('%Y-%m-%d')}]" if default_date else ""
        date_str = input(f"{prompt}{default_str}: ")
        if date_str == "" and default_date:
            return default_date
        try:
            return parse(date_str).date()
        except ValueError:
            print("Invalid date format. Please try again.")

def generateReport():
    # initialization and user inputs
    # Define default date range
    default_start_date = datetime.date(2025, 1, 1)
    default_end_date = datetime.date(2025, 6, 30)
    
    # Get user input with defaults
    start_date = get_date_from_user("Enter the start date", default_start_date)
    end_date = get_date_from_user("Enter the end date", default_end_date)
    # console output
    print("Generating a report from " + start_date.strftime('%Y-%m-%d') + " to " + end_date.strftime('%Y-%m-%d') + ".")

    # Initialize the list of US national holidays
    kr_holidays = holidays.KR()
    #us_holidays = UnitedStates(years=[2023])
    
    # Define the typical commute distance and error percentage
    typical_distance = 24  # km
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

