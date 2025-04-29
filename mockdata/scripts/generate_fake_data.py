from faker import Faker
import psycopg2
import random

# Configure PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",     # Change this if your DB is on another host
    database="postgres",  # Change to your actual database name
    user="postgres",      # Your PostgreSQL username
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

# Generate products
def generate_products(n=50):
    categories = ['Electronics', 'Home', 'Sports', 'Fashion', 'Books']
    for _ in range(n):
        cur.execute("""
            INSERT INTO product (name, price, category)
            VALUES (%s, %s, %s)
        """, (
            fake.word().capitalize(),
            round(random.uniform(10.0, 1000.0), 2),
            random.choice(categories)
        ))
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