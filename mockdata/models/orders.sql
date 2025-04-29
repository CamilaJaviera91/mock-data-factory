-- models/orden.sql
SELECT * FROM {{ source('test', 'orders') }}
