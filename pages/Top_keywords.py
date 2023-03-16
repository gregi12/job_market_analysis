import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Pobierz aktualną ścieżkę do folderu, w którym znajduje się plik Top_key.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Utwórz ścieżkę do pliku csv używając ścieżki bazowej i folderu files
csv_path = os.path.join(BASE_DIR, '..', 'files', 'keywordsfull.csv')

# Wczytaj plik csv do dataframe
df = pd.read_csv(csv_path)
# Uploading dataframe


# Tabs section
st.write('Choose format of the data')
tab1, tab2 , tab3= st.tabs(["Quantity", "Percentage", "Table"])

with tab1:

  st.subheader('Top 15 keywords by amount 📊')
  fig = plt.figure()
  plt.bar(df['keywords'], df['amount'])
  plt.xticks(rotation=90)
  plt.ylabel('Amount')

  # Display chart in Streamlit app
  st.pyplot(fig)
  

with tab2:
# Create bar chart sorted by value
  st.subheader('Top 15 keywords by percentage 📊')
  fig = plt.figure()
  plt.bar(df['keywords'], df['percentage'])
  plt.xticks(rotation=90)
  plt.ylabel('%')

  # Display chart in Streamlit app
  st.pyplot(fig)

with tab3:
  st.write(df)