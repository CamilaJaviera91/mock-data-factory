# 🏭 Mock Data Factory

- Generate large-scale synthetic datasets using SQL and BigQuery.  

- This project is ideal for testing, prototyping, and demonstrating data pipelines, analytics, and dashboards with realistic but fake data.

---

## 📌 Features

- SQL-based data generation for BigQuery
- Modular models for customers, products, and orders
- Parameterized row volume (e.g. 10K, 1M, etc.)
- DBT-ready structure for scalable development
- Easy integration with data pipeline tools (Airflow, Cloud Composer, etc.)

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

## Using the starter project

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

## 📦 Script: generate_fake_data

- This script generates synthetic data for a PostgreSQL database using the Faker library. It creates and populates three tables: client, product, and orders, useful for testing analytics workflows, dashboards, or data pipelines.

---

### 📋 Features

- Automatically creates required tables (client, product, orders)

- Populates:

    - 200 fake clients

    - 30 pre-defined products across categories

    - 500 randomized orders with realistic dates and values

- Uses Python's psycopg2 and Faker libraries

- Customizable and easy to extend

---

### 🚀 Setup

#### Step 1: Prerequisites

Make sure you have the following installed:

- Python 3.7+

- PostgreSQL (running locally or accessible remotely)

Install dependencies:

```
pip install faker psycopg2
```

#### Step 2: Configure Database Connection

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

---

## Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
