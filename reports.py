import pandas as pd

sales = pd.read_csv('data_engineering_data.csv')

sales['ORDER_DATE'] = pd.to_datetime(sales['ORDER_DATE']) - pd.to_timedelta(7, unit='d')

# PREPARE THE DATAFRAMES
sales_average = sales.groupby(['PRODUCT_ID', pd.Grouper(key='ORDER_DATE', freq='W-MON')])['UNITS_ORDERED'].mean().reset_index().sort_values('ORDER_DATE')
sales_total = sales.groupby(['PRODUCT_ID', pd.Grouper(key='ORDER_DATE', freq='W-MON')])['UNITS_ORDERED'].sum().reset_index().sort_values('ORDER_DATE')

# FORMAT AVERAGE DATAFRAME
sales_average = sales_average[['ORDER_DATE', 'PRODUCT_ID', 'UNITS_ORDERED']]
sales_average.columns = ['PERIOD', 'PRODUCT_ID', 'AVG_UNITS_ORDERED']

# FORMAT TOTAL DATAFRAME
sales_total = sales_total[['ORDER_DATE', 'PRODUCT_ID', 'UNITS_ORDERED']]
sales_total.columns = ['PERIOD', 'PRODUCT_ID', 'TOTAL_UNITS_ORDERED']

print('****************************************************************')
print('************** AVERAGE SALES PER PRODUCT PER WEEK **************')
print('****************************************************************')
print(sales_average)
sales_average.to_csv('output_avg.csv')

print('****************************************************************')
print('*************** TOTAL SALES PER PRODUCT PER WEEK ***************')
print('****************************************************************')
print(sales_total)
sales_average.to_csv('output_total.csv')