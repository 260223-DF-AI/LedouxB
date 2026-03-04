from helpers import *
import sys
import logging

def process_sales_file(input_path: str, output_dir: str):
    """
    Main processing pipeline.
    
    1. Read the input file
    2. Validate all records
    3. Transform valid records
    4. Generate reports
    5. Handle any errors gracefully
    
    Returns: ProcessingResult with statistics
    """
    logging.basicConfig(
        level=logging.WARNING,
        format='%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d ----- %(message)s',
        filename='app.log',
        filemode='w',
    )
    try:
        if input_path.endswith(".csv"):
            data: list = read_csv_file(input_path)
        elif input_path.endswith(".json"):
            data: list = read_json_file(input_path)
        validated_records, errors = validate_all_records(data)
        records_totals = calculate_totals(validated_records)
        aggregates_stores = aggregate_by_store(records_totals)
        aggregates_products = aggregate_by_product(records_totals)
        write_summary_report(output_dir, records_totals, errors, (aggregates_stores, aggregates_products))
        write_clean_csv(output_dir, validated_records) # not using totalled records in case we want to reuse the new file and revcalculate totals (dont want them compounding)
        write_error_log(output_dir, errors)
    except FileProcessingError as e:
        logging.error(e)
    except Exception as e:
        logging.error("An error occurred:", exc_info=True)

if __name__ == "__main__":
    # Process from command line
    process_sales_file(input_path=sys.argv[1], output_dir=sys.argv[2])