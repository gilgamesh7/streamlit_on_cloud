import streamlit as st
from dotenv import load_dotenv
from os import environ


load_dotenv()

API_KEY_1 = environ.get('API_KEY_1')
API_KEY_2 = environ.get('API_KEY_2')

st.title(f'{API_KEY_1} {API_KEY_2}')

st.image('yellamma.jpg', caption='Protector Mother')