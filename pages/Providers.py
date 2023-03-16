import os
# Pobierz aktualną ścieżkę do folderu, w którym znajduje się plik Top_key.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Utwórz ścieżkę do pliku csv używając ścieżki bazowej i folderu files
csv_path = os.path.join(BASE_DIR, '..', 'files', 'Sitesfull.csv')
providers = pd.read_csv(csv_path)


st.subheader('Top offers providers 📊')

st.write(providers)
#providers_chart = alt.Chart(providers).mark_bar().encode(
 # x=alt.X('providers', sort=None),y= 'via'
#)
#st.altair_chart(providers_chart,use_container_width=True)