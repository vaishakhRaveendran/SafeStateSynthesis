import streamlit as st
from dotenv import load_dotenv

def main():
    load_dotenv()
    st.set_page_config(page_title="Safe State Synthsesis",page_icon=":books:")
    st.header("Create Your own DFA")
    st.text_input("Shoot Your Question")
    with st.sidebar:
        st.subheader("Add The Paper")
        st.file_uploader("Upload your Paper Here and Click submit")
        st.button("Submit")

if __name__=='__main__':
    main()