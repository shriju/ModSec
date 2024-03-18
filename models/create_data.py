import os
import numpy as np
import pandas as pd

from datetime import datetime as dt


files_exist = [os.path.isfile("data/" + file + ".csv")\
                for file in "products, regions, sales, customers".split(", ")]

#===========================================================================================
#
# Making some changes to given .csv files
#   1. In Products table, there are 2 duplicate product_id.
#   2. In Regions table, converting it to key-value format
#      (instead of having as many rows as in Sales table).
#   3. In Customers table, allowing duplicate emails and addresses (family),
#      but no duplicate names
#   4. In Sales table:
#       - dates are made to be ordered, but random. (no regular intervals)
#       - price is made to sync with product_id as foreign key
#   5. Finally, allowing resampling from Products table to have as many sales
#      transactions as we desire. (say 1000)

if np.all(files_exist):
    sales = pd.read_csv("data/sales.csv")
    regions = pd.read_csv("data/regions.csv")
    products = pd.read_csv("data/products.csv")
    customers = pd.read_csv("data/customers.csv")

else:
    sales = pd.read_csv("data/given_sales.csv")
    regions = pd.read_csv("data/given_regions.csv")
    products = pd.read_csv("data/given_products.csv")
    customers = pd.read_csv("data/given_customers.csv")

for file in [sales, products, customers, regions]:
    print()
    print("no. of rows = ",file.shape[0])
    print("column names = ",list(file.columns))
    print("no. of unique entries per column:")
    print(file.nunique())
    print("-------------------------------------")

# Changes to Products info
products.drop_duplicates('product_name', inplace=True)
products.head()

products.nunique()

# Changes to Regions info
regions.drop_duplicates('region_name', inplace=True)
regions

# Changes to Customers info
customers.drop_duplicates('customer_name', inplace=True)
customers.head()

customers.nunique()

# Changes to Sales info
r = 1000

start_date = '1/1/2015'
end_date = '31/12/2020'
all_dates = pd.date_range(start_date, end_date, freq='D')

sales = {"sales_id": np.arange(1,r+1),
        "product_id": np.random.choice(products.product_id, size=r),
        "customer_id": np.random.choice(customers.customer_id, size=r),
        "date": np.sort(np.random.choice(all_dates, size=r)),
        "region_id": np.random.choice(regions.region_id, size=r)
        }

sales = pd.DataFrame(sales)

sales["sales_amt"] = pd.merge_ordered(sales, products, on='product_id').sort_values(by="sales_id").price.values
#===========================================================================================

#===========================================================================================
#
# save to .csv
sales.to_csv("data/sales.csv", index=False)
products.to_csv("data/products.csv", index=False)
regions.to_csv("data/regions.csv", index=False)
customers.to_csv("data/customers.csv", index=False)
#===========================================================================================