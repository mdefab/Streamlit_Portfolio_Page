import streamlit as st

st.set_page_config(layout="wide")

with st.sidebar:
    st.write("Home")
    st.write("Contact Me")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo_me.jpg")

with col2:
    st.title("About Me")
    content = """
    Write
    About
    Yourself
    """
    st.write(content)


# use expanders to hide/show more description for each app