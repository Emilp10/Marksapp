import streamlit as st
import pandas as pd
import os

# Sidebar with radio buttons for navigation (Login or Sign Up)
st.sidebar.title("Navigation")
option = st.sidebar.radio('Select an option:', ['Login', 'Sign Up'])

# Function to load or initialize the CSV file
def load_or_initialize_csv():
    if not os.path.exists('users.csv'):
        df = pd.DataFrame(columns=['Name', 'Password', 'Mobile', 'City'])
        df.to_csv('users.csv', index=False)
    return pd.read_csv('users.csv')

# Sign Up page
if option == 'Sign Up':
    st.title('Sign Up to your Journey')

    name = st.text_input('Enter your name')
    password = st.text_input('Enter your password', type='password')
    mobile = st.text_input('Enter your mobile number')
    city = st.text_input('Enter your city')

    if st.button('Sign Up'):
        df = load_or_initialize_csv()
        
        # Check if the username already exists
        if name in df['Name'].values:
            st.write('Username already taken')
        else:
            # Append the new user data to the DataFrame
            new_data = pd.DataFrame({'Name': [name], 'Password': [password], 'Mobile': [mobile], 'City': [city]})
            df = pd.concat([df, new_data], ignore_index=True)
            
            # Save the updated DataFrame back to the CSV
            df.to_csv('users.csv', index=False)
            st.write('Sign Up successful')

# Login page
if option == 'Login':
    st.title('Login to your Account')

    name = st.text_input('Enter your name')
    password = st.text_input('Enter your password', type='password')

    if st.button('Login'):
        df = load_or_initialize_csv()
        
        # Check if the username and password are correct
        if name in df['Name'].values:
            user_data = df[df['Name'] == name]
            if user_data.iloc[0]['Password'] == password:
                st.write('Login successful')
            else:
                st.write('Incorrect password')
        else:
            st.write('Username not found')
