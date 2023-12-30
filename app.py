import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import  CharacterTextSplitter
def get_paper_text(paper_docs):
    text = ""
    for paper in paper_docs:
        paper_reader = PdfReader(paper)
        for page in paper_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator='\n',
        chunk_size=1000,
        chunk_overlap=100,#Avoid losing the meaning of the chunk
        length_function=len
    )
    chunks = text_splitter.split_text(raw_text)
    return chunks


def main():
    load_dotenv()
    st.set_page_config(page_title="Safe State Synthsesis",page_icon=":books:")
    st.header("Create Your own DFA")
    st.text_input("Shoot Your Question")
    with st.sidebar:
        st.subheader("Add The Paper")
        paper_docs=st.file_uploader("Upload your Paper Here and Click submit",accept_multiple_files=True)
        if st.button("Submit"):
            with st.spinner("Vectorising"):
                #Get the paper
                raw_text = get_paper_text(paper_docs)
                # st.write(raw_text)
                #chunking the text
                text_chunks = get_text_chunks(raw_text)

if __name__=='__main__':
    main()