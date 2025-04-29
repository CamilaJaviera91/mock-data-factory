-- models/orden.sql
SELECT * FROM {{ source('public', 'orders') }}
