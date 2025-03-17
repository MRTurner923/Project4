import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv('vehicles_us.csv', low_memory = False)
#df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])
print(df.info())

#st.header('Data Viewer')
#st.dataframe(df)

#st.header('Vehicle types by manufacturer')
# create a plotly histogram figure
#fig = px.histogram(df, x='manufacturer', color='type')
# display the figure with streamlit
#st.write(fig)