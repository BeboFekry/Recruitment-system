# Dashboard Page
import streamlit as st
import pandas as pd
import plotly.express as px

# st.title("Dashboard")

# col1, col2 = st.columns(2)
# with col1:
#     st.subheader("Top Acheiver: ")
# with col2:
#     
# if st.button("Show top achiever ->"):
#     st.balloons()
#     st.subheader(":orange[:material/crown:] Rahma Mohamed -> 11 candidates")


sheet_id = "102wYZPgUzyRqfxmmy2gWSGqrmEMvzfG-jzurOir4Qro"
csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"


df = pd.read_csv(csv_url)

recruiter_counts = df['Recruiter Name'].value_counts().reset_index()[1:]

# st.write(recruiter_counts)
# with st.container(border=True):
if st.session_state.first_time:
    st.balloons()
    st.session_state.first_time = False
st.subheader(':orange[:material/crown:] Top Achievers board')
# st.write()
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(":orange[1st] "+recruiter_counts.loc[1]['Recruiter Name'] + ' :orange[:material/crown:]', recruiter_counts.loc[1]['count'], border=True)
with col2:
        st.metric(":orange[2nd] "+recruiter_counts.loc[2]['Recruiter Name'], recruiter_counts.loc[2]['count'], border=True)
with col3:
        st.metric(":orange[3rd] "+recruiter_counts.loc[3]['Recruiter Name'], recruiter_counts.loc[3]['count'], border=True)

recruiter_counts.columns = ['Recruiter Name', 'Candidates Count']

fig_recruiters = px.bar(
    recruiter_counts, 
    x='Recruiter Name', 
    y='Candidates Count', 
    title='عدد المرشحين لكل ريكروتر',
    text_auto=True,
    color='Candidates Count',
    color_continuous_scale='Blues'
)
st.plotly_chart(fig_recruiters)
# fig_recruiters.show()

st.divider()
interview_states = df['Interview State'].value_counts().reset_index()
interview_states.columns = ['Interview State', 'Count']

fig_interview_state = px.pie(
    interview_states, 
    names='Interview State', 
    values='Count', 
    hole=0.4, 
    title='توزيع حالات المقابلات (Interview States)'
)
fig_interview_state.update_traces(textposition='inside', textinfo='percent+label')
# fig_interview_state.show()
st.plotly_chart(fig_interview_state)

st.divider()

company_counts = df['Company'].value_counts().reset_index()
company_counts.columns = ['Company', 'Count']

fig_companies = px.bar(
    company_counts, 
    x='Count', 
    y='Company', 
    orientation='h', 
    title='عدد المرشحين لكل شركة',
    text_auto=True,
    color='Count',
    color_continuous_scale='Teal'
)
fig_companies.update_layout(yaxis={'categoryorder':'total ascending'})
# fig_companies.show()
st.plotly_chart(fig_companies)