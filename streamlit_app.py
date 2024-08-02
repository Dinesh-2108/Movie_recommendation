import streamlit as st

about = st.Page("pages/about.py",title="About",icon="🏠")
user = st.Page("pages/account.py", title="Account", icon=":material/add_circle:",default=True)
help = st.Page("pages/help.py", title="Help", icon="⚙️")
glossary = st.Page("pages/glossary.py",title ="Glossary",icon="📂")
pg = st.navigation([about,user, help,glossary])
# st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
st.set_page_config(page_title="Recommendation engine",page_icon=":movie_camera")

pg.run()