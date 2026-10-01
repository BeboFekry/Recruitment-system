# Offers Page
import streamlit as st
import pandas as pd

col1, col2 = st.columns([3,1], vertical_alignment='center')
with col1:
    st.title("Offers")
with col2:
    if st.button(":material/refresh: Refresh", type='tertiary'):
        # st.session_state.offers = 0
        del st.session_state.offers
        st.rerun()
# with st.expander("Leadbull"):
#     col1, col2 = st.columns([3,1], vertical_alignment='center')
#     with col1:
#         st.subheader("Leadbull")
#     with col2:
#         st.markdown(":green[High Priority]", text_alignment='right')
    
#     info = {
#         # st.page_link("https://forms.gle/v3hZ3q1DcyygcHaL7", label='Form Link')
#         'Form':"https://forms.gle/v3hZ3q1DcyygcHaL7",
#         'Shifts':'Fixed  \n4:00PM to 1:00 AM',
#         'Interview Time':'* Thursday & Friday  \n* 5 00 PM – 11:00 PM',
#         'Location':':location: Maadi  \nhttps://maps.app.goo.gl/YUDE1JkncuvdHarf9',
#         'Graduation Status':'Grads /Undergrads (no commitment) / Dropouts',
#         'Nationality':'Egyptians',
#         'Max Age':35,
#         'Language':'English B2/C1',
#         'Salary':'15K Net + 5K KPIs',
#         'Process':"1-Screening ( Talent Acq -> Pass/Failed Screening )  \n2-ON-SITE interview ( Panel -> Acp/ Rej Site)",
#         'Account':'Canadian Telesales Account',
#         'Key Features':"""
#         1. Mid Period Commission                  
#         2. EXP Optional
#         3. MIGHT WFH in 3 months
#         4. Unlimitted Commission
#         5. Female and male""",
#         }
#     details= """Offer Details:
            
#                 Company Name: Leadbull
            
#                 🚀 GTX .. We’re Hiring!
#                 🇨🇦 “Canadian Tele sales Account”
            
#                 So easy to target it.
            
#                 Offer:
#                 💰 EGP 15K EGP Basic Salary
#                 🎯 EGP 5K KPIs
#                 💸 Daily spiffs
#                 💸 Quarterly incentives
#                 💸Annual profit share 
            
#                 Job Details:
#                 🕓 Shift: 4 PM – 1 AM 
            
#                 Who We’re Looking For:
#                 🗣️ B2+ English Level or above
            
#                 📍 Company Location: Zahraa El Maadi
#                 (Work from site)
#                 Door to Door Trasportation for Females after Test Call
            
#                 🌟 Availability to work from home after 3 months 🏠
            
#                 Egyptians ONLY"""
#     st.table(info, border=True)
#     st.markdown(details)

# with st.expander("Teleperformance - TP"):
#     st.subheader("TP")


# df = pd.read_csv('data/offers.csv')
# with st.loading
if 'offers' not in st.session_state:
    with st.spinner("Loading offers sheet..."):
        sheet_id = "1S2atXi2BwxcT_PujJIJzv0N1-yifDgCnBTBjjV-s3MY"
        csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
        st.session_state.offers = pd.read_csv(csv_url)
# st.write(st.session_state.offers.columns)
# elif st.session_state.offers==0:
#     with st.spinner("Loading offers sheet..."):
#             sheet_id = "1S2atXi2BwxcT_PujJIJzv0N1-yifDgCnBTBjjV-s3MY"
#             csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
#             st.session_state.offers = pd.read_csv(csv_url)
tabs = st.tabs(st.session_state.offers.loc[2:]["Company's Name"].values)
df = st.session_state.offers.copy()
for i in range(2,len(df)):
    # print(df.iloc[i,0])
    info = {
        # st.page_link("https://forms.gle/v3hZ3q1DcyygcHaL7", label='Form Link')
        'Company Name':df.loc[i]["Company's Name"],
        'Status':df.loc[i]["Status"],
        'Form':df.loc[i]["Form"],
        'Shifts':df.loc[i]["Shifts"],
        'Interview Time':df.loc[i]["Interview time"],
        'Location':df.loc[i]["Location"],
        'Graduation Status':df.loc[i]['Graduation Status'],
        'Nationality':df.loc[i]["Nationality"],
        'Max Age':df.loc[i]["Max Age"],
        'Language':df.loc[i]["Language"],
        'Salary':df.loc[i]["Salary"],
        'Process':df.loc[i]["Process"],
        'Account':df.loc[i]["Account"],
        'Key Features':df.loc[i]["Key Features"],
        # 'Offer details':df.loc[i]["Offer details "],
        'Commission Rec':df.loc[i]["Commission Rec"],
        'Commission TL':df.loc[i]["Commission TL"],
        'Commission UM':df.loc[i]["Commission UM"],
        'Period':df.loc[i]["Period"],
        }
    details = df.loc[i]["Offer details"],
    details = details[0].replace('\n', '  \n')
    
    # tabs = st.tabs(st.session_state.offers)
    
    with tabs[i-2]:
        col1, col2 = st.columns([3,1], vertical_alignment='center')
        with col1:
            st.subheader(info['Company Name'])
        with col2:
            if info['Status'].lower().strip()=='high priority':
                state = f":green[{info['Status']}]"
            elif 'mid' in info['Status'].lower().strip():
                state = f":yellow[{info['Status']}]"
            elif 'low' in info['Status'].lower().strip():
                state = f":orange[{info['Status']}]"
            else:
                state = f":red[{info['Status']}]"

            st.markdown(state, text_alignment='right')
        # st.write(pd.DataFrame(info, columns=['test','value']))
        st.dataframe(pd.DataFrame(list(info.items()), columns=['Information','Value']), hide_index=True, )
        st.write("**Offer details:**")
        # st.code(details, language=None)
        # st.markdown(f"```\n{details}\n```")
        st.markdown(f"```\n{details}\n```", text_alignment='center', unsafe_allow_html=True, )

    # with st.expander(str(i) + ". " + info['Company Name']):
    #     col1, col2 = st.columns([3,1], vertical_alignment='center')
    #     with col1:
    #         st.subheader(info['Company Name'])
    #     with col2:
    #         if info['Status'].lower().strip()=='high priority':
    #             state = f":green[{info['Status']}]"
    #         elif 'mid' in info['Status'].lower().strip():
    #             state = f":yellow[{info['Status']}]"
    #         elif 'low' in info['Status'].lower().strip():
    #             state = f":orange[{info['Status']}]"
    #         else:
    #             state = f":red[{info['Status']}]"

    #         st.markdown(state, text_alignment='right')
    #     # st.write(pd.DataFrame(info, columns=['test','value']))
    #     st.dataframe(info)
    #     st.write("**Offer details:**")
    #     st.markdown(f"{details}", text_alignment='center', unsafe_allow_html=True, )
    # # st.markdown(info)
    # print('_'*100)

