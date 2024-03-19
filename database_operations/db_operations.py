import logger as log
from models.model import frames
from validator import Validate

import pandas as pd
#------------------------------importing complete-----------------------------------

class DatabaseOperations:
    
    acceptable_reg = 0
    acceptable_prd = 0
    acceptable_cust = 0
    acceptable_sls = 0

    #creates database initially
    def db_create(self, conn, cursor):
        try:
            cursor.execute("DROP DATABASE IF EXISTS sales_outlook")
            cursor.execute("CREATE DATABASE sales_outlook")
        
        except Exception as e:
            print(str(e))
            log.make_entry("{}: {}".format(type(e).__name__, str(e)))
        
        else:
            print("Database created. \n")
            log.make_entry("Database created")
    
    
    #populates the database from .csv files
    def db_populate(self, conn, cursor):
        try:
            vld = Validate()
            
            #-----------
            #-----------Region table
            df = frames[0]
            cursor.execute("CREATE TABLE regions (region_id TINYINT NOT NULL, region_name VARCHAR(40) NOT NULL, PRIMARY KEY(region_id) );")
            SQL = "INSERT INTO regions (region_id, region_name) VALUES (%s, %s)"
            
            for i in df.index:
                row = (int(df.region_id[i]), df.region_name[i])
                if vld.valid_all("regions", row):
                    self.acceptable_reg += 1
                cursor.execute(SQL, row)
                log.make_entry("Table Regions entry: {}".format(row))
            conn.commit()
            print("Regions table populated. \n")
            log.make_entry(f"No. of acceptable rows in Regions = {self.acceptable_reg}/{df.shape[0]}")

            #-----------
            #-----------Products table
            df = frames[1]
            cursor.execute("CREATE TABLE products (product_id SMALLINT NOT NULL,\
                                                   product_name VARCHAR(40) NOT NULL,\
                                                   category VARCHAR(40) NOT NULL,\
                                                   price SMALLINT NOT NULL,\
                                                   PRIMARY KEY(product_id) );")
            SQL = "INSERT INTO products (product_id, product_name, category, price) VALUES (%s, %s, %s, %s)"
            for i in df.index:
                row = (int(df.product_id[i]), df.product_name[i], df.category[i], int(df.price[i]))
                if vld.valid_all("products", row):
                    self.acceptable_prd += 1
                cursor.execute(SQL, row)
                log.make_entry("Table Products entry: {}".format(row))
            conn.commit()
            print("Products table populated. \n")
            log.make_entry(f"No. of acceptable rows in Products = {self.acceptable_prd}/{df.shape[0]}")

            #-----------
            #-----------Customers table
            df = frames[2]
            cursor.execute("CREATE TABLE customers (customer_id SMALLINT NOT NULL,\
                                                   customer_name VARCHAR(40) NOT NULL,\
                                                   email VARCHAR(40) NOT NULL,\
                                                   address VARCHAR(200),\
                                                   PRIMARY KEY(customer_id)\
                            );")
            SQL = "INSERT INTO customers (customer_id, customer_name, email, address) VALUES (%s, %s, %s, %s)"
            for i in df.index:
                row = (int(df.customer_id[i]), df.customer_name[i], df.email[i], df.address[i])
                if vld.valid_all("customers", row):
                    self.acceptable_cust += 1
                cursor.execute(SQL, row)
                log.make_entry("Table Customers entry: {}".format(row))
            conn.commit()
            print("Customers table populated. \n")
            log.make_entry(f'No. of acceptable rows in Customers = {self.acceptable_cust}/{df.shape[0]}')
            
            #-----------
            #-----------Sales table
            df = frames[3]
            df.date = pd.to_datetime(df.date)
            cursor.execute("CREATE TABLE sales (sales_id INT NOT NULL,\
                                                product_id SMALLINT NOT NULL,\
                                                customer_id SMALLINT NOT NULL,\
                                                date DATE,\
                                                region_id TINYINT NOT NULL,\
                                                sales_amt INT NOT NULL,\
                                                PRIMARY KEY(sales_id),\
                                                CONSTRAINT FK_Product_Sale FOREIGN KEY (product_id) REFERENCES products(product_id),\
                                                CONSTRAINT FK_Customer_Sale FOREIGN KEY (customer_id) REFERENCES customers(customer_id),\
                                                CONSTRAINT FK_Region_Sale FOREIGN KEY (region_id) REFERENCES regions(region_id)\
                            );")
            SQL = "INSERT INTO sales (sales_id, product_id, customer_id, date, region_id, sales_amt) VALUES (%s, %s, %s, %s, %s, %s)"
            for i in df.index:
                row = (int(df.sales_id[i]), int(df.product_id[i]), int(df.customer_id[i]), df.date[i], int(df.region_id[i]), int(df.sales_amt[i]))
                if vld.valid_all("sales", row):
                    self.acceptable_sls += 1
                cursor.execute(SQL, row)
            conn.commit()
            print("Sales table populated. \n")
            log.make_entry(f"No. of acceptable rows in Sales = {self.acceptable_sls}/{df.shape[0]}")

        except Exception as e:
            print(str(e))
            log.make_entry("ERROR: {}: {}".format(type(e).__name__, str(e)))