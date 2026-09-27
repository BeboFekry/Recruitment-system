import streamlit as st

import os
st.write(os.getcwd())
st.write(os.listdir())
st.logo("media/logo.png", size='large')

about = """Findora is an AI-powered product assistant designed to simplify the process of finding, 
comparing, and purchasing products. The system leverages advanced Artificial Intelligence 
techniques, including Large Language Models (LLMs) and agent-based workflows, to deliver 
personalized and data-driven recommendations."""
menu_items = {
"Get help": "mailto:@abdallahfekry95@gmail.com",
"About": about}
st.set_page_config(page_title="Findora", page_icon='media/icon.png', initial_sidebar_state='collapsed', layout='centered', menu_items=menu_items)

if "first_time" not in st.session_state:
  st.session_state.first_time = True
if "logged_in" not in st.session_state:
  st.session_state.logged_in = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# def logoutt():
#     st.session_state.logged_in = False
#     st.rerun()

home = st.Page("home.py", title="Home", icon=":material/home:", default=True)
chat = st.Page("chat.py", title="Chatbot", icon=":material/smart_toy:")
offers = st.Page("offers.py", title="Offers", icon=":material/article:")
dashboard = st.Page("dashboard.py", title="Dashboard", icon=":material/bar_chart:")
booking = st.Page("booking.py", title="Booking", icon=":material/settings:")
settings = st.Page("settings.py", title="Management", icon=":material/settings:")
# test = st.Page("test.py", title="Test", icon=":material/settings:")
# testbot = st.Page("testbot.py", title="Test Bot", icon=":material/smart_toy:")
# manual = st.Page("manual_search.py", title="Manual Search", icon=":material/search:")
pg = st.navigation([home, offers, chat, dashboard, booking, settings])

# if st.session_state.logged_in:   
# else:
#    pg = st.navigation(default_pages)

pg.run()
