import pandas as pd
#------------------------------importing complete-----------------------------------

class Question:

    sql = {1: 'SELECT product_id, SUM(sales_amt) AS "total_sales_amt" \
               FROM sales \
               GROUP BY product_id \
               LIMIT 5;',
           
           2: 'SELECT sales.*, products.product_name, products.category \
               FROM sales \
               INNER JOIN products \
               ON sales.product_id = products.product_id \
               ORDER BY sales_id \
               LIMIT 5;',
           
           3: 'SELECT customer_id, SUM(sales_amt) AS total_invoice_amount \
               FROM sales \
               GROUP BY customer_id \
               ORDER BY total_invoice_amount DESC \
               LIMIT 5;',
           
           4: 'SELECT monthname(date) AS month, AVG(sales.sales_amt) AS avg_sales_amount \
               FROM sales \
               GROUP BY month;'
          }
    
    def print_answer(self, answer):
        print("---------------------------------")
        
        col_names = answer[0]
        df = pd.DataFrame(answer[1], columns=col_names)
        print(df)