import streamlit as st

username = st.text_input("User")
if username:
    password = st.text_input("Password", type='password')
    
    if st.button("Login", type='primary'):
        if username==st.secrets['username'] and password == st.secrets['password']:
            st.session_state.user_type = 'admin'
            st.success("Login sucessfully!")
        else:
            st.error("Wrong username or password!")
