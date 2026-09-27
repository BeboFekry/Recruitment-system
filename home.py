# Home Page - Tutorial
import streamlit as st

# st.title("Home")

# st.header("HR Recruitment Tutorial - Abdallah's Team", divider='blue')
st.image(r"C:\Users\lenovo\Downloads\Picsart_26-09-27_16-54-36-501.png")

offers = st.Page('offers.py')
dashboard = st.Page('dashboard.py')
chatbot = st.Page('chat.py')
booking = st.Page('booking.py')

if st.session_state.logged_in:
    col1, col2, col3, col4 = st.columns([1.1,1.4,1.3,0.8], vertical_alignment='top')
    with col1:
        if st.button(":blue[:material/article:] Offers", type='tertiary', width='content'):
             st.switch_page(offers)
    with col2:
            if st.button(":blue[:material/article:] Booking Sheet", type='tertiary', width='content'):
                st.switch_page(booking)
            # st.link_button(":blue[:material/article:] Booking Sheet", 'https://docs.google.com/spreadsheets/d/102wYZPgUzyRqfxmmy2gWSGqrmEMvzfG-jzurOir4Qro/edit?gid=0#gid=0', type='tertiary')
    with col3:
        if st.button(":blue[:material/smart_toy:] Chatbot", type='tertiary'):
            st.switch_page(chatbot)
    with col4:
        if st.button(":blue[:material/bar_chart:] Dashboard", type='tertiary'):
            st.switch_page(dashboard)


st.header("HR Recruitment Tutorial - Abdallah's Team", divider='blue')
st.subheader("Agenda")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    1. Introduction
    2. Media & Posting                                 
    3. Engaging with the candidates
    4. Evaluation                                                    
    5. Interviewing & Process
    6. Follow Up
    7. Commissions                                               
    8. Final tips & takeaways            
    """)
with col2:
    st.markdown("""
    * المقدمة
    * الميديا والبوستات
    * التعامل مع المتقدمين
    * التقييم                                          
    * اكمال العملية والانترفيو
    * المتابعة
    * العمولات
    * شوية نصائح ع الماشي
    """, text_alignment='right')

st.divider()

st.subheader("Introduction - مقدمة وتعريف")
st.markdown(
"""احنا مين وبنعمل ايه؟

اولا احنا احنا الوسيط مابين شركات الكول سنتر والمتـقدميـن للشغل احنا مسئوليـن عن جانب الميديا بننزل اعلانات ال       بغض النظر علي انهي منصة وبعديـن الناس بتـقدم بنتأكد انهم مناسبـيـن حسب احتياجات الشركة والشروط ونرشحهم للشركة لو تمام واتـقبل بتاخد الكوميشن بتاعك
""", text_alignment='right')
st.divider()
st.subheader("Recruitment Process Steps")
st.image('media/recruitment steps.svg')
st.divider()
