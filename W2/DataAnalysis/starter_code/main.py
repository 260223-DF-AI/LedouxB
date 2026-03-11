from utils import *

def main():
    # Load Data
    # Clean/Transform Data
    df = load_data("./data/orders.csv")

    # Analyze
    category_data = sales_by_category(df)
    region_data = sales_by_region(df)
    daily_data = daily_sales_trend(df)

    # Generate Visuals
    create_category_bar_chart(category_data, './output/category_chart.png')
    create_regional_pie_chart(region_data, './output/regional_chart.png')
    create_sales_trend_line(daily_data, './output/sales_trend_chart.png')
    create_dashboard(df, './output/dashboard.png')

    # Print Summary
    explore_data(df)

if __name__ == "__main__":
    main()