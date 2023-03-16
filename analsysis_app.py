

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


st.subheader('Top offers providers 📊')
# Image upload and text input section
providers = pd.read_csv(r'pages\files\keywordsfull.csv')
st.write(providers)
#providers_chart = alt.Chart(providers).mark_bar().encode(
 # x=alt.X('providers', sort=None),y= 'via'
#)
#st.altair_chart(providers_chart,use_container_width=True)
st.subheader('Text Input')
greet = st.text_input('Write your name, please!')
st.write('👋 Hey!', greet)


# Tabs section
st.subheader('Tabs')
tab1, tab2 = st.tabs(["TAB 1", "TAB 2"])

with tab1:
  st.write('WOW!')
  st.image("https://i.gifer.com/DJR3.gif", width=400)

with tab2:
  st.write('Do you like ice cream? 🍨')
  agree = st.checkbox('Yes! I love it')
  disagree = st.checkbox("Nah! 😅")
  if agree:
    st.write('Even I love it 🤤')
  if disagree:
    st.write('You are boring 😒')

