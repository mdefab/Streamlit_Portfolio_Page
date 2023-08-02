import streamlit as st
import pandas
import math

st.set_page_config(layout="wide")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.image("images/photo_me.jpg", use_column_width="auto")

with col2:
    st.title("About Me")
    content = """
    My name is Michael De Fabrizio. I currently work fulltime as a Notary Public, but in my spare time, or when I'm not with a client at work,
    I'm always trying to improve my programming and data analysis skills. Some of the technologies I have worked with include Python, JavaScript, Django, SQL, Regexes, HTML/CSS, Excel/Spreadsheets, and Tableau. 

    Education: Bachelors Degree in Honour's Science in Kinesiology with a minor in Anthropology, and a Juris Doctor degree. 
    Some of the math/stats/economics specific courses I have taken include:
        1) Research Methodology and Data Analysis
        2) Calculus for Life Sciences
        3) Statistical Methods: Science
        4) Epidiomology & Health
        5) Law and Economics
        *Note: many of my other undergrad courses involved statistics

    Please do not hesitate to reach out to me if you have an opportunity you'd like to discuss!
    """
    st.write(content)


st.write("Below you can find some of the apps I have built!")


col3, col4 = st.columns(2, gap="large")


df = pandas.read_csv("data.csv", sep=";")
middle_index = int(math.ceil(len(df) / 2))
print(len(df), middle_index)

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
        st.image("./images/" + row['image'], use_column_width="auto")
        st.write(f"[Source Code]({row['url']})")



# use expanders to hide/show more description for each app