import pandas as pd
import numpy as np



df = pd.read_csv('sales_data.csv')

sales_table = df[['Sales ID', 'Product ID', 'Customer ID', 'Sales', 'Order Date','Order Quantity', 'Region ID']]
products_table = df[['Product ID', 'Product Name', 'Product Category','Sales Representative', 'Unit Price']]
customers_table = df[['Customer ID', 'Customer Name', 'Email ID','Customer Segment', 'Address']]
regions_table = df[['Region', 'Region ID']]

# Saving DataFrames to CSV files
sales_table.to_csv('sales_table.csv', index=False)
products_table.to_csv('products_table.csv', index=False)
customers_table.to_csv('customers_table.csv', index=False)
regions_table.drop_duplicates().to_csv('regions_table.csv', index=False)






#                Level 1: Data Loading and Basic Analysis

# 1. Load the sales dataset (e.g., 'sales.csv') into a Pandas DataFrame.
sales_data = pd.read_csv('sales_table.csv')

# 2. Display the first 5 rows of the dataset.
print("First five rows of data: ")
print(sales_data[0:5])

# 3. Check the shape (number of rows and columns) of the dataset.
shape_of_sales = sales_data.shape
print('rows in dataset:', shape_of_sales[0])
print('colomns in dataset:', shape_of_sales[1])

# 4. Display basic statistics (mean, median, min, max) for the 'Sales' column.
sales_data_mean = sales_data['Sales'].mean()
sales_data_median = sales_data['Sales'].median()
sales_data_min = sales_data['Sales'].min()
sales_data_max = sales_data['Sales'].max()
print('the average in sales: ',sales_data_mean)
print('the median in sales: ',sales_data_median)
print('the min value in sales: ',sales_data_min)
print('the max value in sales: ',sales_data_max)


# 5. Determine the number of unique products sold.
# sales_data_unique = (sales_data['Product ID'].nunique()).value_counts()
sales_data_unique = sales_data['Product ID'].value_counts().reset_index()
print('Unique product sold: ')
print(sales_data_unique)



#                 Level 4: Data Aggregation and Grouping

# 1. Group the sales data by product category and calculate the total sales amount for each
# category

product_data = pd.read_csv('products_table.csv')
sales_product = pd.merge(sales_data, product_data, on='Product ID', how='inner')
category_sales = sales_product.groupby('Product Category')['Sales'].sum()
print('Sales by the product category: ')
print(category_sales)



# 2. Group the sales data by month and year and calculate the average sales amount for each
# month

sales_data['Order Date'] = pd.to_datetime(sales_data['Order Date'])
sales_data['Month'] = sales_data['Order Date'].dt.month
sales_data['Year'] = sales_data['Order Date'].dt.year

avg_sales_m = sales_data.groupby(['Year', 'Month'])['Sales'].mean()
print(avg_sales_m)



# 3. Aggregate the sales data by region and calculate the total sales amount for each region.

sales_by_region = sales_data.groupby('Region ID')
agg_by_region = sales_by_region.agg({'Sales': 'sum'})
print(agg_by_region)



# 4. Group the sales data by customer segment and calculate the average sales amount for each
# segment.

customer_data = pd.read_csv('customers_table.csv')

sales_customer = pd.merge(sales_data, customer_data, on='Customer ID', how='inner')
sales_by_segment = sales_customer.groupby('Customer Segment')['Sales'].mean()
print(sales_by_segment)



# 5. Aggregate the sales data by sales representative and calculate the total sales amount for
# each representative.


sales_by_rep = sales_product.groupby('Sales Representative')
agg_by_rep = sales_by_rep.agg({'Sales': 'sum'})
print(agg_by_rep)



#                       Level 7: Advanced Pandas Queries

# 1. Use Pandas to filter the sales data for a specific time period (e.g., quarter or year).

sales_data['Order Date'] = pd.to_datetime(sales_data['Order Date'])
desired_year = 2012
# sales_data['Month'] = sales_data['Order Date'].dt.month
sales_data['Year'] = sales_data['Order Date'].dt.year
sales_by_dt = sales_data[sales_data['Year'] == desired_year]
print(sales_by_dt)


# 2. Apply boolean indexing to select rows based on multiple conditions.

condition1 = sales_data['Order Quantity'] > 20
condition2 = sales_data['Sales'] > 500 
condition3 = sales_data['Region ID'] == 2
condition4 = sales_data['Customer ID'].str.contains('BH')

# Combine conditions using logical AND (&)
combined_condition = condition1 & condition2 & condition3 & condition4

# Apply boolean indexing
selected_rows = sales_data[combined_condition]

# Display the selected rows
print('these are selected rows')
print(selected_rows)


# 3. Use Pandas groupby and aggregate functions to calculate custom metrics.

# counting the number of unique 'Product ID' values for each 'Customer ID' in sales table.
unique_product = sales_data.groupby('Customer ID')['Product ID'].nunique()
print("Unique products ",unique_product)


#  Calculating the average 'Sales' amount for each 'Customer ID', 
# then find the customer with the maximum average.

avg_sales = sales_data.groupby('Customer ID')['Sales'].mean()
max_sales_by_ID = avg_sales.idxmax()
max_sales_amount = avg_sales.max()

print("max sales by the customer id: ",max_sales_by_ID)
print("max sales avg sales amount: ",max_sales_amount)


# Calculate the cumulative sum of the 'Sales' column to see the total sales amount over time.

total_sales = sales_data['Sales'][0:10].cumsum()
print("Cummulative sum of sales ", total_sales)


# 4. Combine multiple DataFrames using merge or join operations.

# combining all the tables into one and creating a new csv file for it

region_data = pd.read_csv('regions_table.csv')
sales_and_product = pd.merge(sales_data, product_data, on='Product ID', how='outer')
salesP_and_customer = sales_and_product.join(customer_data.set_index('Customer ID'), on='Customer ID', how='left')
salesPC_and_region = salesP_and_customer.join(region_data.set_index('Region ID'), on='Region ID', how='outer')
joined_table = salesPC_and_region
print(salesPC_and_region[0:10:4])

# joined_table.to_csv('Joined_table.csv', index=False)