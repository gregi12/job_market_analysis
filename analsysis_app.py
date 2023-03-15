import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Expander section
with st.expander("About"):
  st.write("""Trying to add a data table, chart, sidebar button with 
          ballons, an image, text input & exploring tabs!""")

# Sidebar section
with st.sidebar:
  st.subheader('This is a Sidebar')
  st.write('Button with Balloons 🎈')
  if st.button('Click me!✨'):
    st.balloons()
  else:
    st.write(' ')

# Dataframe and Chart display section
st.subheader('Interactive Data Table')

df =pd.read_csv('slownik.csv')
st.dataframe(df) 


st.subheader('Bar Chart 📊')
st.bar_chart(df,x = 'keywords',y='amount')

st.subheader('Most Wanted📊')
df1 = pd.dataFrame(['Excel','Degree','SQL','Making reports','SSIS','Tableau','Python'],
                   [416,340,328,298,224,153,147])
st.bar_chart(df1)
# Image upload and text input section
st.subheader('An Image')
st.image('https://www.scoopbyte.com/wp-content/uploads/2019/12/tom-and-jerry.jpg')

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
