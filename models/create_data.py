import os
import numpy as np
import pandas as pd

from datetime import datetime as dt
#------------------------------importing complete-----------------------------------

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
        #   5. Finally, perform sampling-with-replacement from Products table to have as many sales
        #      transactions as we desire. (say 1000)
#===========================================================================================

class Create:
    def create(self):
        files_path = [("data/cleaned_data/" + file_name + ".csv") for file_name in "regions, products, customers, sales".split(", ")]

        files_exist = [os.path.isfile(file_path) for file_path in files_path]

        if np.all(files_exist):
            regions, products, customers, sales = [pd.read_csv(file_path) for file_path in files_path]
            
        else:
            files_path = [("data/given_data/given_" + file_name + ".csv") for file_name in "regions, products, customers, sales".split(", ")]
            regions, products, customers, sales = [pd.read_csv(file_path) for file_path in files_path]

            for file in [regions, products, customers, sales]:
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
            
            # save to .csv
            regions.to_csv("data/cleaned_data/regions.csv", index=False)
            products.to_csv("data/cleaned_data/products.csv", index=False)
            customers.to_csv("data/cleaned_data/customers.csv", index=False)
            sales.to_csv("data/cleaned_data/sales.csv", index=False)
            #===========================================================================================