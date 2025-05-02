from faker import Faker
import psycopg2
import random
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_SCHEMA = os.getenv("DB_SCHEMA")

# Configure PostgreSQL connection
try:
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cur = conn.cursor()
    print("✅ Successfully connected to PostgreSQL.")
except Exception as e:
    print("❌ Failed to connect to PostgreSQL:", e)
    exit()

fake = Faker()

cur.execute(f"SET search_path TO {DB_SCHEMA};")

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
print("✅ Tables created or verified.")

# Generate clients
def generate_clients(n=200):
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
    print(f"✅ Inserted {n} clients.")

# Generate products
def generate_products():
    product_names = [
        # Electronics
        "Smartwatch Z3", "UltraSound Speaker", "Quantum Laptop Pro", "Solar Power Bank", "VR Vision Headset",
        "Noise-Canceling Earbuds",
        # Home
        "Bamboo Cutting Board", "EcoSmart Kettle", "Smart Air Purifier", "Velvet Throw Blanket", "LED Mood Lamp",
        "Organic Cotton Towels",
        # Sports
        "Carbon Fiber Tennis Racket", "ProFit Yoga Mat", "TrailMax Running Shoes", "SpeedX Bicycle Helmet", "UltraGrip Soccer Ball",
        "Adjustable Dumbbell Set",
        # Fashion
        "UrbanWear Denim Jacket", "Classic Leather Boots", "Elegant Silk Scarf", "StreetFit Hoodie", "Gold Hoop Earrings",
        "Minimalist Wristwatch",
        # Books
        "The Edge of Tomorrow", "Mastering Data Science", "A Brief History of AI", "The Art of Minimalism", "Cooking for Coders",
        "Design Patterns Explained"
    ]

    categories = {
        # Electronics
        "Smartwatch Z3": "Electronics", "UltraSound Speaker": "Electronics", "Quantum Laptop Pro": "Electronics",
        "Solar Power Bank": "Electronics", "VR Vision Headset": "Electronics", "Noise-Canceling Earbuds": "Electronics",
        # Home
        "Bamboo Cutting Board": "Home", "EcoSmart Kettle": "Home", "Smart Air Purifier": "Home",
        "Velvet Throw Blanket": "Home", "LED Mood Lamp": "Home", "Organic Cotton Towels": "Home",
        # Sports
        "Carbon Fiber Tennis Racket": "Sports", "ProFit Yoga Mat": "Sports", "TrailMax Running Shoes": "Sports",
        "SpeedX Bicycle Helmet": "Sports", "UltraGrip Soccer Ball": "Sports", "Adjustable Dumbbell Set": "Sports",
        # Fashion
        "UrbanWear Denim Jacket": "Fashion", "Classic Leather Boots": "Fashion", "Elegant Silk Scarf": "Fashion",
        "StreetFit Hoodie": "Fashion", "Gold Hoop Earrings": "Fashion", "Minimalist Wristwatch": "Fashion",
        # Books
        "The Edge of Tomorrow": "Books", "Mastering Data Science": "Books", "A Brief History of AI": "Books",
        "The Art of Minimalism": "Books", "Cooking for Coders": "Books", "Design Patterns Explained": "Books"
    }

    for name in product_names:
        price = round(random.uniform(10.0, 1000.0), 2)
        category = categories[name]
        cur.execute("""
            INSERT INTO product (name, price, category)
            VALUES (%s, %s, %s)
        """, (name, price, category))

    conn.commit()    
    print(f"✅ Inserted {len(product_names)} products.")

# Generate orders
def generate_orders(n=500):
    for _ in range(n):
        client_id = random.randint(1, 200)
        product_id = random.randint(1, 30)  # Use the correct range based on actual inserted products
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
    print(f"✅ Inserted {n} orders.")

# Run generation functions
generate_clients()
generate_products()
generate_orders()

# Close connection
cur.close()
conn.close()
print("✅ PostgreSQL connection closed. Data generation complete.")