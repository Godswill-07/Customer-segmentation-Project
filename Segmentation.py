import streamlit as st
import pandas as pd
import numpy as np
import joblib


scaler = joblib.load('scaler_v172.pkl')
kmeans = joblib.load('kmeans_v172.pkl')

st.title('Customer Segmentation App')
st.write('Enter customer details to predict the segment')

age = st.number_input('Age', min_value=18, max_value=100,value=35 )
income = st.number_input('Income', min_value=0, max_value=200000,value=50000 )
total_spending = st.number_input('Total Spending (sum of purchases)', min_value=0, max_value=5000,value=1000 )
num_web_purchases = st.number_input('Number of Web Purchases', min_value=0, max_value=100,value=10)
num_store_purchases = st.number_input('Number of Store Purhases', min_value=0, max_value=100,value=10 )
num_web_visits = st.number_input('Number of Website Visits per month', min_value=0, max_value=50,value=30)
recency = st.number_input('Recency (Day since last purchase)', min_value=0, max_value=365,value=30)


input_data = pd.DataFrame ({
    'Age' : [age],
    'Income' : [income],
    'Total_Spending': [total_spending],
    'NumWebPurchases' : [num_web_purchases],
    'NumStorePurchases' : [num_store_purchases],
    'NumWebVisitsMonth' : [num_web_visits],
    'Recency' : [recency]
})

input_scaled = scaler.transform(input_data)

if st.button('Predict Segment'):

    cluster = kmeans.predict(input_scaled)[0]

    st.success(f'Predicted Segment: Cluster {cluster}')

    st.write(""""
            **\nCluster Description
             
                **Cluster 0 : Web Visitors, Store Visitors

                **Cluster 1 : Most Recent Customers

                **Cluster 2 : Oldest Customers, Second highest Earners and Spenders

                **Cluster 3 : lowest income earners, lowest spenders

                **Cluster 4: Highest income earners and spenders

                **Cluster 5 : Dormant Customers

             """)
    
