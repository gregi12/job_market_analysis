

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



st.subheader('Text Input')
greet = st.text_input('Write your name, please!')
if greet:
  st.write('👋 Hey! ',greet )
  st.write('')



