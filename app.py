import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # read the data
st.title('Vehicle Data Explorer')


hist_button = st.checkbox('Build Histogram')

if hist_button:
    # Create a message
    st.write('Building a histogram for the odometer column')
    
    # Create the histogram
    fig_hist = px.histogram(car_data, x="odometer")
    
    # Show the interactive Plotly chart
    st.plotly_chart(fig_hist, use_container_width=True)

scatter_button = st.checkbox('Build Scatter Plot')

if scatter_button:
    # Create a message
    st.write('Building a scatter plot for the odometer and price columns')
    
    # Create the scatter plot
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    
    # Show the interactive Plotly chart
    st.plotly_chart(fig_scatter, use_container_width=True)

