import csv
import random
from datetime import datetime, timedelta

def generate_sample_data():
    """Generate 50 rows of customer order data with intentional quality issues."""
    
    orders = []
    base_date = datetime(2024, 1, 1)
    
    # Generate 50 rows
    for i in range(50):
        order_id = f"ORD{1000 + i}"
        customer_name = f"Customer {i}" if i not in [5, 15, 25] else None  # 3 nulls
        email = f"customer{i}@example.com"
        order_date = (base_date + timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d")
        amount = round(random.uniform(10, 500), 2)
        status = random.choice(["pending", "completed", "cancelled"])
        
        orders.append({
            "order_id": order_id,
            "customer_name": customer_name,
            "email": email,
            "order_date": order_date,
            "amount": amount,
            "status": status
        })
    
    # Add duplicate order_ids (rows 30 and 40)
    orders[40]["order_id"] = orders[30]["order_id"]
    
    # Add negative amounts (rows 10, 20)
    orders[10]["amount"] = -50.00
    orders[20]["amount"] = -75.50
    
    # Add invalid email (row 35)
    orders[35]["email"] = "invalidemail.com"
    
    # Add future date (row 45)
    future_date = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
    orders[45]["order_date"] = future_date
    
    # Add invalid status (row 48)
    orders[48]["status"] = "shipped"
    
    # Write to CSV
    with open("./functions/sample_data.csv", "w", newline="") as csvfile:
        fieldnames = ["order_id", "customer_name", "email", "order_date", "amount", "status"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(orders)
    
    print("CSV file 'sample_data.csv' generated with 50 rows of sample data.")

if __name__ == "__main__":
    generate_sample_data()