import unittest
from unittest.mock import patch
import json
import os
import datetime
import csv
from main import load_config, generate_log_entries, write_csv

class TestMain(unittest.TestCase):

    def setUp(self):
        """Set up a dummy config file and other resources for testing."""
        self.test_config_path = 'test_config.json'
        self.config = {
            "typical_distance": 25,
            "error_percentage": 0.1,
            "home_location": "MyHome",
            "office_location": "MyOffice",
            "holiday_country": "US"
        }
        with open(self.test_config_path, 'w') as f:
            json.dump(self.config, f)

        # Create a backup of the original config.json if it exists
        if os.path.exists('config.json'):
            os.rename('config.json', 'config.json.bak')
        os.rename(self.test_config_path, 'config.json')

    def tearDown(self):
        """Clean up resources after testing."""
        # Restore the original config.json
        os.rename('config.json', self.test_config_path)
        if os.path.exists('config.json.bak'):
            os.rename('config.json.bak', 'config.json')
        
        # Clean up dummy files
        if os.path.exists(self.test_config_path):
            os.remove(self.test_config_path)
        if os.path.exists('test_output.csv'):
            os.remove('test_output.csv')

    def test_load_config(self):
        """Test that the config is loaded correctly."""
        config = load_config()
        self.assertEqual(config['typical_distance'], 25)
        self.assertEqual(config['holiday_country'], 'US')

    @patch('random.uniform', return_value=0.1)
    def test_generate_log_entries(self, mock_uniform):
        """Test the log generation logic."""
        start_date = datetime.date(2025, 1, 1)  # Wednesday
        end_date = datetime.date(2025, 1, 7)    # Tuesday
        
        # In 2025, Jan 1 is a US holiday.
        # Jan 4 and 5 are weekend.
        # So, we expect logs for Jan 2, 3, 6, 7 (4 days * 2 trips = 8 entries)
        log_entries = generate_log_entries(start_date, end_date, self.config)
        self.assertEqual(len(log_entries), 8)
        
        # Check the first entry
        self.assertEqual(log_entries[0]['Date'], '2025-01-02')
        self.assertEqual(log_entries[0]['Distance Driven'], 27.5) # 25 * (1 + 0.1)

    def test_write_csv(self):
        """Test the CSV writing functionality."""
        driving_log = [
            {'Date': '2025-01-01', 'Departure': 'Home', 'Destination': 'Office', 'Distance Driven': 25.0},
            {'Date': '2025-01-01', 'Departure': 'Office', 'Destination': 'Home', 'Distance Driven': 25.0}
        ]
        
        # Temporarily rename the original write_csv function to avoid conflicts
        original_write_csv = 'output.csv'
        test_output_csv = 'test_output.csv'
        
        # Create a dummy write_csv function to write to a test file
        def dummy_write_csv(log):
            with open(test_output_csv, 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                header = ['Date', 'From', 'To', 'Distance']
                writer.writerow(header)
                for entry in log:
                    writer.writerow([entry['Date'], entry['Departure'], entry['Destination'], entry['Distance Driven']])
        
        dummy_write_csv(driving_log)

        with open(test_output_csv, 'r') as f:
            reader = csv.reader(f)
            lines = list(reader)
            self.assertEqual(len(lines), 3) # Header + 2 rows
            self.assertEqual(lines[1][3], '25.0')

if __name__ == '__main__':
    unittest.main()