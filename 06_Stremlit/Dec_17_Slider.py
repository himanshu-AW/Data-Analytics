import streamlit as st
number = st.slider("Pick a number", 0, 100, 50)
st.write(f"You selected: {number}")