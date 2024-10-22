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


col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
print(len(df))


def write_content():
    st.header(row["title"])
    st.write(row["description"])
    st.image("images/" + row["image"])
    st.write(f"[Source Code]({row['url']})")


mid = len(df) // 2
with col3:
    for idx, row in df[:mid].iterrows():
        write_content()

with col4:
    for idx, row in df[mid:].iterrows():
        write_content()
