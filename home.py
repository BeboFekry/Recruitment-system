# Home Page - Tutorial
import streamlit as st

# st.title("Home")


# st.header("HR Recruitment Tutorial - Abdallah's Team", divider='blue')
st.image(r"media/Picsart_26-09-27_16-54-36-501.png")

offers = st.Page('offers.py')
dashboard = st.Page('dashboard.py')
chatbot = st.Page('chat.py')
booking = st.Page('booking.py')

# st.button("Link")
# if st.session_state.logged_in:
col1, col2, col3, col4 = st.columns([1.1,1.4,1.3,0.8], vertical_alignment='top')
with col1:
    # st.page_link(offers)
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
"""GTX Agency احنا مين وبنعمل ايه؟ اولا احنا

احنا الوسيط مابين شركات الكول سنتر والمتـقدميـن للشغل احنا مسئوليـن عن جانب الميديا بننزل اعلانات الهايرينج بغض النظر علي انهي منصة وبعديـن الناس بتـقدم بنتأكد انهم مناسبـيـن حسب احتياجات الشركة والشروط ونرشحهم للشركة لو تمام واتـقبل بتاخد الكوميشن بتاعك
""", text_alignment='right')
st.divider()
st.subheader("Recruitment Process Steps")
st.image('media/recruitment steps.png')
st.divider()


# st.Page(offers, title='لما تخش علي صفحة الاوفرات دي هتلاقي التفاصيل دي كلها')
explain = """
**Company Name** :material/arrow_forward:  اسم الشركة

**Status** :material/arrow_forward:  حالة الاوفر ودرجة الاولوية شغال ولا هولد

**Form** :material/arrow_forward:  evaluation الفورم اللي هتملاها لما اللي معاك يتقبل في ال

**Shifts** :material/arrow_forward:  الشيفتات ومواعيد العمل

**Interview Time** :material/arrow_forward:  مواعيد الانترفيو دة لما الكانديديت يتقبل تححد معه ميعاد منهم

**Location** :material/arrow_forward:  العنوان او مقر عمل الشركة

**Graduation Status** :material/arrow_forward:  Graduate, Undergraduate, Gap year, and Dropouts حالة المؤهل وهنا فيه اربع حالات خريج او طالب او مأجل سنة او سايب التعليم

**Nationality** :material/arrow_forward:  foreigner الجنسية مصري ولا

**Max Age** :material/arrow_forward:  أقصى سن غالبا بيكون من 30 ل35

**Language** :material/arrow_forward:  B2,B2+,C1 مستوى اللغة 

**Salary** :material/arrow_forward:  المرتب

**Process** :material/arrow_forward:  الخطوات اللي الشركة بتتبعها في التوظيف مثلا بيرجعوا الفويس نوت بتاعه الاول او انترفيو عليطول كل شركة ليها البروسيس بتاعتها ولازم تبقي عارفها وباصص فيها

**Account** :material/arrow_forward:  طبيعة العمل او الاكنت مثلا سيلز او سبورت او استطلاع كدا

**Key Features** :material/arrow_forward:  ملخص سريع للمزايا

**Commission Rec** :material/arrow_forward:  الكوميشن بتاعك

**Period** :material/arrow_forward:  المدة اللي هتاخد بعدها الكوميشن وبتتحسب بعد ما يتقبل ويبدأ تدريب وبتكوزن من اسبوع لشهر حسب كل شركة

**Offers Details** :material/arrow_forward:  تفاصيل الاوفر تقدر تدوس كوبي وتنشر منها علي طول ودي اللي بتبعتها للكانديديت لما يسأل عن تفاصيل الاوفر

دلوقتي تقدر تخش علي صفحة الاوفرات وتشوف كل اللي مفتوح
"""
st.markdown(explain)
if st.button("Offers", type='primary'):
     st.switch_page(offers)

st.divider()

explain = """:أول خطوة بننـزل اعلان التوظيف وهنا عندنا اختيارات كتير

(Facebook, LinkedIN, Instagram, Wuzzuf, Indeed, Tiktok, YouTube)

مثلا خلينا في اسهل حاجة خالص جروبات الفيسبوك بتاعة الكول سنتر اللي فيها ريتش عالي فأول حاجة انت محتاجها تخش في الجروبات دي كلها هحطلكوا اللينكات اهي خش في جروب جروب ولو تعرف جروبات تاني خش فيها عادي
"""
st.markdown(explain, text_alignment='right')
fb_groups = ["https://www.facebook.com/share/g/1BqxKb9jsA/", 
             "https://www.facebook.com/share/g/1CuyVNS6dR/", 
             "https://www.facebook.com/share/g/1DWqVB8N8k/",
             "https://www.facebook.com/share/g/1E2NoNVisP/", 
             "https://www.facebook.com/share/g/19g4y9pV7W/",
             "https://www.facebook.com/share/g/19Nn5TttyR/",
             "https://www.facebook.com/share/g/1Mi2rc3KkU/",
             "https://www.facebook.com/share/g/1FCaa81SQb/",
             "https://www.facebook.com/share/g/1BqwyuDPif/",
             "https://www.facebook.com/share/g/194fNNBjRM/",]

cols = st.columns(5)
c = 0
n = 1
for i in range(len(fb_groups)):
    with cols[c]:
        st.link_button(f':blue[Group {i+1} link]', fb_groups[i], type='tertiary')
    c+=1
    c%=5
st.divider()

st.markdown("""البوستين دول تقريبا نفس الوفر ونفس الجروب بس البوست رقم 2 جذاب اكثر لالنتباه وكمان مفهوش كل التفاصيل عشان يبقي شكله منظم اكتر والناس عادي هتسأل علي التفاصيل هنبعت التفاصيل كاملة انبوكس ونعمل ريبالي علي الكومنت بتاعهم. فالبوست هيظهر ويترشح لناس اكثر""", text_alignment='right')
col1, col2 = st.columns(2, vertical_alignment='bottom')
with col1:
    st.image("media/sh1.png", caption='Post 1')
with col2:
    st.image("media/sh2.png", caption='Post 2')
st.divider()


st.markdown("""check your dm يبقى انا دلوقتي هنزل البوست ولو حد سأل هبعتله التفاصيل الكاملة ةسكريبت الفويس نوت واعمله ريبلاي علي الكومنت """, text_alignment='right')
col1, col2 = st.columns(2, vertical_alignment='top')
with col1:
    st.image("media/sh3.png", caption='Post 2')
with col2:
    st.markdown("""
```\nHello this is Folan, HR recruiter from GTX
To apply kindly could you share a record of least 1 minute mentioning your
1. Educational background, 
2. Working Experience.
3. What makes you interested to apply in customers services field?
Please send the voice on WA and mention 
the company name: 01xxxxxxxxx\n```""")
st.divider()


st.markdown("""طيب بعد ما يبعتلك الفويس هتبعت الفويس على جروب الواتس وتبعت معاه البيانات الاساسية 
1. اسم الشركة
2. اسم الكانديديت
3. اخر اربع ارقام فقط من رقم تليفونه
4. خريج ولا لأ
5. خبرته ايه""", text_alignment='right')
col1, col2 = st.columns(2, vertical_alignment='top')
with col1:
    st.image("media/sh4.png", caption='Group Evaluation Process')
with col2:
    st.space('xlarge')
    st.markdown("Case 1: voice note accepted")
    st.markdown("""
```\nCongratulations! You have passed The Quality Step & we will be connecting to the Company Shorly.Do your Best and Good Luck\n```""")
    st.space('large')
    st.markdown("Case 2: voice note rejected")
    st.markdown("""
```\nDear Folan Company-Name decided not to move foraed with your application.
We believe you have great potential. Here is what we believe you might work on:
(Send QA Comment) 
We Believe in you and Have your back To the Beyond!\n```""")
st.divider()
