import streamlit as st

import pages.seir
import pages.about

PAGES = {
    "Epidemiological model": pages.seir,
    "About the project": pages.about,
}


def main(): 
    st.markdown(pages.utils.texts.INTRODUCTION)
    
    st.sidebar.markdown("# Navigation")
    goto = st.sidebar.radio("Go to", list(PAGES.keys()))
    PAGES[goto].write()

if __name__=="__main__":
    main()