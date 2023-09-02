import streamlit as st
import pandas as pd
import altair as alt

st.header("Mobile Daten: Monatlicher Durchschnittsverbrauch 2021")
st.subheader("Gigabytes je mobilem Breitbandanschluss, ausgewählte EU-Staaten")

source = pd.DataFrame({
        'Gigabytes': [36.7, 26.4, 19.9, 12.6, 10.8, 7.7, 6.0, 4.7, 3.7],
        'Land': ['Finnland', 'Österreich', 'Estland', 'Italien', 'Polen', 'Spanien', 'Deutschland', 'Niederlande', 'Slowakei']
})
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Gigabytes:Q',
        x='Land:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    2023
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: OECD")