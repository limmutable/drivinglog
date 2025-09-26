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

def load_config():
    """Loads the configuration from config.json."""
    with open('config.json', 'r') as f:
        return json.load(f)

def generate_log_entries(start_date, end_date, config):
    """Generates the driving log entries."""
    holiday_country = config['holiday_country']
    country_holidays = holidays.country_holidays(holiday_country)
    typical_distance = config['typical_distance']
    error_percentage = config['error_percentage']
    home_location = config['home_location']
    office_location = config['office_location']

    driving_log = []
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5 and current_date not in country_holidays:
            # Morning commute
            distance1 = typical_distance * (1 + random.uniform(-error_percentage, error_percentage))
            driving_log.append({
                "Date": current_date.strftime("%Y-%m-%d"),
                "Departure": home_location,
                "Destination": office_location,
                "Distance Driven": round(distance1, 2),
            })

            # Evening commute
            distance2 = typical_distance * (1 + random.uniform(-error_percentage, error_percentage))
            driving_log.append({
                "Date": current_date.strftime("%Y-%m-%d"),
                "Departure": office_location,
                "Destination": home_location,
                "Distance Driven": round(distance2, 2),
            })
        current_date += timedelta(days=1)
    return driving_log

def write_csv(driving_log):
    """Writes the driving log to output.csv."""
    with open('output.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        header = ['Date', 'From', 'To', 'Distance']
        writer.writerow(header)
        for entry in driving_log:
            writer.writerow([entry['Date'], entry['Departure'], entry['Destination'], entry['Distance Driven']])
    print("Saved the output in output.csv")

def print_log(driving_log):
    """Prints the driving log to the console."""
    for entry in driving_log:
        print(f"Date: {entry['Date']}, Departure: {entry['Departure']}, Destination: {entry['Destination']}, Distance Driven: {entry['Distance Driven']} km")

def generate_report(start_date, end_date):
    """Main function to generate the report."""
    print(f"Generating a report from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}.")
    config = load_config()
    driving_log = generate_log_entries(start_date, end_date, config)
    print_log(driving_log)
    write_csv(driving_log)

def main():
    parser = argparse.ArgumentParser(description='Generate a driving log.')
    parser.add_argument('--from', required=True, help='The start date for the report (e.g., YYYY-MM-DD).')
    parser.add_argument('--to', required=True, help='The end date for the report (e.g., YYYY-MM-DD).')
    args = parser.parse_args()

    try:
        start_date = parse(getattr(args, 'from')).date()
        end_date = parse(args.to).date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)

    generate_report(start_date, end_date)

if __name__ == '__main__':
    main()