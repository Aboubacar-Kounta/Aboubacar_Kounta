import streamlit as  st

# 1. Titre principal
st.title("TECHNICIEN  GEOMATICIEN")
# profil
st.header(" ")
st.write(" Spécialiste de la donnée géographique,je combine l'expertise des levées de terrain avec la puissance de l'analyse numérique. Mon objectif est de transformer des mesures complexes en de decision visuel et précis.Que ça soit pour structurer un cadastre, optimiser une logistique urbaine ou modéliser des infrastructures de génie civil, j'apporte une vision qui allie la réalité du sol à la puissance numérique.  ")
        
#st.audio("")
with st.sidebar:
    st.header("Aboubacar Kounta")
    st.write("Géomaticien")
    st.sidebar.markdown("## ** Informations personnelles **")
    st.write("")
    st.write("Adresse: Dakar, Sénégal")
    st.write(" Mail: Kontaa508@gmail.com")
    st.write("")  
st.divider() 
# 5. Formations
st.subheader("Parcours Académiques ")
st.write("2025-2027 - BREVET DE TECHNICIEN SUPÉRIEUR EN GEOMATIQUE")
st.write(" 2021-2022 - LICENCE SCIENCES JURIDIQUES ")
st.write("2021 - CABLAGE INFORMATIQUE  ")
st.write(" 2018-2019 -BACCALAUREAT LETTRES ET SCIENCES HUMAINES ")

# 3. Compétences
st.subheader("Compétences Pratiques ")
st.write("QGIS")
st.write("ArcGIS")
st.write("Autocad")
st.write("Niveau de Chantier")
st.write("Cartographie")
st.write("Topographie")
st.write("Station Totale")
st.write("Pilotage de Drone")
st.write("Télédétection")
st.write("Photogrammétrie")
st.write("Python (Automatisation des Données )")
st.write("Suite Office")


# 6. message de contact 
st.write("---")
message = st.text_input("Laissez-moi un message :")
if st.button("Envoyer"):
    st.write("Merci ! Message reçu :", message)