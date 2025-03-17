import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv('C:/Users/turne/Project4/vehicles_us.csv')

df['cylinders'] = pd.to_numeric(df['cylinders'])
df['cylinders'] = df['cylinders'].astype('Int64')
df['date_posted'] = pd.to_datetime(df['date_posted'])

df['model_year'] = df['model_year'].fillna('Unknown')
df['cylinders'] = df['cylinders'].fillna(0)
df['odometer'] = df['odometer'].fillna('NaN')
df['paint_color'] = df['paint_color'].fillna('Unknown')
df['is_4wd'] = df['is_4wd'].replace(np.nan, 0).astype(bool)

st.header('4WD vs Non-4WD Vehicle Sale Time')
fig = px.histogram(df, x='days_listed', color='is_4wd', title='Sale Time for 4WD vs Non-4WD Vehicles',
                   labels={'days_listed': 'Days Listed', 'is_4wd': '4WD Vehicle'},
                   nbins=30)
st.write(fig)