import streamlit as st
from llama_index import GPTVectorStoreIndex  # Updated this line
import os
import config

@st.cache_resource
def load_indexes():
    """load the pipeline object for preprocessing and the ml model"""

    # load index files 
    index_document = GPTVectorStoreIndex.load_from_disk('index_txt.json')  # Updated this line
    index_video = GPTVectorStoreIndex.load_from_disk('index_video.json')  # Updated this line
    index_wikipedia = GPTVectorStoreIndex.load_from_disk('index_wikipedia.json')  # Updated this line (and fixed a typo)
    return index_document, index_video, index_wikipedia

def main():

    API_KEY = config.API_KEY
    # api key
    os.environ['OPENAI_API_KEY'] = API_KEY

    # load indices
    index_document, index_video, index_wikepedia = load_indexes()

    st.header('Custom-Made Chatbots')

    # select the data to write queries for
    st.write("Select the data that your chatbot should be trained with:")
    data = st.selectbox('Data', ('.txt file (My favorite fruits)', 'Youtube Video (Vanilla Cake Recipe)', 'Wikipedia Article (Apple)'))

    # use the index based on the seleted data
    if data == '.txt file (My favorite fruits)':
        st.image('fruit.png')
        index = index_document
    elif data == 'Youtube Video (Vanilla Cake Recipe)':
        st.image('cake.png')
        index = index_video
    elif data == 'Wikipedia Article (Apple)':
        st.image('apple.jpeg')
        index = index_wikepedia

    # query the selected index
    query = st.text_input('Enter Your Query')
    button = st.button(f'Response')
    if button:
        st.write(index.query(query))

if __name__ == '__main__':
    main()
