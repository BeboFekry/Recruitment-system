import streamlit as st


if not st.session_state.logged_in:
    key = st.text_input('Passeowd', type='password')
    if key:
        if key == st.secrets['password']:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Wrong Password!")

if st.session_state.logged_in:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.link_button("Offers Link", 'https://docs.google.com/spreadsheets/d/1S2atXi2BwxcT_PujJIJzv0N1-yifDgCnBTBjjV-s3MY/edit?gid=984832798#gid=984832798', type='tertiary', width='content')
    with col2:
            st.link_button("Booking Link", 'https://docs.google.com/spreadsheets/d/102wYZPgUzyRqfxmmy2gWSGqrmEMvzfG-jzurOir4Qro/edit?gid=0#gid=0', type='tertiary')
    with col3:
            st.link_button("Special Offers Link", '', type='tertiary')
    with col4:
        st.link_button("Special Offers Link", '', type='tertiary')