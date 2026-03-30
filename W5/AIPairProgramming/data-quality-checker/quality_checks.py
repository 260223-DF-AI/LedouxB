import pandas as pd


def check_nulls(df: pd.DataFrame) -> dict:
    """Check for null values in each column."""
    if df.empty:
        return {"error": "DataFrame is empty"}
    null_counts = df.isnull().sum()
    return null_counts.to_dict()

def check_duplicates(df: pd.DataFrame, key_column: str) -> dict:
    """Find duplicate rows based on a key column."""
    if df.empty:
        return {"error": "DataFrame is empty"}
    if key_column not in df.columns:
        return {"error": f"Key column '{key_column}' not found in DataFrame"}
    duplicate_rows = df[df.duplicated(subset=[key_column], keep=False)]
    return {"duplicate_count": len(duplicate_rows), "duplicate_rows": duplicate_rows}


def check_negative_values(df: pd.DataFrame, numeric_columns: list) -> dict:
    """Flag negative values in specified numeric columns."""
    if df.empty:
        return {"error": "DataFrame is empty"}
    if not all(col in df.columns for col in numeric_columns):
        return {"error": "One or more numeric columns not found in DataFrame"}
    negative_counts = {}
    for col in numeric_columns:
        negative_counts[col] = (df[col] < 0).sum()
    return negative_counts

def check_future_dates(df: pd.DataFrame, date_column: str) -> dict:
    """Check for dates in the future."""
    if df.empty:
        return {"error": "DataFrame is empty"}
    if date_column not in df.columns:
        return {"error": f"Date column '{date_column}' not found in DataFrame"}
    future_dates = df[df[date_column] > pd.Timestamp.now()]
    return {"future_date_count": len(future_dates), "future_dates": future_dates}

def check_email_format(df: pd.DataFrame, email_column: str) -> dict:
    """Validate email format in the specified column."""
    if df.empty:
        return {"error": "DataFrame is empty"}
    if email_column not in df.columns:
        return {"error": f"Email column '{email_column}' not found in DataFrame"}
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    invalid_emails = df[~df[email_column].str.match(email_pattern, na=False)]
    return {"invalid_email_count": len(invalid_emails), "invalid_emails": invalid_emails}