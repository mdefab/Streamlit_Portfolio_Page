import streamlit as st

st.header("Contact Me")

with st.form(key="contact_form"):
    st.text_input(label="Please enter your email address:", key="email")
    st.text_area(label="Your Message:", key="description")
    submit = st.form_submit_button(label="submit")

    if "submit":
        print(f"{st.session_state.email} wants to know {st.session_state.description}")