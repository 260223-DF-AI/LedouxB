import pandas as pd
from pathlib import Path
import json
from datetime import datetime
from quality_checks import *
from ..functions.report_generator import generate_report

def read_data(filepath):
    """Read CSV file"""
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"Error: File {filepath} not found")
        return None

def save_report(report, output_path):
    """Save report to file"""
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(report)

def print_summary(checks):
    """Print summary to console"""
    print("\n=== Data Quality Summary ===")
    print(f"Rows: {checks['shape']['rows']}")
    print(f"Columns: {checks['shape']['columns']}")
    print(f"Duplicate Rows: {checks['duplicate_rows']}")
    print("Missing Values:", checks['missing_values'])

if __name__ == "__main__":
    # Read data
    df = read_data('sample_data.csv')
    
    if df is not None:
        # Run checks
        checks = {
            'nulls': check_nulls(df),
            'duplicate_rows': check_duplicates(df),
            'negative_values': check_negative_values(df),
            'future_dates': check_future_dates(df),
            'email_format': check_email_format(df),
        }
        # Generate report
        report_data = {
            'generated': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'file': 'sample_data.csv',
            'total_rows': df.shape[0],
            'checks': [
                {'name': 'Shape Check', 'status': checks['shape']['status'], 'issues': checks['shape']['issues'], 'details': checks['shape']['details']},
                {'name': 'Duplicate Rows Check', 'status': checks['duplicate_rows']['status'], 'issues': checks['duplicate_rows']['issues'], 'details': checks['duplicate_rows']['details']},
                {'name': 'Missing Values Check', 'status': checks['missing_values']['status'], 'issues': checks['missing_values']['issues'], 'details': checks['missing_values']['details']}
            ]
        }
        report = generate_report(report_data)

        # Save report
        save_report(report, 'output/report.md')
        print("Report saved to output/report.md")
        
        # Print summary
        print_summary(checks)