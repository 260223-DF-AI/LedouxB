from .exceptions import InvalidDataError, MissingFieldError
import re

def validate_sales_record(record: dict, line_number: int):
    """
    Validate a single sales record.
    
    Required fields: date, store_id, product, quantity, price
    Validation rules:
    - date must be in YYYY-MM-DD format
    - quantity must be a positive integer
    - price must be a positive number
    
    Returns: Validated record with converted types
    Raises: InvalidDataError or MissingFieldError
    """
    try:
        fields = ["date", "store_id", "product", "quantity", "price"]
        for field in fields:
            if not record[field]:
                msg = f"Missing required field {field}"
                raise MissingFieldError(msg)
        # Date
        if not re.search(r"^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$", record["date"]):
            msg = f"Invalid date '{record["date"]}'"
            raise InvalidDataError(msg)
        # Store ID
        if not re.search(r"^STORE[0-9]{3}$", record["store_id"]):
            msg = f"Invalid store ID '{record["store_id"]}'"
            raise InvalidDataError(msg)
        # Quantity
        try:
            quantity = int(record["quantity"])
            if quantity <= 0:
                msg = f"Quantity must be positive, got {quantity}"
                raise InvalidDataError(msg)
            if quantity != float(record["quantity"]): #non-pos value or not int (typecast to int will omit decimal places)
                msg = f"Quantity must be an integer, got {record["quantity"]}"
                raise InvalidDataError(msg)
            record["quantity"] = quantity
        except ValueError as e:
            msg = f"Invalid quantity '{record["quantity"]}'"
            raise InvalidDataError(msg)
        # Price
        try:
            price = float(record["price"])
            if price <= 0:
                msg = f"Price must be positive, was {price}"
                raise InvalidDataError(msg)
            if price * 100 != (price * 100 // 1): #non-pos value or not int (typecast to int will omit decimal places)
                msg = f"Price must contain no more than two decimals, got {price}"
                raise InvalidDataError(msg)
            record["price"] = price
        except ValueError as e:
            msg = f"Invalid price '{record["price"]}'"
            raise InvalidDataError(msg)
        return record
    except InvalidDataError as e:
        # msg = f"Data was not able to be formatted correctly: {e}"
        raise InvalidDataError(e)
    except MissingFieldError as e:
        # msg = f"One of the fields was missing from the input: {e}"
        raise MissingFieldError(e)

def validate_all_records(records):
    """
    Validate all records, collecting errors instead of stopping.
    
    Returns: Tuple of (valid_records, error_list)
    """
    valid_records = []
    error_list = []
    for i, record in enumerate(records):
        try:
            validated_record = validate_sales_record(record, i)
            valid_records.append(validated_record)
        except InvalidDataError as e:
            error_list.append((i, e))
        except MissingFieldError as e:
            error_list.append((i, e))
    return (valid_records, error_list)
