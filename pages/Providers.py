import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
# Pobierz aktualną ścieżkę do folderu, w którym znajduje się plik Top_key.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Utwórz ścieżkę do pliku csv używając ścieżki bazowej i folderu files
csv_path = os.path.join(BASE_DIR, '..', 'files', 'Sitesfull.csv')
providers = pd.read_csv(csv_path)


st.subheader('Top offers providers 📊')

st.write('Choose format of the data')
tab1, tab2 , tab3= st.tabs(["Quantity", "Percentage", "Table"])

with tab1:
  
  st.subheader('Top 15 keywords by amount 📊')
  fig = plt.figure()
  colors = ['#de2d26', '#2b8cbe', '#a1d99b'] + ['#bdbdbd'] * 2
  plt.bar(providers['Via'], providers['Amount'],color=colors,edgecolor='black')
  plt.xticks(rotation=90)
  plt.ylabel('Amount')
  # Display chart in Streamlit app
  st.pyplot(fig)
  

with tab2:
# Create bar chart sorted by value
  st.subheader('Top 15 keywords by percentage 📊')
  fig = plt.figure()
  colors = ['#de2d26', '#2b8cbe', '#a1d99b'] + ['#bdbdbd'] * 2
  plt.pie(labels =providers['Percentage'], providers['Via'], color=colors,
        startangle = 90,
        shadow = True
        )
  
  # ustawienie kolorów słupków
 

  # Display chart in Streamlit app
  st.pyplot(fig)





with tab3:
  st.write(providers)