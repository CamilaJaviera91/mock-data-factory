{{ config(
    materialized='table',
    description='Sales summary by store and year, based on orders data.'
) }}

with resume as (
    select 
        o.order_date as date,
        concat(s.city, '-', s.store_id) as store,
        p.name,
        p.category,
        p.price,
        o.quantity,
        (p.price * o.quantity) as total,
        sm.name as salesman,
        c.name as client
    from {{ source('test', 'orders') }} o
    join {{ source('test', 'store') }} s on o.store_id = s.store_id
    join {{ source('test', 'product') }} p on o.product_id = p.product_id
    join {{ source('test', 'salesman') }} sm on o.salesman_id = sm.salesman_id
    join {{ source('test', 'client') }} c on o.client_id = c.client_id
)

select 
    extract(year from date(date)) as year,
    store,
    sum(total) as total
from resume
group by year, store
order by year, total asc