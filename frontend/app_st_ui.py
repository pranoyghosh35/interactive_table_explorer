import streamlit as st
import codecs

def setup_ui():
    """
    Set up the Streamlit UI components.
    """
    st.title("📊 Come interact with Data!")
    st.sidebar.title("ℹ️ About")
    # Path to the README.html file
    readme_path = "./data/usr_manuals/README.html"

    # Provide a link to open the README.html content in a new window
    st.sidebar.markdown(
        f'<a href="{readme_path}" target="_blank" style="text-decoration: none;"><img src="https://img.icons8.com/color/48/000000/help.png" width="20"/> Help</a>',
        unsafe_allow_html=True
    )
    st.sidebar.info(
        """
        This app allows you to upload a data file with one or more tables, select one at a time and visualize any two features 
        from selected table.
        """
    )

def display_file_uploader(clear_submit):
    """
    Display the file uploader widget.
    """
    uploaded_file = st.file_uploader(
        "Upload a Data file (CSV, Excel)",
        type=['csv', 'xls', 'xlsx', 'xlsm', 'xlsb'],
        on_change=clear_submit,
    )
    return uploaded_file

def display_openai_api_key_input():
    """
    Display the input for the OpenAI API key.
    """
    st.sidebar.info("""
    Please enter your OpenAI API key to chat about the data.
    """)
    return st.sidebar.text_input("OpenAI API Key", type="password")
