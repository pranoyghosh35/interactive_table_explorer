import streamlit as st
from frontend.app_st_ui import (
    setup_ui, 
    display_file_uploader, 
    display_openai_api_key_input,
)
from backend.doc_load import load_data
from backend.chat import setup_chat
from backend.util import display_dataframe, plotly_dataframe

def clear_submit():
    """
    Clear the Submit Button State
    """
    st.session_state["submit"] = False

@st.cache_data(ttl="2h")
def cached_load_data(file):
    return load_data(file)

# Setup the page
setup_ui()

# File uploader
uploaded_file = display_file_uploader(clear_submit)

if uploaded_file:
    try:
        tmp_name_df = cached_load_data(uploaded_file)
        if not tmp_name_df:
            st.error("Failed to load data. Please check the file and try again.")
            st.stop()

        sheet_names = list(tmp_name_df.keys())

        if len(sheet_names) > 1:
            selected_name = st.selectbox("Select a sheet or table", sheet_names)
        else:
            selected_name = sheet_names[0]

        df = tmp_name_df[selected_name]

        # Display selected DataFrame info
        st.write(f"Selected {selected_name} with {df.shape[0]} rows and {df.shape[1]} columns.")
        st.write("Columns:")
        st.markdown(f"<div style='color:green'>{', '.join(df.columns)}</div>", unsafe_allow_html=True)

        # User input for display options
        display_option = st.radio("Choose display option", ("Head and Tail", "Random Sample"))
        n_rows = len(df)

        if display_option == "Random Sample":
            n_random_sample = st.number_input("Number of random samples to display", min_value=1, max_value=n_rows, value=5)
            display_dataframe(df, n_random_sample=n_random_sample)
        else:
            n_head = st.number_input("Number of rows to display from the head", min_value=1, max_value=n_rows//2, value=5)
            n_tail = st.number_input("Number of rows to display from the tail", min_value=1, max_value=n_rows//2, value=5)
            display_dataframe(df, n_head=n_head, n_tail=n_tail)

        # Create two tabs
        tabs = st.tabs(["Funplots", "Let's chat"])

        with tabs[0]:
            st.header("Scatter plots are fun!")

            # User inputs for plotly_dataframe parameters
            x_axis = st.selectbox("Select x-axis", df.columns)
            y_axis = st.selectbox("Select y-axis", df.columns)
            target_class = st.selectbox("Select target class (optional)", [None] + list(df.columns))

            # Plot parameters
            legend = st.checkbox("Show legend", value=True)
            colormap = st.selectbox("Select colormap", ['Viridis', 'Cividis', 'Plasma', 'Inferno', 'Magma'])
            marker = st.selectbox("Select marker", ['circle', 'x', 'cross', 'triangle-up', 'triangle-down'])
            marker_size = st.slider("Marker size", min_value=1, max_value=10, value=2)
            x_lim = st.slider("X-axis limit", float(df[x_axis].min()), float(df[x_axis].max()), (float(df[x_axis].min()), float(df[x_axis].max())))
            y_lim = st.slider("Y-axis limit", float(df[y_axis].min()), float(df[y_axis].max()), (float(df[y_axis].min()), float(df[y_axis].max())))

            # Plot the figure
            fig = plotly_dataframe(
                df, x_axis, y_axis, legend=legend, colormap=colormap,
                marker=marker, marker_size=marker_size, x_lim=x_lim, y_lim=y_lim, target_class=target_class
            )
            st.plotly_chart(fig)

        with tabs[1]:
            st.header("Reason about data!")
            st.markdown("""<div style="font-size:24px; font-weight:bold;">powered by OPENAI's 🤖 gpt-3.5-turbo</div>""",
            unsafe_allow_html=True
            )
            st.text("""You should be able to summarize, find specific values,and perform basic statistical operations
            about a feature or group of features (column or columns) in the table.""")
            try:
                # OpenAI API Key input
                openai_api_key = display_openai_api_key_input()
                #Get temperature parameter from user
                temp=st.slider("Temperature", min_value=0.0, max_value=0.5, value=0.0)
                # Setup chat interaction
                setup_chat(df, openai_api_key,temp)
            except ValueError as e:
                st.error(e)
                st.stop()

    except ValueError as e:
        st.error(e)
        st.stop()
