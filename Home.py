import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.image("images/photo_me.jpg", use_column_width="auto")

with col2:
    st.title("About Me")
    content = """
    Write
    About
    Yourself
    """
    st.write(content)


st.write("Below you can find some of the apps I have built. Feel free to contact me!")


col3, col4 = st.columns(2, gap="large")


df = pandas.read_csv("data.csv", sep=";")
middle_index = (len(df) // 2)

with col3:
    for index, row in df[0:middle_index].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'], use_column_width="auto")
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[middle_index:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'], use_column_width="auto")
        st.write(f"[Source Code]({row['url']})")



# use expanders to hide/show more description for each app