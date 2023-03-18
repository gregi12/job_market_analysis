import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Pobierz aktualną ścieżkę do folderu, w którym znajduje się plik Top_key.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Utwórz ścieżkę do pliku csv używając ścieżki bazowej i folderu files
csv_path = os.path.join(BASE_DIR, '..', 'files', 'Typefull.csv')

# Wczytaj plik csv do dataframe
df = pd.read_csv(csv_path)
# Uploading dataframe


# Tabs section
st.subheader("Schedule type ")
st.write('Choose format of the data')
tab1, tab2 , tab3= st.tabs(["Quantity", "Percentage", "Table"])

with tab1:
    st.subheader('Top types of contract📊')
    fig = plt.figure()
    colors = ['#D2042D', '#702963', '#C04000','#8F8585','#bdbdbd'] 
    plt.bar(providers['Via'], providers['Amount'],color=colors,edgecolor='black',linewidth=1)
    plt.xticks(rotation=90)
    plt.ylabel('Amount')
    # Display chart in Streamlit app
    st.pyplot(fig)
