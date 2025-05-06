from faker import Faker
import psycopg2
import random
from dotenv import load_dotenv
import os
from psycopg2.extras import execute_batch

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

fake = Faker('es_CL')

cur.execute(f"SET search_path TO {DB_SCHEMA};")

# Create tables if they don't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS client (
    client_id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    address TEXT,
    city TEXT
);
            
CREATE TABLE IF NOT EXISTS store (
    store_id SERIAL PRIMARY KEY,
    name TEXT,
    city TEXT
);

CREATE TABLE IF NOT EXISTS product (
    product_id SERIAL PRIMARY KEY,
    name TEXT,
    price NUMERIC(10,2),
    category TEXT
);
            
CREATE TABLE IF NOT EXISTS salesman (
    salesman_id SERIAL PRIMARY KEY,
    name TEXT,
    city TEXT
);

CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES client(client_id),
    product_id INTEGER REFERENCES product(product_id),
    salesman_id INTEGER REFERENCES salesman(salesman_id),
    store_id INTEGER REFERENCES store(store_id),
    order_date DATE,
    quantity INTEGER
);
""")
conn.commit()
print("✅ Tables created or verified.")

# Generate clients
def generate_clients(n=1000):

    city_maule = ["Talca", "Curicó", "Linares", "Molina", "San Javier", "Cauquenes", 
                  "Chanco", "Colbún", "Rauco", "Villa Alegre", "Longaví", "Constitución", 
                  "Pencahue", "Sagrada Familia", "Hualañé", "Teno", "Licantén", 
                  "Empedrado", "Pelarco", "San Clemente"]

    data = []
    for _ in range(n):
        full_name = fake.name()
        first_name, last_name = full_name.split(" ")[0], full_name.split(" ")[-1]
        email = f"{first_name.lower()}.{last_name.lower()}@stores.com"
        address = fake.street_address()
        city = random.choice(city_maule)
        data.append((full_name, email, address, city))

    execute_batch(cur, """
        INSERT INTO client (name, email, address, city)
        VALUES (%s, %s, %s, %s)
    """, data)
    conn.commit()
    print(f"✅ Inserted {n} clients.")


    # Generate clients
def generate_store(n=10):
    city_maule = ["Talca", "Curicó", "Linares", "Molina", "Cauquenes", 
                  "Villa Alegre", "Constitución", "Teno", "Longaví", "San Clemente"]
    
    if n > len(city_maule):
        print("❌ Not enough unique cities to generate the requested number of stores.")
        return
    
    # Select unique cities for each store
    selected_cities = random.sample(city_maule, n)
    data = [(fake.company(), city) for city in selected_cities]
    
    execute_batch(cur, """
        INSERT INTO store (name, city)
        VALUES (%s, %s)
    """, data)
    conn.commit()
    print(f"✅ Inserted {n} stores.")



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

# Generate salesman
def generate_salesman(n=50):
    data = [(fake.name(), fake.city()) for _ in range(n)]
    execute_batch(cur, """
    INSERT INTO salesman (name, city)
    VALUES (%s, %s)""", data)

    conn.commit()
    print(f"✅ Inserted {n} salesman.")

# Generate orders
def generate_orders(n=50000):
    data = []
    for _ in range(n):
        client_id = random.randint(1, 200)
        product_id = random.randint(1, 30)  # Use the correct range based on actual inserted products
        salesman_id = random.randint(1, 50)
        store_id = random.randint(1, 10)
        quantity = random.randint(1, 5)
        order_date = fake.date_this_decade()  # Generate a random date within this decade
        data.append((client_id, product_id, salesman_id, store_id, order_date, quantity))

    # Insert multiple rows at once for better performance
    execute_batch(cur, """
        INSERT INTO orders (client_id, product_id, salesman_id, store_id, order_date, quantity)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, data)
    
    conn.commit()
    print(f"✅ Inserted {n} orders.")

# Run generation functions
generate_clients()
generate_store()
generate_products()
generate_salesman()
generate_orders()

# Close connection
cur.close()
conn.close()
print("✅ PostgreSQL connection closed. Data generation complete.")