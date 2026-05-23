#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

## Gives the binary RCA matrix containing countries and the products they export (where RCA = 1 means the country exports the product with a revealed comparative advantage and RCA = 0 means they do not)

## Step 1: Load Trade Data
data = pd.read_excel("")

## Step 2: Calculate total country exports for each country
country_totals = data.groupby('Country')['Export Value'].sum().rename('Country_Total') ## Groups data by country and adds there're exports
data = data.merge(country_totals, on='Country') ## Adds total country exports to existing dataframe

## Step 3: Calculate total world exports per product
product_totals = data.groupby('Product')['Export Value'].sum().rename('Product_Total')
data = data.merge(product_totals, on='Product')

## STEP 4: Calculate Total world exports
world_total = data['Export Value'].sum()


# STEP 5: RCA calculation
# RCA = (Xpc / Xp) / (Xc / Xw)
data['RCA'] = (data['Export Value'] / data['Product_Total']) / (data['Country_Total'] / world_total)

## STEP 6: Represent in matrix form
rca_matrix = pd.pivot_table(data,
                            values='RCA',
                            index='Product',
                            columns='Country',
                            fill_value=0)

binary_matrix = (rca_matrix >= 1).astype(int)


## STEP 7: Save outputs as CSV
# RCA matrix (Product × Country)
binary_matrix.to_excel('')
print("Done")

