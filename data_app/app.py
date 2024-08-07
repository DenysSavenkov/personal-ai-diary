import streamlit as st

pg = st.navigation([
    # st.Page("data_app/pages/page_home.py", title="Home"),
    st.Page("data_app/pages/page_article_analyzer.py", title="Article Analyzer"),
])
st.set_page_config(page_title="Academic Expert System", page_icon=":material/science:")
pg.run()