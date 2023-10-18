import streamlit as st
import pandas as pd
import numpy as np
import ast

#to view this Streamlit app on a browser, run it with the following   command: streamlit run streamlite_NID.py

def random_nid(taxon_list):
        return np.random.choice(taxon_list)

# load species.csv
df = pd.read_csv(r'species_w2v.csv')
#print(df)

# warning : Some taxa are over reprensented, hence the artificial threshold here
taxon_rare = df[df["count"] < 50]
# creation of a list
taxon_list = taxon_rare.name.tolist()
your_pokemon = ast.literal_eval(random_nid(taxon_list))[0][0]

st.title("""
🎲 Random Taxon 🎲
""")
#st.markdown(''':gray[Made by]''')
#st.write("[CEEBIOS](https://ceebios.com/)")
st.write('Cette application tire au sort une espèce, ou un groupe taxonomique.')
submit = st.button("Donne-moi un taxon !")
if submit:
   st.header(your_pokemon)
 

st.write("Maintenant, obtenons de la donnée sur ce taxon, en allant sur https://bioinspire-explore.mnhn.fr/" )

