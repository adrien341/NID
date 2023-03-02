import streamlit as st
import pandas as pd
import numpy as np


def random_nid(taxon_list):
        return np.random.choice(taxon_list)

# load species.csv
df = pd.read_csv(r'species.csv')
#print(df)
taxon_rare = df[df["count"] < 10000]
taxon_list = taxon_rare.name.tolist()
your_pokemon = random_nid(taxon_list)

st.title("""
Bienvenue, etudiant.e de la 4e promotion Master NID.
""")
st.write('Cette application te donnera une espèce, ou un groupe taxonomique sur lequel chercher de la donnée, le temps d un exercice')
submit = st.button("Donne moi un taxon !")
if submit:
   st.header(your_pokemon)
 

st.write("Maintenant, cultive-nous sur ce taxon, en allant sur https://itn5front-y5c3h4ocuq-wl.a.run.app/" )
