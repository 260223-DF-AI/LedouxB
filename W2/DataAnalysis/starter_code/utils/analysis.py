import pandas as pd

def load_data(filepath):
    """
    Load the orders dataset.
    - Parse dates correctly
    - Handle missing values
    - Return a clean DataFrame
    """
    df = pd.read_csv(filepath)
    df = clean_data(df)
    print(df)
    return df

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
    print(f"Average product price: {df["unit_price"].mean()}")
    print(f"Date range: {df["order_date"].min()} to {df["order_date"].max()}")

def clean_data(df):
    """
    Clean the dataset:
    - Remove duplicates
    - Fill or drop missing values (document your strategy)
    - Standardize text columns (strip whitespace, consistent case)
    - Add calculated columns: 'total_amount' = quantity * unit_price
    """
    df = df.drop_duplicates()

    df["order_id"] = pd.to_numeric(df["order_id"])
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["product_name"] = df["product_name"].str.lower().str.strip()
    df["category"] = df["category"].str.capitalize().str.strip()
    df["region"] = df["region"].str.capitalize().str.strip()

    # Fill/Drop Strategy: Anything filled is not considered critical to records and should not result in a dropped entry
    # order_id: Fill w/ 0000
    df["order_id"] = df["order_id"].fillna(0)
    # customer_id: Fill w/ C000
    df["customer_id"] = df["customer_id"].fillna("C000")
    # order_date: Fill w/ unix common epoch
    df["order_date"] = df["order_date"].fillna(pd.to_datetime("1970-01-01"))
    # product_name: Fill w/ generic product name "Product"
    df["product_name"] = df["product_name"].fillna("Product")
    # category: Fill w/ "Miscellaneous"
    df["category"] = df["category"].fillna("Miscellaneous")
    # quantity: Fill w/ 1
    df["quantity"] = df["quantity"].fillna(1)
    # unit_price: Drop rows missing unit_price since it is required for calculations
    df = df.dropna(subset=["unit_price"])
    # region: Fill w/ "Global" as general coverage. NOTE: Interplanetary locations will be grouped in if missing region value
    df["region"] = df["region"].fillna("Global")



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
    df["day_of_week"] = df["order_date"].dt.dayofweek
    df["month"] = df["order_date"].dt.month
    df["quarter"] = df["order_date"].dt.quarter
    df["is_weekend"] = df["day_of_week"] >= 5
    return df

def sales_by_category(df):
    """
    Calculate total sales and order count by category.
    Returns: DataFrame with columns [category, total_sales, order_count, avg_order_value]
    Sorted by total_sales descending.
    """
    sales = (
        df.groupby("category", as_index=False)
        .agg(
            total_sales=("total_amount", "sum"),
            order_count=("quantity", "sum")
        )
    )
    sales["avg_order_value"] = sales["total_sales"] / sales["order_count"]
    return sales.sort_values("total_sales", ascending=False).reset_index(drop=True)

def sales_by_region(df):
    """
    Calculate total sales by region.
    Returns: DataFrame with columns [region, total_sales, percentage_of_total]
    """
    sales = (
        df.groupby("region", as_index=False)
        .agg(total_sales=("total_amount", "sum"))
    )
    sales["percentage_of_total"] = (sales["total_sales"] / sales["total_sales"].sum()).round(4) * 100
    return sales.sort_values("total_sales", ascending=False).reset_index(drop=True)

def top_products(df, n=10):
    """
    Find top N products by total sales.
    Returns: DataFrame with columns [product_name, category, total_sales, units_sold]
    """
    top = (
        df.groupby(["product_name", "category"], as_index=False)
        .agg(
            total_sales=("total_amount", "sum"),
            units_sold=("quantity", "sum")
        )
    )
    return top.sort_values("total_sales", ascending=False).head(n=n).reset_index(drop=True)

def daily_sales_trend(df):
    """
    Calculate daily sales totals.
    Returns: DataFrame with columns [date, total_sales, order_count]
    """
    daily = (
        df.groupby("order_date", as_index=False)
        .agg(
            total_sales=("total_amount", "sum"),
            order_count=("quantity", "sum")
        )
    )
    daily = daily.rename(columns={"order_date": "date"})
    return daily.sort_values("date", ascending=True).reset_index(drop=True)

def customer_analysis(df):
    """
    Analyze customer purchasing behavior.
    Returns: DataFrame with columns [customer_id, total_spent, order_count, 
             avg_order_value, favorite_category]
    """
    customers = (
        df.groupby("customer_id", as_index=False)
        .agg(
            total_spent=("total_amount", "sum"),
            order_count=("quantity", "sum"),
            avg_order_value=("total_amount", "sum"), #divide by order count later
            favorite_category=("category", lambda x: pd.Series.mode(x)[0])
        )
    )
    customers["avg_order_value"] = customers["total_spent"] / customers["order_count"]
    
    customers.drop(index="C000", errors="ignore") #dropping the filler customer made earlier to fill missing customer ids
    return customers.sort_values("customer_id", ascending=True).reset_index(drop=True)

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
    weekend_sales = int(df[df["is_weekend"] == True]["total_amount"].sum())
    weekday_sales = int(df[df["is_weekend"] == False]["total_amount"].sum())
    comparison["weekend"]["total_sales"] = weekend_sales
    comparison["weekend"]["percentage"] = round(float(100 * weekend_sales / (weekend_sales + weekday_sales)), 2)
    comparison["weekdays"]["total_sales"] = weekday_sales
    comparison["weekdays"]["percentage"] = round(float(100 * weekday_sales / (weekend_sales + weekday_sales)), 2)

    return comparison

if __name__ == "__main__":
    df = load_data("../data/orders.csv")
    explore_data(df)