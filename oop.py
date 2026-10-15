#s25b38/044
#lisa kushaba
stock = {
    "W001": ("Rolex Submariner", 1500),
    "W002": ("Casio G-Shock", 120),
    "S001": ("Nike Air Max", 90),
    "S002": ("Adidas Yeezy", 200),
    "S003": ("Rolex Submariner", 1500),
}

# Unpack
name, price = stock["S002"]
print(f"{name} costs ${price}")
#TypeError because tuples are immutable and do not support item assignment.

#question 2
daily_orders = ["W001", "S001", "W001", "S002", "S001", "S001", "W002"]
unique_ordered = set(daily_orders)
print(f"Unique products ordered: {unique_ordered}")
unordered = set(stock.keys()) - set(daily_orders)
print(f"Products not ordered: {unordered}")

#question 3
# i) Add new entry to 'stock'
stock["S004"] = ("Puma RS", 110)
order_count = {}
for product_id in daily_orders:
    order_count[product_id] = order_count.get(product_id, 0) + 1

print(f"Order counts: {order_count}")
# iii) Calculate total sales for the day
total_sales = sum(
    count * stock[product_id][1] for product_id, count in order_count.items()
)
print(f"Total sales: ${total_sales}")