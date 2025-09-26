# import modules used here -- sys is a very standard one
import sys
import random
import datetime
from datetime import timedelta
import holidays
import csv
from dateutil.parser import parse
import argparse
import json

# Generating a driving record file (csv format)
# Date (YYYY-MM-DD), From, To, Distance
# Example of a raw: "2022-07-24, Home, Office, 24"

def generateReport(start_date, end_date):
    # Load configuration
    with open('config.json', 'r') as f:
        config = json.load(f)

    typical_distance = config['typical_distance']
    error_percentage = config['error_percentage']
    home_location = config['home_location']
    office_location = config['office_location']
    holiday_country = config['holiday_country']

    # console output
    print("Generating a report from " + start_date.strftime('%Y-%m-%d') + " to " + end_date.strftime('%Y-%m-%d') + ".")

    # Initialize the list of holidays
    country_holidays = holidays.country_holidays(holiday_country)

    # Generate the driving log
    driving_log = []

    current_date = start_date
    while current_date <= end_date:
        # Check if the current date is a weekday (Monday to Friday) and not a holiday
        if current_date.weekday() < 5 and current_date not in country_holidays:
            # Calculate the actual distance with random error
            actual_distance1 = typical_distance * (1 + random.uniform(-error_percentage, error_percentage))
            # Add the log entry
            log_entry1 = {
                "Date": current_date.strftime("%Y-%m-%d"),
                "Departure": home_location,
                "Destination": office_location,
                "Distance Driven": round(actual_distance1, 2),
            }
            driving_log.append(log_entry1)

            actual_distance2 = typical_distance * (1 + random.uniform(-error_percentage, error_percentage))
            # Add the log entry
            log_entry2 = {
                "Date": current_date.strftime("%Y-%m-%d"),
                "Departure": office_location,
                "Destination": home_location,
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
    parser = argparse.ArgumentParser(description='Generate a driving log.')
    parser.add_argument('--start', required=True, help='The start date in YYYY-MM-DD format.')
    parser.add_argument('--end', required=True, help='The end date in YYYY-MM-DD format.')
    args = parser.parse_args()

    try:
        start_date = parse(args.start).date()
        end_date = parse(args.end).date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)

    generateReport(start_date, end_date)

# Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
    main()
