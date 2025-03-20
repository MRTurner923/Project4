import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv('vehicles_us.csv')

#Altering data types for use later on in the project
df['cylinders'] = pd.to_numeric(df['cylinders'])
df['cylinders'] = df['cylinders'].astype('Int64')
df['date_posted'] = pd.to_datetime(df['date_posted'])

#Cleaning up and filling in missing data
df['model_year'] = df['model_year'].fillna('Unknown')
df['cylinders'] = df['cylinders'].fillna(0)
df['odometer'] = df['odometer'].fillna(0)
df['paint_color'] = df['paint_color'].fillna('Unknown')
df['is_4wd'] = df['is_4wd'].replace(np.nan, 0).astype(bool)

#Added manufacturer column and convert to string for later analysis
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0].title())
df['manufacturer'] = df['manufacturer'].astype(str)

#Histogram comparing days listed between 4WD and non-4WD vehicles
st.header('4WD vs Non-4WD Vehicle Sale Time')
fig_4wd = px.histogram(df, x = 'days_listed', color = 'is_4wd',
                   labels = {'days_listed': 'Days Listed', 'is_4wd': '4WD Vehicle'},
                   color_discrete_map={True: 'blue', False: 'red'},
                   nbins=50)
st.write(fig_4wd)

#Bar graph comparing average sale price by paint color
avg_price_by_paint = df.groupby('paint_color')['price'].mean().reset_index()
st.header('Average Sale Price by Paint Color (USD)')
fig_paint = px.bar(avg_price_by_paint,
                   x = 'paint_color',
                   y = 'price',
                   labels = {'paint_color': 'Paint Color', 'price': 'Average Price ($)'},
                   color = 'paint_color',
                    color_discrete_map = {
                       'white': 'lightblue', 'red': 'red', 'black': 'black', 'blue': 'blue', 'grey': 'grey', 'silver': 'silver', 
                       'custom': 'gold', 'orange': 'orange', 'yellow': 'yellow', 'brown': 'brown', 'green': 'green', 'purple': 'purple'})
st.write(fig_paint)

#Find all vehicles with odometer readings > 100,000 miles
high_mileage = df[df['odometer'] > 100000]
#Filter resulting df to vehicle types SUV, sedan, pickup, coupe
high_mileage_of_interest = high_mileage[high_mileage['type'].isin(['SUV', 'sedan', 'pickup', 'coupe'])]
#Group by type and compare average prices
avg_price_high_mileage = high_mileage_of_interest.groupby('type')['price'].mean().reset_index()
#Bar graph comparing average sales price of high mileage sedans, coupes, pickup trucks, and SUVs
st.header('Average Resale Price of High Mileage (> 100,000 miles) Sedans/Coupes and Pickup Trucks/SUVs')
fig_mileage = px.bar(avg_price_high_mileage, x = 'type', y = 'price', color = 'type',
                   labels = {'type': 'Type', 'price': 'Price'},
                   color_discrete_map = {'SUV': 'blue', 'coupe': 'red', 'pickup': 'green', 'sedan': 'purple'})
fig_mileage.update_layout(yaxis_title = "Average Price (USD)")
st.write(fig_mileage)

#Scatter plot showing sale price of each vehicle from each manufacturer in the dataset
st.header('Price vs Manufacturer')
fig_price_manufacturer = px.scatter(df, x = 'manufacturer', y = 'price', color = 'manufacturer',
                 color_discrete_map = {
                     'Bmw': 'lightblue', 'Ford': 'red', 'Hyundai': 'black', 'Chrysler': 'blue', 'Toyota': 'grey',
                     'Honda': 'silver', 'Kia': 'gold', 'Chevrolet': 'orange', 'Ram': 'yellow', 'Gmc': 'brown',
                     'Jeep': 'green', 'Nissan': 'purple', 'Subaru': 'lightgreen', 'Dodge': 'darkblue',
                     'Mercedes-Benz': 'coral', 'Acura': 'indigo', 'Cadillac': 'teal', 'Volkswagen': 'plum',
                     'Buick': 'salmon'
                 })
st.write(fig_price_manufacturer)
