# Driving Log Generator

This script generates a simulated driving log in CSV format. It creates a record of daily commutes by prompting the user for a start and end date, calculating distances for weekdays while excluding public holidays.

## Features

- **Custom Date Range**: Specify the exact start and end dates for the report interactively.
- **Flexible Date Input**: Accepts various date formats (e.g., "2023-01-01", "Jan 1, 2023", "01/01/2023").
- **Holiday Exclusion**: Automatically skips log entries for public holidays in South Korea.
- **Realistic Data**: Simulates slight, random variations in daily commute distances to appear more realistic.
- **CSV Output**: Saves the final report to an `output.csv` file for easy use in spreadsheets or data analysis tools.

## Prerequisites

Before running the script, you need to have Python 3 and the following Python libraries installed:

- `python-dateutil`: For robustly parsing date strings.
- `holidays`: For identifying public holidays.

## Installation

1.  Ensure you have Python 3 installed on your system.
2.  Install the necessary libraries using pip:
    ```bash
    pip install python-dateutil holidays
    ```

## How to Run

1.  Execute the script from your command line:
    ```bash
    python main.py
    ```
2.  When prompted, enter the desired start date for the log and press Enter.
3.  Next, enter the end date and press Enter.

The script will process the information and generate an `output.csv` file in the same directory.

## Output File

The script will create a file named `output.csv` with the following columns:

- `Date`: The date of the trip in `YYYY-MM-DD` format.
- `From`: The departure location (always "Home" or "Office").
- `To`: The destination location.
- `Distance`: The distance of the trip in kilometers.

### Example `output.csv`:

```csv
Date,From,To,Distance
2024-03-04,Home,Office,28.16
2024-03-04,Office,Home,32.89
2024-03-05,Home,Office,25.82
2024-03-05,Office,Home,23.86
```