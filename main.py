import streamlit as st

st.title('Hello World')
st.subheader('This is a subheader')

#take some input from the user and display it
name = st.text_input('Enter your name')
st.write('Hello', name)

maths = st.slider('Enter your math marks', 0, 100)
st.write(name, 'scored', maths, 'marks in maths')

exam = st.radio('How was your exam?', ['Good', 'Average', 'Bad'])
st.write('You felt the exam was', exam)

subjects = st.multiselect('Select your favourite subjects', ['Maths', 'Science', 'English'])
st.write('You chose', subjects)

#take an excel file as input and save it to current directory and dispaly the file with data in it
import pandas as pd
uploaded_file = st.file_uploader('Choose a file', type='xlsx')
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write(df)