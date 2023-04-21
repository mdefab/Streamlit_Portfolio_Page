import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="contact_form"):
    email = st.text_input(label="Please enter your email address:")
    message = st.text_area(label="Your Message:")
    submit = st.form_submit_button(label="submit")

    if submit:
        send_email(email, message)
        st.info("Thank you for your email. I will respond as soon as possible!")