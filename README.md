# 🏭 Mock Data Factory

## 📌 Description

- This repository is a project designed to generate large-scale synthetic datasets using SQL and BigQuery. 

- It's particularly useful for testing, prototyping, and demonstrating data pipelines, analytics, and dashboards with realistic but fake data.

---

## 🔧 Key Features

- **SQL-Based Data Generation:** Utilizes SQL for creating synthetic data tailored for BigQuery environments.

- **Modular Models:** Includes separate models for customers, products, and orders, allowing for flexible data generation.

- **Parameterized Row Volume:** Supports generating datasets with varying sizes (e.g., 10K, 1M rows) to suit different testing needs.

- **DBT-Ready Structure:** Structured to integrate seamlessly with DBT (Data Build Tool) for scalable development.

- **Pipeline Integration:** Designed for easy integration with data pipeline tools like Airflow and Cloud Composer.

---

## 🗂️ Project Structure

```
├── .gitignore
├── logs
│   └── dbt.log
├── mockdata
│   ├── analyses
│   │   └── .gitkeep
│   ├── dbt_project.yml
│   ├── .gitignore
│   ├── macros
│   │   └── .gitkeep
│   ├── models
│   │   ├── client.sql
|   |   ├── orders.sql
|   |   ├── product.sql
│   │   └── schema.yml
│   ├── scripts
│   │   └── generate_fake_data.py
│   ├── README.md
│   ├── seeds
│   │   └── .gitkeep
│   ├── snapshots
│   │   └── .gitkeep
│   └── tests
│       └── .gitkeep
└── README.md
```

---

## 🧪 DBT Integration

Try running the following commands.

- Builds or materializes the tables/views based on your transformations.

```
dbt run
```

- Runs checks on the data to ensure quality and correctness.

```
dbt test
```

---

## 🐍 Python Script: generate_fake_data.py

- Located in the mockdata/scripts/ directory, this Python script uses the Faker library to generate synthetic data for a PostgreSQL database. It creates and populates three tables: client, product, and orders. 

- The script is customizable and can be extended to fit specific testing scenarios.

---

### 🔧 Key Features

- SQL-based data generation tailored for BigQuery.

- Modular models for entities like customers, products, and orders.

- Parameterized row volume, allowing generation of datasets with varying sizes (e.g., 10K, 1M rows).

- DBT-ready structure for scalable development.

- Easy integration with data pipeline tools such as Airflow and Cloud Composer.

---

### 🚀 Setup

#### ⚙️ Step 1: Prerequisites

Make sure you have the following installed:

- Python 3.7+

- PostgreSQL (running locally or accessible remotely)

Install dependencies:

```
pip install faker psycopg2
```

#### 🔗 Step 2: Configure Database Connection

Update the PostgreSQL credentials in the script:

```
conn = psycopg2.connect(
    host="localhost",
    database="db_name",
    user="user_name",
    password="*****"
)
```

- Adjust the values to match your environment.

#### ▶️ Step 3: Run the Script

Once configured, run the script:

```
python generate_fake_data.py
```

You'll see log messages indicating progress:

```
✅ Successfully connected to PostgreSQL.
✅ Tables created or verified.
✅ Inserted 200 clients.
✅ Inserted 30 products.
✅ Inserted 500 orders.
✅ PostgreSQL connection closed. Data generation complete.
```
---

## 🗃️ Table Schemas

```client```

| Column    | Type               |
|-----------|--------------------|
| client_id | SERIAL PRIMARY KEY |
| name      | TEXT               |
| email     | TEXT               |
| address   | TEXT               |
| city      | TEXT               |
| country   | TEXT               |

```product```
| Column      | Type                |
|-------------|---------------------|
| product_id  | SERIAL PRIMARY KEY  |
| name        | TEXT                |
| price       | NUMERIC(10,2)       |
| category    | TEXT                |

```salesman```

| Column      | Type               |
|-------------|--------------------|
| salesman_id | SERIAL PRIMARY KEY |
| name        | TEXT               |
| city        | TEXT               |

```orders```
| Column      | Type                    |
|-------------|-------------------------|
| order_id    | SERIAL PRIMARY KEY      |
| client_id   | INTEGER (FK to client)  |
| product_id  | INTEGER (FK to product) |
| order_date  | DATE                    |
| quantity    | INTEGER                 |
| total       | NUMERIC(10,2)           |

---

## 🛠️ Customization

To generate more or fewer rows, change the arguments in generate_clients(), generate_products(), generate_salesman() or generate_orders(). You can modify the list of product names and categories to suit your business domain.

---

## 📎 Related Projects

I have other related repositories that might be of interest:​

- ```sql-mock-data:``` Earlier version or a related project focusing on SQL-based mock data generation.
    - [repository](https://github.com/CamilaJaviera91/sql-mock-data)

- ```dbt-transformations-sql-mock-data:``` This project contains transformations and documentation for the data model generated in ```sql-mock-data```.​
    - [repository](https://github.com/CamilaJaviera91/dbt-transformations-sql-mock-data)

---

## 💭 Final Thoughts

- The mock-data-factory repository offers a robust framework for generating synthetic datasets, making it a valuable tool for data engineers and analysts working with BigQuery and DBT. Its modular design and integration capabilities make it adaptable to various testing and development scenarios.

- If you need assistance setting up the project or customizing it for your specific use case, feel free to ask!

---

## 📚 Learn More About dbt

- 📖 **Read the [official dbt documentation](https://docs.getdbt.com/docs/introduction)** — A great starting point to understand how dbt works and how to get started.
- 💬 **Visit [Discourse](https://discourse.getdbt.com/)** — Explore frequently asked questions and community discussions.
- 💻 **Join the [dbt Slack community](https://community.getdbt.com/)** — Get live support, ask questions, and connect with other data practitioners.
- 📅 **Browse upcoming [dbt events](https://events.getdbt.com)** — Find webinars, meetups, and conferences near you.
- 📰 **Read the [dbt blog](https://blog.getdbt.com/)** — Stay up to date with product updates, best practices, and community highlights.

---

## 📄 License

This project is released under the MIT License.
