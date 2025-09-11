import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

## Taking the text input from the user
name = st.text_input("Enter your name:")

## Create a Slider
age = st.slider("Enter your age:",0,100,25)
st.write(f"Your age is {age}")

## Create a selectbox
options = ["Python", "C++", "Java", "JavaScript"]
choice = st.selectbox("Choose your favourite programming language:",options)
st.write(f"You selected {choice}")

if name:
    st.write(f"Hello {name}")   

data = {
    "Name" : ["John", "Jane", "Jack", "Jill"],
    "Age" : [23, 25, 22, 24],
    "City" : ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sample.csv")
st.write(df)

## Create a upload button
uploaded_file = st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)