-- models/producto.sql
SELECT * FROM {{ source('test', 'product') }}
