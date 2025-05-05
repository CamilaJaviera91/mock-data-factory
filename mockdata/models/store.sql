-- models/store.sql
SELECT * FROM {{ source('test', 'store') }}
