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
  
  st.subheader('Top 5 by amount of offers found📊')
  fig = plt.figure()
  colors = ['#D2042D', '#702963', '#C04000','#8F8585','#bdbdbd'] 
  plt.bar(providers['Via'], providers['Amount'],color=colors,edgecolor='black',linewidth=1)
  plt.xticks(rotation=90)
  plt.ylabel('Amount')
  # Display chart in Streamlit app
  st.pyplot(fig)
  

with tab2:

  st.subheader('Top 5 by amount of offers found📊')
# Create bar chart sorted by value
  labels = [key for key in providers['Via']]
  keys = [key for key in providers['Percentage']]
  colors = ['#D2042D', '#05D832', '#D5E901','#8F8585','#bdbdbd'] 
  fig, ax = plt.subplots()
  
  ax.pie(keys, labels=labels, 
        startangle = 90,
        autopct='%1.1f%%',
        colors=colors
        )
  
  st.pyplot(fig)





with tab3:
  st.write(providers)