#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Visualization 1: Data Table
st.write("Visualization 1: Data Table")
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40]
})
st.write(data)


# In[5]:


# Visualization 2: Bar Chart
st.write("Visualization 2: Bar Chart")
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [10, 20, 15, 30]
})
fig, ax = plt.subplots()
ax.bar(data['Category'], data['Value'])
st.pyplot(fig)


# In[ ]:




