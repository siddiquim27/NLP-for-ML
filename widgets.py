import streamlit as st
import pandas as pd


st.title("streamlit text input")

name = st.text_input("Enter your name: ")

age = st.slider("select your age" , 0,100,25)
st.write(f"your age is {age}.")


options = ["python" , "java" , "c++" , "R"]
choice = st.selectbox("choose your fvrt language:" , options)
st.write(f"You selected :  {choice}. ")
if name:
    st.write(f"Hello , {name}")
    



df = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column' : [10, 20, 30, 40]
})

## display the data frames 
st.write("here is the dataframes")
st.write(df)


uploaded_file = st.file_uploader("choose a csv file" , type ="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)