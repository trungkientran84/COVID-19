import streamlit as st

from pages.utils import texts

def write():
    st.write("## About the project")
    st.write(texts.ABOUT)
