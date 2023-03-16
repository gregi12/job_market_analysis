
import sys
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
sys.path.append(r'C:\Users\komputer\Desktop\aktualne\environment\serpapi\job_analysis\Lib\site-packages')
st.set_page_config(
  page_title='Job market analsysis',
  page_icon = '📊'
)
# Expander section
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

df =pd.read_csv('keywords.csv')
df = df.sort_values('amount',ascending=False)

# Create bar chart sorted by value
plt.bar(df['keywords'], data['amount'])
plt.xticks(rotation=90)
plt.title('Sorted Bar Chart')
plt.xlabel('Category')
plt.ylabel('Value')

# Display chart in Streamlit app
st.pyplot()







# Display chart in Streamlit app
st.altair_chart(chart, use_container_width=True)
st.subheader('Top 15 keywords 📊')
st.bar_chart(df,x = 'keywords',y='amount')

# Dataframe and Chart display section
st.subheader('Interactive Data Table')

st.dataframe(df) 



st.subheader('Top offers providers 📊')
# Image upload and text input section
providers = pd.read_csv('Diffrent_sites.csv')
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

