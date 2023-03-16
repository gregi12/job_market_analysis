
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
  st.write('👋 Hey ',greet," , it's nice to meet you!" )
  original_title = '<p style="font-family:Courier; font-size: 20px; font-weight:600;">My name is Grzegorz. As we already know each other and you are still here I will give brief overview of this analysis, app and maybe few words about me.</p>'
  st.markdown(original_title, unsafe_allow_html=True)
  st.write(' ')

  st.write('If someone is wondering...')
  with st.expander("Here I explain how I obtained data"):
    st.write("https://github.com/gregi12/Jobs-offers-project/blob/master/getting_data.py")
    # Tworzenie trzech przycisków w trzech kolumnach
  col1, col2, col3 = st.beta_columns(3)

  # Dodawanie przycisków do kolumn
  with col1:
      if st.button("About analysis"):
        original_title = '<p style="font-family:Calibri; font-size: 20px; font-weight:600;">Sooo, these results comes from over 1200 job offers. Above is link to github file where I give more detailed explanation about how I obtained the data.</p>'
        st.markdown(original_title, unsafe_allow_html=True)
  with col2:
      if st.button("About app"):
        original_title = '<p style="font-family:Calibri; font-size: 20px; font-weight:600;">In upper left corner you can see navigation links, every one of them is for specific aspect. Whenever there is info about percentage , it means percentage of all offers after I deleted duplicates, so on 994 offers. </p>'
        st.markdown(original_title, unsafe_allow_html=True)

  with col3:
      if st.button("About me"):
        original_title = '<p style="font-family:Calibri; font-size: 20px; font-weight:600;">Sooo, these results comes from over 1200 job offers. Above is link to github file where I give more detailed explanation about how I obtained the data.</p>'
        st.markdown(original_title, unsafe_allow_html=True)


