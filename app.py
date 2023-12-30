import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

def get_paper_text(paper_docs):
    text = ""
    for paper in paper_docs:
        paper_reader = PdfReader(paper)
        for page in paper_reader.pages:
            text += page.extract_text()
    return text

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
                raw_text=get_paper_text(paper_docs)


if __name__=='__main__':
    main()