import streamlit as st

a,b,c =st.columns(3)
with a:
    st.subheader("*General Information*  [ℹ️]")
    with st.expander("What is this project ? "):
        st.write("this is a demo project how a recommendation engine works.")
    with st.expander("why should I register on this ?"):
        st.write("Actually making an account on this, helps me alot to improve my model as if now I don't have any kind of user data to work on for collabrotive model")    
    with st.expander("Site Preferences"):
        st.write("Tips & Tricks - From advance search tricks, to making lists, or leaving ratings and reviews, we’ll help you get the most out of this.")
with b:
    st.subheader("*Discover & Contribute* [👁️]")
    with st.expander("How can I search a movie or TV show ?"):
        st.write("1.You can create an account and later after logging inot your account you can search")
        st.write("2.Currently I am still working on signup & signin pages so you can \'Next\' provided ")
    with st.expander("Why my model is little boring ?"):
        st.write("Here, this is a small demo with is basically working on textual data of about 5K movies & I think user contribution will be a great milestone.")
    with st.expander("What is purpose of providing glossary ?"):
        st.write("In this glossary page I am providing the info which you use as search arguments. ")
with c:
    st.subheader("*Commom Issues*[🛠️]")
    with st.expander("Why this model is not able to provide good movies ?"):
        st.write("As I mentioned before this is demo. It is still in developmental stages")
    with st.expander("MODEL login/registration issues"):
        st.write("This may a take while to sort the issues of the login pages.Thankyou for your patience")
    with st.expander("How can I go through to different pages ?"):
        st.write("As this is still in developmental stage, hardly this provide some good features like many websites."
                 "For now you can use the basic buttons provided.")
    
st.divider()
with st.container(border =True):
    st.header("Need more help ?")
    st.subheader("You can mail to the Developer using this: ")
    st.write("hsmash0008@gmail.com")