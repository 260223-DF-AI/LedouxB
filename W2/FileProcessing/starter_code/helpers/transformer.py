def calculate_totals(records: list) -> list:
    """
    Calculate line totals (quantity * price) for each record.
    Returns: Records with added 'total' field
    """
    for record in records:
        record["total"] = round(record["quantity"] * record["price"], 2)
    return records

def aggregate_by_store(records: list) -> dict:
    """
    Aggregate sales by store_id.
    Returns: Dict mapping store_id to total sales
    """
    aggregate_sales = {}
    for record in records:
        id = record["store_id"]
        if id in aggregate_sales.keys():
            aggregate_sales[id] += record["total"]
        else:
            aggregate_sales[id] = record["total"]
    return aggregate_sales

def aggregate_by_product(records: list) -> dict:
    """
    Aggregate sales by product.
    Returns: Dict mapping product to total quantity sold
    """
    aggregate_sales = {}
    for record in records:
        prod = record["product"]
        if prod not in aggregate_sales.keys():
            aggregate_sales[prod] = record["quantity"]
        else:
            aggregate_sales[prod] += record["quantity"]
    return aggregate_sales