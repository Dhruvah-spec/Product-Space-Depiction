#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

## Uses the binary RCA matrix to give the matrix containing product proximities

# -----------------------------
# File paths
# -----------------------------
input_file = ""
output_file = ""

# -----------------------------
# Read binary RCA matrix
# Products as rows, Countries as columns
# -----------------------------
M = pd.read_excel(
    input_file,
    index_col=0,
    dtype="int8"
)

# -----------------------------
# Ensure product codes are strings and 4 digits
# -----------------------------
M.index = (
    M.index.astype(str)
           .str.strip()
           .str.zfill(4)   # 👈 ensures exactly 4 digits
)

# -----------------------------
# Convert to NumPy for speed
# -----------------------------
M_np = M.values

# Number of countries exporting each product
product_ubiquity = M_np.sum(axis=1)

# Co-export matrix: products × products
co_export = M_np @ M_np.T

# -----------------------------
# Compute proximity matrix
# -----------------------------
num_products = M_np.shape[0]
proximity = np.zeros((num_products, num_products), dtype=float)

for i in range(num_products):
    for j in range(num_products):
        if product_ubiquity[i] > 0 and product_ubiquity[j] > 0:
            proximity[i, j] = min(
                co_export[i, j] / product_ubiquity[i],
                co_export[i, j] / product_ubiquity[j]
            )

# -----------------------------
# Convert to DataFrame
# -----------------------------
proximity_df = pd.DataFrame(
    proximity,
    index=M.index,
    columns=M.index
)

# -----------------------------
# Save to Excel
# -----------------------------
proximity_df.to_excel(output_file)

print(f"Product proximity matrix saved as: {output_file}")

