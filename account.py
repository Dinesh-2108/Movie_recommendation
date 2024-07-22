import streamlit as st
import pandas as pd
import base64
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

if st.query_params:
    st.session_state["title"] = st.query_params.get("title","")
    st.session_state["people"] = st.query_params.get("people","")
    st.session_state["genre"] = st.query_params.get("genre","")
    st.session_state['current_page'] = 'search'

if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'main'


def _mainpage():
    # Streamlit app
    container = st.container(border=True)
    
    with container:
        st.title(":rainbow[ Movie recommendation] :movie_camera:")
        st.subheader("***Make an account to explore***")
            
    def signup():
        st.session_state['current_page'] = 'signup'
    def signin():
        st.session_state['current_page'] = 'signin'
    def search():
        st.session_state['current_page'] = 'search'
        
    a,b,c, =st.columns(3)
    with a:
        sign_up = st.button("Sign Up",on_click=signup)   
    with b:
        sign_in = st.button("Sign In",on_click=signin)
    with c:
        on = st.button("NEXT  > ",on_click=search)
    
    st.divider()
    col1,col2,col3 =st.columns(3)
    
    with col1:
        st.image("hulk.jpg",caption="⭐6.5/10",use_column_width=True)
        st.image("tmnt.jpg",caption="⭐7.1/10",use_column_width=True)
    with col2:
        st.image("avatar.jpg",caption="⭐8.8/10",use_column_width=True)
    with col3:
        st.image("interstellar.jpg",caption="⭐9/10",use_column_width=True)
        st.image("minions.jpg",caption="⭐7.5/10",use_column_width=True)
    st.divider()
    st.subheader("*Thank you visit again*")
    

# Extracting the data
if 'data_not_loaded':
    st.session_state['movie_data_base'] = pd.read_csv("mdb.csv")
# mdb = pd.read_csv("mdb.csv")
    st.session_state['data_not_loaded'] = True
mdb = st.session_state['movie_data_base']

def signup_page():
    st.subheader("Currently this is in developmental stage. You can ignore this & go forword. Thank you for your patience")
    st.divider()
    def search():
        st.session_state['current_page'] = 'search'
    def signin():
        st.session_state['current_page'] = 'signin'
    a,b,c= st.columns(3)
    with b:
        mail = st.text_input("Gmail")
        username = st.text_input("User name")
        passcode = st.text_input("Set up password")
        confirm = st.text_input("Confirm your password")
        # if confirm and (passcode == confirm):
        #             on = st.button("Next > ",on_click=signin)
    st.divider()
    on = st.button("Next > ",on_click=search)
    
def signin_page():
    st.subheader("Currently this is in developmental stage. You can ignore this & go forword. Thank you for your patience")
    st.divider()
    def search():
        st.session_state['current_page'] = 'search'
    def search():
        st.session_state['current_page'] = 'search'
    a,b,c, =st.columns(3)
    with b:
        st.write("LOGIN","↓")
        name = st.text_input("User name")
        password = st.text_input("Password")
        # if password :
        #     on = st.button("NEXT  > ",on_click=search)
    st.divider()
    on = st.button("Next > ",on_click=search)
                
def search_page():
    # User input
    def gotomain():
        st.session_state['current_page'] = 'main'
    st.write("***For more ideas you can use glossary page***")
    a,b,c =st.tabs(["title","genre","people"])
    with a:
        
        
        title_input = st.text_input("***You can search here base on title***",key="title")
        
        # Function to display a loading GIF
        def display_loading_gif():
            gif_path = r"static/bean.gif"
            with open(gif_path, "rb") as gif_file:
                gif_base64 = base64.b64encode(gif_file.read()).decode("utf-8")

            html_code = f"""
            <div style="text-align: center;" id="loading">
                <img src="data:image/gif;base64,{gif_base64}" alt="loading">
            </div>
            """
            return html_code
        if title_input:
        # Display the loading GIF
            container = st.container()

            with container:
                loading_html = display_loading_gif()
                gif_placeholder = st.markdown(loading_html, unsafe_allow_html=True)

            tfidf = TfidfVectorizer(stop_words="english")
            columns = ['title', 'genres', 'keywords', 'overview', 'cast', 'crew', 'revenue', 'vote_average', 'vote_count', 'popularity']
            scores = []

            for column in columns:
                tfidf_matrix = tfidf.fit_transform(mdb[column].apply(lambda x: ' '.join(x) if isinstance(x, list) else str(x))).toarray()

                # Transform user input using TF-IDF vectorizer
                user_tfidf = tfidf.transform([title_input.lower()])

                # Compute cosine similarity between user input and all movies
                cosine_similarities = cosine_similarity(user_tfidf, tfidf_matrix).flatten()
                scores.append(cosine_similarities)

            df = sum(scores)
            sortedIndices = df.argsort()[::-1]

            top_n = 5
            recommendations = mdb.iloc[sortedIndices[:top_n]]
            st.divider()
            st.write(f"Top {top_n} similar movies for: {title_input}")

            films =[]

            # Remove the loading GIF after search is completed
            gif_placeholder.empty()
            container.markdown("")
            # with container:
            #     st.write("Done ! 👍")
            col1,col2 =st.columns(2)
            with col1:
                for index, movie in recommendations.iterrows():
                    films.append(f'{str(movie["title"]).capitalize()}')
                    with st.popover(f'*:blue[{str(movie["title"]).capitalize()}]*'):
                        st.write(f"⭐ {(movie['vote_average'])}/10")
                        with st.expander("Know more 👇🏻"):
                            st.write(f"{(movie['genres']).capitalize()}")
                            st.divider()
                            st.write(f"{(movie['overview'].capitalize())}")
            with col2:
                st.image("man.png",width =500)
            def save_response(title_input,films):
                st.session_state["title: "+ title_input] = {'user_input':title_input,"movies":films}
            save_response(title_input,films)
            st.toast("Search Completed",icon="👍")
    with b:
        genre_input = st.text_input("***You can search here based on genres***",key="genre")
        
        # Function to display a loading GIF
        def display_loading_gif():
            gif_path = r"static/bean.gif"
            with open(gif_path, "rb") as gif_file:
                gif_base64 = base64.b64encode(gif_file.read()).decode("utf-8")

            html_code = f"""
            <div style="text-align: center;" id="loading">
                <img src="data:image/gif;base64,{gif_base64}" alt="loading">
            </div>
            """
            return html_code
        if genre_input:
        # Display the loading GIF
            container = st.container()

            with container:
                loading_html = display_loading_gif()
                gif_placeholder = st.markdown(loading_html, unsafe_allow_html=True)

            tfidf = TfidfVectorizer(stop_words="english")
            columns = [ 'genres']
            scores = []

            for column in columns:
                tfidf_matrix = tfidf.fit_transform(mdb[column].apply(lambda x: ' '.join(x) if isinstance(x, list) else str(x))).toarray()

                # Transform user input using TF-IDF vectorizer
                user_tfidf = tfidf.transform([genre_input.lower()])

                # Compute cosine similarity between user input and all movies
                cosine_similarities = cosine_similarity(user_tfidf, tfidf_matrix).flatten()
                scores.append(cosine_similarities)

            df = sum(scores)
            sortedIndices = df.argsort()[::-1]

            top_n = 5
            recommendations = mdb.iloc[sortedIndices[:top_n]]
            st.divider()
            st.write(f"Top {top_n} similar movies for: {genre_input}")

            films =[]

            # Remove the loading GIF after search is completed
            gif_placeholder.empty()
            container.markdown("")
            # with container:
            #     st.write("Done ! 👍")
            col1,col2 =st.columns(2)
            with col1:
                for index, movie in recommendations.iterrows():
                    films.append(f'{str(movie["title"]).capitalize()}')
                    with st.popover(f'*:blue[{str(movie["title"]).capitalize()}]*'):
                        st.write(f"{(movie['genres']).capitalize()}")
                        with st.expander("Know more 👇🏻"):
                            st.write(f"⭐ {(movie['vote_average'])}/10")
                            st.divider()
                            st.write(f"{(movie['overview'].capitalize())}")
            with col2:
                st.image("man.png",width =500)
            def save_response(genre_input,films):
                st.session_state["genres: "+genre_input] = {'user_input':genre_input,"movies":films}
            save_response(genre_input,films)
            st.toast("Search Completed",icon="👍")
    with c:
        user_input = st.text_input("***You can search here based on people***",key="people")
        # Function to display a loading GIF
        def display_loading_gif():
            gif_path = r"static/bean.gif"
            with open(gif_path, "rb") as gif_file:
                gif_base64 = base64.b64encode(gif_file.read()).decode("utf-8")

            html_code = f"""
            <div style="text-align: center;" id="loading">
                <img src="data:image/gif;base64,{gif_base64}" alt="loading">
            </div>
            """
            return html_code
        if user_input:
        # Display the loading GIF
            container = st.container()

            with container:
                loading_html = display_loading_gif()
                gif_placeholder = st.markdown(loading_html, unsafe_allow_html=True)

            tfidf = TfidfVectorizer(stop_words="english")
            columns = ['cast', 'crew']
            scores = []

            for column in columns:
                tfidf_matrix = tfidf.fit_transform(mdb[column].apply(lambda x: ''.join(x) if isinstance(x, list) else str(x))).toarray()
                
                user = user_input.replace(" ","_")
                # Transform user input using TF-IDF vectorizer
                user_tfidf = tfidf.transform([user.lower()])

                # Compute cosine similarity between user input and all movies
                cosine_similarities = cosine_similarity(user_tfidf, tfidf_matrix).flatten()
                scores.append(cosine_similarities)

            df = sum(scores)
            sortedIndices = df.argsort()[::-1]

            top_n = 5
            recommendations = mdb.iloc[sortedIndices[:top_n]]
            st.divider()
            st.write(f"Top {top_n} similar movies for: {user_input}")

            films =[]

            # Remove the loading GIF after search is completed
            gif_placeholder.empty()
            container.markdown("")
            # with container:
            #     st.write("Done ! 👍")
            col1,col2 =st.columns([3,1])
            with col1:
                for index, movie in recommendations.iterrows():
                    films.append(f'{str(movie["title"]).capitalize()}')
                    with st.popover(f'*:blue[{str(movie["title"]).capitalize()}]*'):
                        st.write(f"⭐ {(movie['vote_average'])}/10")
                        with st.expander("Know more 👇🏻"):
                            # Convert the string to a list
                            actual_list = ast.literal_eval(movie["cast"])
                            # Print each value separately
                            st.subheader("Cast :")
                            for name in actual_list:
                                name= name.replace("_"," ")
                                st.write(name.capitalize())
                            # Convert the string to a list
                            st.divider()
                            actual_list = ast.literal_eval(movie["crew"])
                            # Print each value separately
                            st.subheader("Director:")
                            for name in actual_list:
                                name= name.replace("_"," ")
                                st.write(name.capitalize())
                            st.divider()
                            st.write(f"{(movie['genres'].capitalize())}")
                            st.divider()
                            st.write(f"{(movie['overview'].capitalize())}")
            with col2:
                st.image("man.png",width =500)
            def save_response(user_input,films):
                st.session_state["people: "+user_input] = {'user_input':user_input,"movies":films}
            save_response(user_input,films)
            st.toast("Search Completed",icon="👍")
    st.divider()   
    st.button("go to mainpage",on_click=gotomain)
    # st.divider()
    # st.write(st.session_state)
page_dict = {'main':_mainpage,
             "signup":signup_page,
             "signin":signin_page,
             'search':search_page}
page_dict[st.session_state['current_page']]()

