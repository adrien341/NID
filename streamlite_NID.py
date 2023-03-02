import streamlit as st
import pandas as pd
import numpy as np
import ast


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
Bienvenue, etudiant.e de la 4e promotion Master NID.
""")
st.write('Cette application te donnera une espèce, ou un groupe taxonomique sur lequel chercher de la donnée, le temps d un exercice')
submit = st.button("Donne moi un taxon !")
if submit:
   st.header(your_pokemon)
 

st.write("Maintenant, cultive-nous sur ce taxon, en allant sur https://itn5front-y5c3h4ocuq-wl.a.run.app/" )
