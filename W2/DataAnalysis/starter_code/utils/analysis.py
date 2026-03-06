import pandas as pd

def load_data(filepath):
    """
    Load the orders dataset.
    - Parse dates correctly
    - Handle missing values
    - Return a clean DataFrame
    """
    df = pd.read_csv(filepath)
    clean_data(df)
    explore_data(df)



def explore_data(df):
    """
    Print basic statistics about the dataset:
    - Shape (rows, columns)
    - Data types
    - Missing value counts
    - Basic statistics for numeric columns
    - Date range covered
    """
    print(f"Shape: {df.shape}")
    print(f"Data types: {df.dtypes}")
    print(f"Missing values: {df.isnull().sum()}")
    print(f"Average order quantity: {df["quantity"].mean()}")
    print(f"Average product price: {df["price"].mean()}")
    print(f"Date range: {df["order_date"].min()} to {df["order_date"].max()}")

def clean_data(df):
    """
    Clean the dataset:
    - Remove duplicates
    - Fill or drop missing values (document your strategy)
    - Standardize text columns (strip whitespace, consistent case)
    - Add calculated columns: 'total_amount' = quantity * unit_price
    """
    df.drop_duplicates()

    # Fill/Drop Strategy: Anything filled is not considered critical to records and should not result in a dropped entry
    # order_id: Fill w/ 0000
    df["order_id"].fillna("0000")
    # customer_id: Fill w/ C000
    df["customer_id"].fillna("C000")
    # order_date: Fill w/ unix common epoch
    df["order_date"].fillna("1970-01-01")
    # product_name: Fill w/ generic product name "Product"
    df["product_name"].fillna("Product")
    # category: Fill w/ "Miscellaneous"
    df["category"].fillna("Miscellaneous")
    # quantity: Fill w/ 1
    df["quantity"].fillna(1)
    # unit_price: Drop, could find entry with matching product_name and guess price based on quantity and price in the future
    df.dropna(subset=["unit_price"])
    # region: Fill w/ "Global" as general coverage. NOTE: Interplanetary locations will be grouped in if missing region value
    df["region"].fillna("Global")

    df["order_date"] = pd.to_datetime(df["order_date"])
    df["product_name"] = df["product_name"].str.lower().str.strip()
    df["category"] = df["category"].str.capitalize().str.strip()
    df["region"] = df["region"].str.capitalize().str.strip()

    df["total_amount"] = df["quantity"] * df["unit_price"]

    return df

def add_time_features(df):
    """
    Add time-based features:
    - day_of_week (0=Monday, 6=Sunday)
    - month
    - quarter
    - is_weekend (boolean)
    """
    df["day_of_week"] = df["datetime"].dt.dayofweek
    df["month"] = df["datetime"].dt.month
    df["quarter"] = df["datetime"].dt.quarter
    df["is_weekend"] = df["day_of_week"] >= 5

def sales_by_category(df):
    """
    Calculate total sales and order count by category.
    Returns: DataFrame with columns [category, total_sales, order_count, avg_order_value]
    Sorted by total_sales descending.
    """
    sales = pd.DataFrame()
    sales["category"] = df["category"].unique()
    sales["total_sales"] = df.groupby("category")["total_amount"].sum()
    sales["order_count"] = df.groupby("category")["quantity"].sum()
    sales["avg_order_value"] = sales["total_sales"] / sales["order_count"]
    return sales

def sales_by_region(df):
    """
    Calculate total sales by region.
    Returns: DataFrame with columns [region, total_sales, percentage_of_total]
    """
    sales = pd.DataFrame()
    sales["region"] = df["region"].unique()
    sales["total_sales"] = df.groupby("region")["total_amount"].sum()
    sales["percentage_of_total"] = sales["total_sales"] / sales["total_sales"].sum()
    return sales

def top_products(df, n=10):
    """
    Find top N products by total sales.
    Returns: DataFrame with columns [product_name, category, total_sales, units_sold]
    """
    top = pd.DataFrame()
    top["product_name"] = df["product_name"].unique()
    top["category"] = df.groupby("product_name")["category"]
    top["total_sales"] = df.groupby("product_name")["total_amount"].sum()
    top["units_sold"] = df.groupby("product_name")["quantity"].sum()
    return top.sort_values("total_sales", ascending=False).head(n=n)

def daily_sales_trend(df):
    """
    Calculate daily sales totals.
    Returns: DataFrame with columns [date, total_sales, order_count]
    """
    daily = pd.DataFrame()
    daily["date"] = df["order_date"].unique()
    daily["total_sales"] = df.groupby("order_date")["total_amount"].sum()
    daily["order_count"] = df.groupby("order_date")["quantity"].sum()
    return daily

def customer_analysis(df):
    """
    Analyze customer purchasing behavior.
    Returns: DataFrame with columns [customer_id, total_spent, order_count, 
             avg_order_value, favorite_category]
    """
    customers = pd.DataFrame()
    customers["customer_id"] = df["customer_id"].unique()
    customers["total_spent"] = df.groupby("customer_id")["total_amount"].sum()
    customers["order_count"] = df.groupby("customer_id")["quantity"].sum()
    customers["avg_order_value"] = customers["total_spent"] / customers["order_count"]
    customers["favorite_category"] = df.groupby("customer_id")["category"].mode()
    customers.drop(index="C000") #dropping the filler customer made earlier to fill missing customer ids
    return customers

def weekend_vs_weekday(df):
    """
    Compare weekend vs weekday sales.
    Returns: Dict with weekend and weekday total sales and percentages.
    """
    comparison = {
        "weekend": {
            "total_sales": 0,
            "percentage": 0
        },
        "weekdays": {
            "total_sales": 0,
            "percentage": 0
        }
    }
    weekend_sales = df[df["is_weekend"] == True]["total_amount"].sum()
    weekday_sales = df[df["is_weekend"] == False]["total_amount"].sum()
    comparison["weekend"]["total_sales"] = weekend_sales
    comparison["weekend"]["percentage"] = weekend_sales / (weekend_sales + weekday_sales)
    comparison["weekdays"]["total_sales"] = weekday_sales
    comparison["weekdays"]["percentage"] = weekday_sales / (weekend_sales + weekday_sales)

    return comparison