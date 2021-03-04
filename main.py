"""Main module for the streamlit app"""
import streamlit as st
import awesome_streamlit as ast


import src.pages.eda
import src.pages.cluster

from variables.media import CAPTAIN_LOGO
from variables.strings import PAGE_EDA
from variables.strings import PAGE_CLUSTER
from variables.strings import MAIN_TITLE
from variables.strings import SIDE_BAR_INFO


PAGES = {
    PAGE_EDA: src.pages.eda,
    PAGE_CLUSTER: src.pages.cluster,
}


def main():
    """Main function of the App"""
    st.set_page_config(
        page_title=MAIN_TITLE,
        page_icon=CAPTAIN_LOGO,
        layout="centered",  # wide takes all page width
        initial_sidebar_state="expanded",
    )
    st.sidebar.title(MAIN_TITLE)
    st.sidebar.image(CAPTAIN_LOGO, use_column_width=True)
    selection = st.sidebar.radio(label="App visualization mode", options=['learning', 'pro'], index=0)
    st.learning_mode = True if selection == 'learning' else False
    selection = st.sidebar.radio(label="", options=list(PAGES.keys()), index=0)
    # sidebar
    if st.learning_mode:
        st.sidebar.title("Data sources")
        st.sidebar.info(SIDE_BAR_INFO)

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)


if __name__ == "__main__":
    main()
