# 🏭 Mock Data Factory

Generate large-scale synthetic datasets using SQL and BigQuery.  
<br>
This project is ideal for testing, prototyping, and demonstrating data pipelines, analytics, and dashboards with realistic but fake data.

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
mock-data-factory/
├── dbt_project.yml              ✅ Project configuration
├── README.md                    ✅ Clear project documentation
├── .gitignore               
├── models/
│   └── mock_data/               ✅ Organized model directory
│       ├── customers.sql        ✅ Synthetic data generation logic
│       └── schema.yml           ✅ Model descriptions and tests
├── macros/
│   └── .gitkeep                 ✅ Ready for future reusable macros
```

