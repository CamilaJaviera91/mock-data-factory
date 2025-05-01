from faker import Faker
import psycopg2
import random

# Configure PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",     # Change this if your DB is on another host
    database="postgres",  # Change to your actual database name
    user="admin",         # Your PostgreSQL username
    password="admin123"   # Your PostgreSQL password
)
cur = conn.cursor()

fake = Faker()

# Create tables if they don't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS client (
    client_id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    address TEXT,
    city TEXT,
    country TEXT
);

CREATE TABLE IF NOT EXISTS product (
    product_id SERIAL PRIMARY KEY,
    name TEXT,
    price NUMERIC(10,2),
    category TEXT
);

CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES client(client_id),
    product_id INTEGER REFERENCES product(product_id),
    order_date DATE,
    quantity INTEGER,
    total NUMERIC(10,2)
);
""")
conn.commit()

# Generate clients
def generate_clients(n=100):
    for _ in range(n):
        cur.execute("""
            INSERT INTO client (name, email, address, city, country)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            fake.name(),
            fake.email(),
            fake.street_address(),
            fake.city(),
            fake.country()
        ))
    conn.commit()

# Updated generate_products function with fixed product names
def generate_products():
    product_names = [
        # Electronics
        "Smartwatch Z3", "UltraSound Speaker", "Quantum Laptop Pro", "Solar Power Bank", "VR Vision Headset",
        # Home
        "Bamboo Cutting Board", "EcoSmart Kettle", "Smart Air Purifier", "Velvet Throw Blanket", "LED Mood Lamp",
        # Sports
        "Carbon Fiber Tennis Racket", "ProFit Yoga Mat", "TrailMax Running Shoes", "SpeedX Bicycle Helmet", "UltraGrip Soccer Ball",
        # Fashion
        "UrbanWear Denim Jacket", "Classic Leather Boots", "Elegant Silk Scarf", "StreetFit Hoodie", "Gold Hoop Earrings",
        # Books
        "The Edge of Tomorrow", "Mastering Data Science", "A Brief History of AI", "The Art of Minimalism", "Cooking for Coders"
    ]

    categories = {
        "Smartwatch Z3": "Electronics", "UltraSound Speaker": "Electronics", "Quantum Laptop Pro": "Electronics",
        "Solar Power Bank": "Electronics", "VR Vision Headset": "Electronics",

        "Bamboo Cutting Board": "Home", "EcoSmart Kettle": "Home", "Smart Air Purifier": "Home",
        "Velvet Throw Blanket": "Home", "LED Mood Lamp": "Home",

        "Carbon Fiber Tennis Racket": "Sports", "ProFit Yoga Mat": "Sports", "TrailMax Running Shoes": "Sports",
        "SpeedX Bicycle Helmet": "Sports", "UltraGrip Soccer Ball": "Sports",

        "UrbanWear Denim Jacket": "Fashion", "Classic Leather Boots": "Fashion", "Elegant Silk Scarf": "Fashion",
        "StreetFit Hoodie": "Fashion", "Gold Hoop Earrings": "Fashion",

        "The Edge of Tomorrow": "Books", "Mastering Data Science": "Books", "A Brief History of AI": "Books",
        "The Art of Minimalism": "Books", "Cooking for Coders": "Books"
    }

    for name in product_names:
        price = round(random.uniform(10.0, 1000.0), 2)
        category = categories[name]
        cur.execute("""
            INSERT INTO product (name, price, category)
            VALUES (%s, %s, %s)
        """, (name, price, category))

    conn.commit()

# Generate orders
def generate_orders(n=200):
    for _ in range(n):
        client_id = random.randint(1, 100)
        product_id = random.randint(1, 50)
        quantity = random.randint(1, 5)
        unit_price = round(random.uniform(10.0, 1000.0), 2)
        total = round(quantity * unit_price, 2)
        cur.execute("""
            INSERT INTO orders (client_id, product_id, order_date, quantity, total)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            client_id,
            product_id,
            fake.date_this_decade(),
            quantity,
            total
        ))
    conn.commit()

# Run generation functions
generate_clients()
generate_products()
generate_orders()

# Close connection
cur.close()
conn.close()