import streamlit as st
import pandas as pd

st.subheader(':blue[:material/sticky_note_2:] Candidates Booking Table', divider='blue')

if 'df' not in st.session_state:
    with st.spinner("Loading booking table"):
        sheet_id = "102wYZPgUzyRqfxmmy2gWSGqrmEMvzfG-jzurOir4Qro"
        csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
        st.session_state.df = pd.read_csv(csv_url)
        st.session_state.df = st.session_state.df.dropna(how='all', axis=1)
df = st.session_state.df.copy()

n = st.text_input('Search with the last 4 phone numbers', max_chars=4, placeholder='Search...', icon=":material/search:")
if n:
  if n.isnumeric() and len(n)==4:
    df = df[df['Last 4 Phone numbers']==int(n)]

with st.popover("Filters"):
  st.markdown('Filters')
  rec = st.selectbox('Recruiter Name',['ALL'] + df['Recruiter Name'].dropna().unique().tolist())
  if rec and rec!='ALL':
    df = df[df['Recruiter Name']==rec]
  state = st.selectbox('State',['ALL'] + df['State'].dropna().unique().tolist())
  if state and state!='ALL':
    df = df[df['State']==state]
  company = st.selectbox('Company',['ALL'] + df['Company'].dropna().unique().tolist())
  if company and company!='ALL':
    df = df[df['Company']==company]


if st.button(':material/remove: Remove filters'):
   df = st.session_state.df.copy()

def color_entire_row(row):
  styles = [''] * len(row)

  if row.get('State') == 'accepted':
    styles = ['color: green; '] * len(row)
  elif row.get('State') == 'pending':
    styles = ['color: goldenrod; '] * len(row)
  elif row.get('State') == 'interview':
      styles = ['color: lightblue; '] * len(row)
  elif row.get('State') == 'rejected':
    styles = ['color: red; '] * len(row)

  return styles


df['Last 4 Phone numbers'] = df['Last 4 Phone numbers'].astype(str)

if st.session_state.user_type=='recruiter':
  styled_df = df[df['Recruiter Name']!='Abdallah Fekry'].reset_index(drop=True).dropna(how='all', axis=1).style.apply(color_entire_row, axis=1)
else:
   styled_df = df.reset_index(drop=True).dropna(how='all', axis=1).style.apply(color_entire_row, axis=1)

st.dataframe(styled_df)

st.divider()
st.markdown("#### :blue[:material/schedule:] Next Interviews")
st.dataframe(df[df['State']=='interview'][['Candidate Name', 'Company', 'Last 4 Phone numbers','Interview Date', 'Day', 'Hour','Recruiter Name']].reset_index(drop=True))
