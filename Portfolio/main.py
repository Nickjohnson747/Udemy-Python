import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/1.png")  # , width=)  # TODO: Find an actual photo of myself

with col2:
    st.title("Nick Johnson")
    biography = """sijfgknsfdjgknskdljgnsdlfgksdngsdgkklkjjjkjjjj"""  # TODO: short bio

    st.info(biography)

info_blurb = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(info_blurb)


col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for idx, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for idx, row in df[10:].iterrows():
        st.header(row["title"])
