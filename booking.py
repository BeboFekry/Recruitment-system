import streamlit as st
import pandas as pd

st.subheader(':blue[:material/sticky_note_2:] Candidates Booking Table', divider='blue')

if 'df' not in st.session_state:
    with st.spinner("Loading booking table"):
        sheet_id = "102wYZPgUzyRqfxmmy2gWSGqrmEMvzfG-jzurOir4Qro"
        csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
        st.session_state.df = pd.read_csv(csv_url)


df = st.session_state.df.copy()

# st.dataframe(
#     (
#         st.session_state.df[st.session_state.df['Recruiter Name']!='Abdallah Fekry']
#         .reset_index(drop=True)
#         # .apply(lambda x: f":green[{x[i]}]" for i in x)
#      )
#              )



# def color_states(row):
#   # إنشاء قائمة بنفس طول الصف تحمل القيم الافتراضية (بدون تنسيق)
#   styles = [''] * len(row)

#   # التأكد من أسماء الأعمدة بدقة (عدل الأسماء حسب اللي عندك في الـ DataFrame)
#   # لو الشرط متحقق في الـ interview state
#   if row.get('Interview State') == 'Accepted':
#     # نفترض إننا عايزين نلون عمود الـ interview state بس (أو الصف كله، حسب رغبتك)
#     idx = row.index.get_loc('Interview State')
#     styles[idx] = 'color: green; font-weight: bold;'

#   # لو الشرط متحقق في الـ vn state
#   if row.get('VN State') == 'Accepted':
#     idx = row.index.get_loc('VN State')
#     styles[idx] = 'color: goldenrod; font-weight: bold;'

#   return styles
# import pandas as pd


def color_entire_row(row):
  # القيمة الافتراضية (بدون تنسيق لكل أعمدة الصف)
  styles = [''] * len(row)

  # لو الـ interview state بيساوي accepted، لون الصف كله بالأخضر
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

# تطبيق الـ Styler على الـ DataFrame بالكامل (axis=1 تعني التطبيق على مستوى الصفوف)
styled_df = df[df['Recruiter Name']!='Abdallah Fekry'].reset_index(drop=True).style.apply(color_entire_row, axis=1)

# لعرضها لو شغال في Jupyter Notebook:
# styled_df     

# تطبيق الدالة على الـ DataFrame وإظهار النتيجة (في Jupyter Notebook مثلاً)
# styled_df = df.style.apply(color_states, axis=1)

st.dataframe(styled_df)

st.divider()
st.markdown("#### :blue[:material/schedule:] Next Interviews")
st.dataframe(df[df['State']=='interview'][['Candidate Name', 'Company', 'Last 4 Phone numbers','Interview Date', 'Day', 'Hour','Recruiter Name']].reset_index(drop=True))
# st.table(
#    (
#       df.loc[df['Interview Date'].dropna()
#              .index][['Recruiter Name', 'Company', 'Last 4 Phone numbers','Interview Date', 'Day', 'Hour']]
             
#       )
#    )