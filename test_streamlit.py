import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px



st.title('Analyse de corrélations Dataframe "voiture"')

st.write("Pour commencer voici le Dataframe en question")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
voitures = pd.read_csv(link)


pays = voitures['continent'].unique()
country_select = st.sidebar.selectbox('Choisir une région:', pays)
filtered_data = voitures[voitures['continent'] == country_select]

st.write(filtered_data)

st.write(" ")
st.write("à l'aide d'une heatmap seaborn on cherche les corrélations")
st.write(" ")

fig, ax = plt.subplots()
sns.heatmap(filtered_data.corr(),cmap="vlag", center= 0, ax=ax)
st.write(fig)

st.write(" ")
st.write("on peut observer un coefficient corrélation négative proche de -1 avec le temps pour arriver à 60mph et la puissance")
st.write(" ")

#ici graph
fig2, ax2 = plt.subplots()
sns.lineplot(x='hp', y='time-to-60', data=filtered_data)
ax2.set(xlabel="Puissance chevaux", ylabel = "Temps pour arriver à 60 miles par heure")
st.pyplot(fig2)

st.write(" ")
st.write("plus la puissance moteur augmente, moins la voiture met de temps à atteindre les 60 mph")
#st.line_chart(df_weather['MAX_TEMPERATURE_C'])

#second graph?
st.write(" ")
st.write("on peut aussi observer que plus le volume du moteur (cubic inches) est élevé, plus la masse du véhicule est élevée")

#graph3
fig3, ax3 = plt.subplots()
sns.lineplot(x='cubicinches', y='weightlbs', data=filtered_data)
ax2.set(xlabel="volume du moteur", ylabel = "masse du véhicule")
st.pyplot(fig3)

st.write("le moteur est la partie la plus lourde du véhicule, mais influe-t-il sur la vitesse?")

fig = px.scatter(filtered_data,
                x='cubicinches',
                y='time-to-60',
                color= 'weightlbs',
                size = 'cubicinches',
                hover_name='time-to-60',
                title=f'Accélération du véhicule en fonction du volume du moteur',
                height=700,
                labels={
                     "cubicinches": "volume du moteur (en pouces)",
                     "time-to-60": "temps pour arriver à 60 miles par heure (en secondes)",
                     "weightlbs": "masse du véhicule    "
                 })

st.plotly_chart(fig,use_container_width=True)

st.write("si on séléctionne le Japon ou les Usa on peut voir que le volume du moteur et la masse totale du véhicule influencent grandement son accélération, en revanche c'est moins vrai pour l'Europe")
