import streamlit as st
import base64

st.logo("media/Logo.png", size='large')

about = """HR Recruiter Tutorial - Abdallah's Team"""
menu_items = {
"Get help": "mailto:@abdallahfekry95@gmail.com",
"About": about}
st.set_page_config(page_title="Recruiter", page_icon='media/icon.png', initial_sidebar_state='collapsed', layout='centered', menu_items=menu_items)

def set_bg_video(video_file):
  with open(video_file, "rb") as f:
    encoded_video = base64.b64encode(f.read()).decode()

  html_code = f"""
    <style>
    MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    # header {{visibility: hidden;}}

    .video-background {{
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        z-index: -1;
        object-fit: cover;
    }}

    .stApp {{
        background: transparent !important;
    }}
    </style>

    <video autoplay muted loop class="video-background">
        <source src="data:video/mp4;base64,{encoded_video}" type="video/mp4">
        متصفحك لا يدعم عرض الفيديو.
    </video>
    """
  st.markdown(html_code, unsafe_allow_html=True)

set_bg_video(r"media/bg_video.webm")

if "first_time" not in st.session_state:
  st.session_state.first_time = True
if "logged_in" not in st.session_state:
  st.session_state.logged_in = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "user_type" not in st.session_state:
  st.session_state.user_type = 'recruiter'


home = st.Page("home.py", title="Home", icon=":material/home:", default=True)
chat = st.Page("chat.py", title="Chatbot", icon=":material/smart_toy:")
offers = st.Page("offers.py", title="Offers", icon=":material/article:")
dashboard = st.Page("dashboard.py", title="Dashboard", icon=":material/bar_chart:")
booking = st.Page("booking.py", title="Booking", icon=":material/sticky_note_2:")
settings = st.Page("settings.py", title="Management", icon=":material/settings:")
pg = st.navigation([home, offers, chat, dashboard, booking, settings])

pg.run()
