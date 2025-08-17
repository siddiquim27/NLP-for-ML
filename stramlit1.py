import streamlit as st
import pandas as pd
import numpy as np


## title
st.title('helllo streamlit app')


# display a simple  text

st.write("this is a simple text")


## create a dataframes 

df = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column' : [10, 20, 30, 40]
})

## display the data frames 
st.write("here is the dataframes")
st.write(df)

## create a line chart 
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns = ['a' , 'b', 'c']
)
st.line_chart(chart_data)