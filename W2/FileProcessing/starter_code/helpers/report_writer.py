from datetime import datetime

def write_summary_report(filepath: str, valid_records: list, errors: list, aggregations):
    """
    Write a formatted summary report.
    
    Report should include:
    - Processing timestamp
    - Total records processed
    - Number of valid records
    - Number of errors (with details)
    - Sales by store
    - Top 5 products
    """
    try:
        with open(filepath + "/summary_report.txt", "w", encoding="utf-8") as f:
            f.write("=== Sales Processing Report ===\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            num_valid = len(valid_records)
            num_error = len(errors)
            f.write(f"\nProcessing Statistics:\n")
            f.write(f"- Total records: {num_valid + num_error}\n")
            f.write(f"- Valid records: {num_valid}\n")
            f.write(f"- Error records: {num_error}\n")
            f.write("\nErrors:\n")
            for error in errors:
                f.write(f"- Line {error[0]}: {str(error[1])}\n")
            f.write("\nSales by Store:\n")
            for key, value in aggregations[0].items():
                f.write(f"- {key}: ${value}\n")
            f.write("\nTop Products:\n")
            top_products = sorted(aggregations[1].items(), key=lambda item: item[1], reverse=True)
            for i, prod in enumerate(top_products, 1):
                if i > 5:
                    break
                f.write(f"{i}. {prod[0]}: {prod[1]} units\n")
            
    except Exception as e:
        raise Exception(e)
    finally:
        if not f.closed:
            f.close()

def write_clean_csv(filepath, records):
    """
    Write validated records to a clean CSV file.
    """
    try:
        with open(filepath + "/sample_sales_cleaned.csv", "w", encoding="utf-8") as f:
            f.write("date, store_id, prduct, quantity, price\n")
            for record in records:
                f.write(f"{record["date"]},{record["store_id"]},{record["product"]},{record["quantity"]},{record["price"]}\n")
    except Exception as e:
        raise Exception(e)
    finally:
        if not f.closed:
            f.close()

def write_error_log(filepath, errors):
    """
    Write processing errors to a log file.
    """
    try:
        with open(filepath + "/errors.log", "w", encoding="utf-8") as f:
            f.write("="*20 + " PROCESSING ERRORS " + "="*20 + "\n")
            for error in errors:
                f.write(f'Line {error[0]}: {str(error[1])}\n')
    except Exception as e:
        raise Exception(e)
    finally:
        if not f.closed:
            f.close()