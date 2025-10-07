# Driving Log Generator

This script generates a **simulated** driving log in CSV format with **fictional data**. It does NOT record actual distances driven. Instead, it creates synthetic records of daily commutes using randomly generated numbers based on a normal distribution centered around user-configured default values. The tool produces these fictional entries for weekdays within a specified date range, automatically excluding public holidays.

## Features

- **Custom Date Range**: Specify the exact start and end dates for the report using command-line arguments.
- **Holiday Exclusion**: Automatically skips log entries for public holidays in South Korea.
- **Synthetic Data Generation**: Uses a normal distribution to generate random, fictional distances centered around the user-configured default values (not actual driving data).
- **CSV Output**: Saves the final report to an `output.csv` file for easy use in spreadsheets or data analysis tools.

## Prerequisites

Before running the script, you need to have Python 3 and the following Python libraries installed:

- `python-dateutil`: For robustly parsing date strings.
- `holidays`: For identifying public holidays.

## Installation

### 1. Create and activate virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

Install the necessary libraries using pip:
```bash
pip install -r requirements.txt
```

Alternatively, install manually:
```bash
pip install python-dateutil holidays
```

## How to Run

Execute the script from your command line, providing the start and end dates as arguments:
```bash
python main.py --from YYYY-MM-DD --to YYYY-MM-DD
```

For example:
```bash
python main.py --from 2025-01-01 --to 2025-06-30
```

The script will process the information and generate an `output.csv` file in the same directory.

## Configuration

You can customize the script's behavior by editing the `config.json` file. The following parameters are available:

- `typical_distance`: The average distance of a one-way commute in kilometers.
- `error_percentage`: The maximum random variation to apply to the distance (e.g., 0.20 for 20%).
- `home_location`: The name of the starting location for the morning commute.
- `office_location`: The name of the destination for the morning commute.
- `holiday_country`: The two-letter country code for which to exclude public holidays (e.g., "KR" for South Korea, "US" for the United States).

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

## Deactivate Virtual Environment

When you're done working on the project:

```bash
deactivate
```

## Project Structure

```
drivinglog/
├── main.py              # Main script
├── config.json          # Configuration file
├── requirements.txt     # Python dependencies
├── README.md            # This file
├── .gitignore           # Git ignore rules
├── venv/                # Virtual environment (not tracked in git)
└── output-*.csv         # Generated output files (not tracked in git)
```
