# Offers Page
import streamlit as st
import pandas as pd

col1, col2 = st.columns([3,1], vertical_alignment='center')
with col1:
    st.title("Offers")
with col2:
    if st.button(":material/refresh: Refresh", type='tertiary'):
        del st.session_state.offers
        st.rerun()

if 'offers' not in st.session_state:
    with st.spinner("Loading offers sheet..."):
        sheet_id = "1S2atXi2BwxcT_PujJIJzv0N1-yifDgCnBTBjjV-s3MY"
        csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
        st.session_state.offers = pd.read_csv(csv_url)
        st.session_state.offers = st.session_state.offers.transpose().reset_index(drop=True)
        st.session_state.offers.columns = st.session_state.offers.iloc[0,:]
        st.session_state.offers = st.session_state.offers.iloc[1:,:]
        st.session_state.offers = st.session_state.offers.reset_index(drop=True)
        custom_order = {
            'High Priority': 0, 
            'Mid Priority': 1, 
            'Low Priority': 2, 
            'Temp Hold': 3, 
            'Hold': 4
        }
        st.session_state.offers = (st.session_state.offers.sort_values(by='Status', key=lambda x: x.map(custom_order)).reset_index(drop=True))

tabs = st.tabs(st.session_state.offers["Company's Name"].to_list())
df = st.session_state.offers.copy()

for i in range(2,len(df)):
    # print(df.iloc[i,0])
    info = {
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
    

    # ______________________________________________________________________________
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
        if st.session_state.user_type=='recruiter':
            info.pop('Commission TL')
            info.pop('Commission UM')
        st.dataframe(pd.DataFrame(list(info.items()), columns=['Information','Value']), hide_index=True, width='stretch', height='content')
        st.write("**Offer details:**")
        st.markdown(f"```\n{details}\n```", unsafe_allow_html=True, )
