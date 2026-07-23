import streamlit as st

st.header('media')
n1 = st.number_input('numero 1')
n2 = st.number_input ('numero 2')


media = (n1    +   n2)  / 2

st.info(media)
