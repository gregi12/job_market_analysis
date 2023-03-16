import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Uploading dataframe
df =pd.read_csv('..\\files\\keywordsfull.csv')
df = df.sort_values('amount',ascending=False)

# Tabs section
st.write('Choose format of the data')
tab1, tab2 , tab3= st.tabs(["Quantity", "Percentage", "Table"])

with tab1:

  st.subheader('Top 15 keywords by amount 📊')
  fig = plt.figure()
  plt.bar(df['keywords'], df['amount'])
  plt.xticks(rotation=90)
  plt.xlabel('Keyword')
  plt.ylabel('Amount')

  # Display chart in Streamlit app
  st.pyplot(fig)
  

with tab2:
# Create bar chart sorted by value
  st.subheader('Top 15 keywords by percentage 📊')
  fig = plt.figure()
  plt.bar(df['keywords'], df['amount'])
  plt.xticks(rotation=90)
  plt.xlabel('Keyword')
  plt.ylabel('Amount')

  # Display chart in Streamlit app
  st.pyplot(fig)

with tab3:
  st.write(df)