import streamlit as st

st.title("ABOUT US ")
st.divider()
container = st.container(border=True)
col1,col2 =st.columns([3,1])
with col1:
    st.subheader("Our Mission ")
    st.write("The purpose of designing this is to learn how movie lovers discover their next favorite film."
             "We understand how overwhelming it can be to choose from the vast array of movies available, so we've develop a basic demo of recommendation system to simplify the process for you.")
    st.subheader("How It Works")
    st.write("Our recommendation engine uses simpe NLP algorithms to analyze your movie preferences and viewing history. We provide personalized movie suggestions tailored to your unique tastes.")    
with col2:
    st.image("images/face.png",use_column_width=True)
st.divider()
