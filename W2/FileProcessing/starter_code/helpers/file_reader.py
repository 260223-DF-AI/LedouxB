from .exceptions import FileProcessingError
from json import load

def read_csv_file(filepath) -> list:
    """
    Read a CSV file and return a list of dictionaries.
    
    Should handle:
    - FileNotFoundError
    - UnicodeDecodeError (try utf-8, then latin-1)
    - Empty files
    
    Returns: List of dictionaries (one per row)
    Raises: FileProcessingError with descriptive message
    """
    try:
        f = None
        with open(filepath, 'r', encoding='utf-8') as f:
            content = []
            for i, l in enumerate(f):
                if i == 0: # skip column names
                    continue
                line = l.split(',')
                content.append({
                    'date': line[0],
                    'store_id': line[1],
                    'product': line[2],
                    'quantity': line[3],
                    'price': line[4].removesuffix('\n'),
                    # 'price': ((float(line[4]) * 100) // 1) / 100 # making sure prices only have two decimal places
                })
            if not content:
                return []
            return content
    except FileNotFoundError as e:
        msg = f"File not found: {e}"
        raise FileProcessingError(msg)
    except UnicodeDecodeError as e:
        msg = f"Unicode decode error: {e}"
        raise FileProcessingError(msg)
    except Exception as e:
        msg = f"Unhandled exception occured: {e}"
        raise Exception(msg)
    finally:
        if f is not None and not f.closed:
            f.close()
    return []

def read_json_file(filepath) -> list:
    """
    Read a JSON file and return a list of dictionaries.
    
    Should handle:
    - FileNotFoundError
    - UnicodeDecodeError (try utf-8, then latin-1)
    - Empty files
    
    Returns: List of dictionaries (one per row)
    Raises: FileProcessingError with descriptive message
    """
    try:
        f = None
        with open(filepath, 'r', encoding='utf-8') as f:
            content = load(f)
            if not content:
                return []
            return content
    except FileNotFoundError as e:
        msg = f"File not found: {e}"
        raise FileProcessingError(msg)
    except UnicodeDecodeError as e:
        msg = f"Unicode decode error: {e}"
        raise FileProcessingError(msg)
    except Exception as e:
        msg = f"Unhandled exception occured: {e}"
        raise Exception(msg)
    finally:
        if f is not None and not f.closed:
            f.close()
    return []