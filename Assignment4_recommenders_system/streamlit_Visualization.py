#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import streamlit as st 

# EDA Pkgs
import pandas as pd 

# Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns 

df = pd.read_csv('newrating.csv')
test = pd.read_csv('t.csv')
predictions = pd.read_csv('pred.csv')
five_rating_prod = pd.read_csv('5ratingprod.csv')
purchase = pd.read_csv('purchase.csv')


prod = purchase.groupby("Products").rating.mean().sort_values(ascending = False)
st.success("Top Products by Average Rating")          
prod.head(5).plot.bar(rot=0)\
.set(title="Top Products by average rating",
xlabel="Product", ylabel="AVG Rating")
st.pyplot()


prod = purchase.groupby("Products").rating.count().sort_values(ascending = False)
st.success("Most bought Products")          
prod.head(5).plot.bar(rot=0)\
.set(xlabel="Product", ylabel="number of times bought")
st.pyplot()


# Pie Chart
#st.checkbox("Pie Plot")
all_columns_names = df.columns.tolist()
#st.button("Generate Pie Plot")
st.success("Pie Plot for Ratings")
st.write(df.iloc[:,2].value_counts().plot.pie(autopct="%1.1f%%"))
st.pyplot()

rating = st.multiselect("Enter rating", df['rating'].unique())
#st.write("Your input rating", rating)
selected_rating_data = df[(df['rating'].isin(rating))]
rating_data_is_check = st.checkbox("Display the data of selected ratng")
if rating_data_is_check:
    st.write(selected_rating_data)


st.warning("Comparison between test and recommended data")
test_plot = test.groupby("Products").rating.mean().sort_values(ascending = False)
st.success("Top Products by Average Rating in test Data")          
test_plot.head(5).plot.bar(rot=0)\
.set(title="Top Products by average rating",
xlabel="Product", ylabel="AVG Rating")
st.pyplot()


predictions_plot = predictions.groupby("Products").prediction.mean().sort_values(ascending = False)
st.success("Top Products by Average Rating in recommended Data")          
predictions_plot.head(5).plot.bar(rot=0)\
.set(title="Top Products by average rating",
xlabel="Product", ylabel="AVG Rating")
st.pyplot()









