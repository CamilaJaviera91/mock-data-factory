-- models/cliente.sql
SELECT * FROM {{ source('test', 'client') }}
