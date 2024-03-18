import pandas as pd

class Question:

    sql = {1: 'select product_id, sum(sales_amt) as "total_sales_amt" \
                from sales \
                group by product_id \
                limit 5;',
           
           2: 'select sales.*, products.product_name, products.category \
                from sales \
                inner join products \
                on sales.product_id = products.product_id \
                order by sales_id \
                limit 5;',
           
           3: 'select customer_id, sum(sales_amt) as total_invoice_amount \
                from sales \
                group by customer_id \
                order by total_invoice_amount desc \
                limit 5;',
           
           4: 'select monthname(date) as month, avg(sales.sales_amt) as avg_sales_amount \
                from sales \
                group by month;'
        }

    def __init__(self):
        pass
    
    def print_answer(self, answer):
        print("---------------------------------")
        col_names = answer[0]
        df = pd.DataFrame(answer[1], columns=col_names)
        print(df)