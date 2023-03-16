
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(
  page_title='Job market analsysis',
  page_icon = '📊'
)
# Expander section
st.subheader("Hello, I'm glad to present you results of my analysis")
with st.expander("Here I explain how I obtained data"):
  st.write("https://github.com/gregi12/Jobs-offers-project/blob/master/getting_data.py")

# Sidebar section
with st.sidebar:
  st.subheader('This is a Sidebar')
  st.write('Button with Balloons 🎈')
  if st.button('Click me!✨'):
    st.balloons()
  else:
    st.write(' ')



st.subheader('Follow instruction below to continue!')
greet = st.text_input('Write your name, please!')
if greet:
  st.write('👋 Hey! ',greet," it's nice to meet you" )
  original_title = '<p style="font-family:Courier; font-size: 20px;">My name is Grzegorz and as we already know each other and you are still here I will give brief overview of this analysis, app and maybe few words about me.</p>'
  st.markdown(original_title, unsafe_allow_html=True)
  st.write(' ')



# Tworzenie trzech przycisków w trzech kolumnach
col1, col2, col3 = st.beta_columns(3)

# Dodawanie przycisków do kolumn
with col1:
    button1 = st.button("Przycisk 1")

with col2:
    button2 = st.button("Przycisk 2")

with col3:
    button3 = st.button("Przycisk 3")