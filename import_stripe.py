import csv
import stripe

stripe.api_key = "pk_live_51Itf0iBfPYcjROShoTxAJMuKSiALPmBi1MgtLxub6UkXZ2Sos884Sy6E0R221dIQyT5ZFDi5ywz4kIKMxmIdag2c00GmcepI6B"

# Define a function to create a product and price
def create_product_and_price(name, description, default_price_data, unit_label):
    # Create product
    product = stripe.Product.create(
        name=name,
        description=description,
    )

    # Create price for the product with default_price_data
    price = stripe.Price.create(
        product=product.id,
        unit_amount=int(float(default_price_data) * 100),  # Stripe uses cents
        currency="usd",  # Replace with the appropriate currency code
        recurring= "Never",  # Adjust as needed
        unit_label=unit_label,
    )

    return product, price

# Read CSV and create products/prices
with open('products.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['Name']
        description = row['Description']
        default_price_data = row['Default Price Data']
        unit_label = row['Unit Label']

        product, price = create_product_and_price(name, description, default_price_data, unit_label)

        print(f"Created product: {product.id} and price: {price.id}")
