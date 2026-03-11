import matplotlib.pyplot as plt
import pandas as pd
from .analysis import *

def create_category_bar_chart(category_data, output_path):
    """
    Create a horizontal bar chart of sales by category.
    - Include value labels on bars
    - Use a professional color scheme
    - Save to output_path
    """
    fig, ax = plt.subplots()
    ax.barh(category_data["total_sales"], category_data["category"])
    ax.set_xlabel("Sales")
    ax.set_ylabel("Category")
    ax.set_title("Sales by Category")
    fig.savefig(output_path)
    plt.close(fig)

def create_regional_pie_chart(region_data, output_path):
    """
    Create a pie chart showing sales distribution by region.
    - Include percentages
    - Use distinct colors for each region
    - Save to output_path
    """
    fig, ax = plt.subplots()
    ax.pie(region_data["percentage_of_total"], labels=region_data["region"])
    ax.set_title("Regional Sales Data")
    fig.savefig(output_path)
    plt.close(fig)

def create_sales_trend_line(daily_data, output_path):
    """
    Create a line chart showing daily sales trend.
    - Include moving average (7-day)
    - Mark weekends differently
    - Add proper axis labels and title
    - Save to output_path
    """
    # Make a local copy so we don't mutate the caller's DataFrame
    daily_data = daily_data.copy()

    # Ensure dates are datetime-like for Matplotlib date plotting
    daily_data["date"] = pd.to_datetime(daily_data["date"])

    daily_data["rolling_avg"] = daily_data["total_sales"].rolling(window=7).mean()

    fig, ax = plt.subplots()
    ax.plot(daily_data["date"], daily_data["total_sales"], label="Total Sales")
    ax.plot(daily_data["date"], daily_data["rolling_avg"], label="Rolling Average (7 Days)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales ($)")
    ax.legend()

    # Add weekend shading
    daily_data = daily_data.rename(columns={"date": "order_date"})
    daily_data = add_time_features(daily_data)

    for i, val in enumerate(daily_data["day_of_week"]):
        if i == 0:
            continue
        if val == 6:
            ax.axvspan(daily_data["order_date"][i - 1], daily_data["order_date"][i], color="grey", alpha=0.25)

    fig.savefig(output_path)
    plt.close(fig)
        

def create_dashboard(df, output_dir):
    """
    Create a multi-panel dashboard with 4 subplots:
    1. Sales by category (bar)
    2. Sales by region (pie)
    3. Daily trend (line)
    4. Top 10 products (horizontal bar)
    
    Save as a single figure.
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 5))
    ax = axes.flatten()

    cat_data = sales_by_category(df)
    ax[0].bar(cat_data["category"], cat_data["total_sales"])
    ax[0].set_xlabel("Category")
    ax[0].set_ylabel("Sales")
    ax[0].set_title("Sales by Category")

    reg_data = sales_by_region(df)
    ax[1].pie(reg_data["percentage_of_total"], labels=reg_data["region"])
    ax[1].set_title("Regional Sales Data")

    day_data = daily_sales_trend(df)
    day_data["rolling_avg"] = day_data["total_sales"].rolling(window=7).mean()

    ax[2].plot(day_data["date"], day_data["total_sales"], label="Total Sales")
    ax[2].plot(day_data["date"], day_data["rolling_avg"], label="Rolling Average (7 Days)")
    ax[2].set_xlabel("Date")
    ax[2].set_ylabel("Sales ($)")
    ax[2].legend()

    day_data = day_data.rename(columns={"date": "order_date"})
    day_data = add_time_features(day_data)

    for i, val in enumerate(day_data["day_of_week"]):
        if i == 0:
            continue
        if val == 6:
            ax[2].axvspan(day_data["order_date"][i - 1], day_data["order_date"][i], color="grey", alpha=0.25)

    prod_data = top_products(df)
    ax[3].barh(prod_data["total_sales"], prod_data["product_name"])
    ax[3].set_xlabel("Sales ($)")
    ax[3].set_ylabel("Product")
    ax[3].set_title("Top 10 Products")

    fig.savefig(output_dir)
    plt.close(fig)


if __name__ == "__main__":
    df = load_data("../data/orders.csv")
    create_category_bar_chart(sales_by_category(df), '../output/category_chart.png')
    create_regional_pie_chart(sales_by_region(df), '../output/regional_chart.png')
    create_sales_trend_line(daily_sales_trend(df), '../output/sales_tre d_chart.png')
    create_dashboard(df, '../output/dashboard.png')