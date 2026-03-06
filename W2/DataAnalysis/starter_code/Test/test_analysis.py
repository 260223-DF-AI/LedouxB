import pytest
import pandas as pd
from starter_code.utils.analysis import *

@pytest.fixture
def sample_data():
    """Create sample data for testing."""
    return pd.DataFrame({
        'order_id': [1, 2, 3],
        'customer_id': ['C001', 'C002', 'C001'],
        'order_date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-02']),
        'product_name': ['Widget', 'Gadget', 'Widget'],
        'category': ['Electronics', 'Electronics', 'Electronics'],
        'quantity': [2, 1, 3],
        'unit_price': [10.00, 25.00, 10.00],
        'region': ['North', 'South', 'North']
    })

def test_clean_data_removes_duplicates(sample_data):
    """Test that clean_data removes duplicate rows."""
    # Arrange
    df: pd.DataFrame = sample_data
    df.loc[len(df)] = df.iloc[1]
    expected = False # expect any duplicates to return false
    
    # Act
    df = clean_data(df)
    actual = df.duplicated().any()

    # Assert
    assert actual == expected

def test_sales_by_category_calculation(sample_data):
    """Test that category totals are calculated correctly."""
    # Arrange
    expected = pd.DataFrame({
        "category": ["Electronics"],
        "total_sales": 75.00,
        "order_count": 6,
        "avg_order_value": 75/6
    })

    # Act
    clean_df = clean_data(sample_data)
    actual = sales_by_category(clean_df)

    # Assert
    assert actual.equals(expected)

def test_top_products_returns_correct_count(sample_data):
    """Test that top_products returns requested number of items."""
    # Arrange
    expected = pd.DataFrame({
        "product_name": ["widget"],
        "category": ["Electronics"],
        "total_sales": [50.00],
        "units_sold": [5]
    })

    # Act
    clean_df = clean_data(sample_data)
    actual = top_products(clean_df, 1)

    print(expected)
    print(actual)

    # Assert
    assert actual.equals(expected)

# TODO: Add at least 5 more tests

def test_sales_by_region_calculation(sample_data):
    """Test that region totals are calculated correctly."""
    # Arrange
    expected = pd.DataFrame({
        "region": ["North", "South"],
        "total_sales": [50.00, 25.00],
        "percentage_of_total": [round(100 * 50/75, 2), round(100 * 25/75, 2)]
    })

    # Act
    clean_df = clean_data(sample_data)
    actual = sales_by_region(clean_df)

    # Assert
    assert actual.equals(expected)

def test_daily_sales_trend(sample_data):
    """Test that daily sales totals are calculated correctly."""
    # Arrange
    expected = pd.DataFrame({
        "date": pd.to_datetime(['2024-01-01', '2024-01-02']),
        "total_sales": [20.0, 55.0],
        "order_count": [2, 4]
    })
    
    # Act
    clean_df = clean_data(sample_data)
    actual = daily_sales_trend(clean_df)

    print(expected)
    print(actual)

    # Assert
    assert actual.equals(expected)

def test_customer_analysis(sample_data):
    """Test that customer totals and trends are calculated correctly"""
    # Arrange
    expected = pd.DataFrame({
        "customer_id": ["C001", "C002"],
        "total_spent": [50.0, 25.0],
        "order_count": [5, 1],
        "avg_order_value": [10.0, 25.0],
        "favorite_category": ["Electronics", "Electronics"]
    })

    # Act
    clean_df = clean_data(sample_data)
    actual = customer_analysis(clean_df)

    # Assert
    assert actual.equals(expected)

def test_weekend_vs_weekday_calculation(sample_data):
    """Test that weekend and weekday calculations are calculated correctly"""
    # Arrange
    expected = {
        "weekend": {
            "total_sales": 0.0,
            "percentage": 0.0
        },
        "weekdays": {
            "total_sales": 75.0,
            "percentage": 100.0
        }
    }

    # Act
    clean_df = clean_data(sample_data)
    df = add_time_features(clean_df)
    actual = weekend_vs_weekday(df)

    # Assert
    assert actual == expected