import streamlit as st
from langchain.agents import AgentType
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI


def setup_chat(df, openai_api_key, temp=0):
    if "messages" not in st.session_state or st.sidebar.button(
            "Clear conversation history"):
        # Extract column names from the DataFrame to include in the
        # instructions
        column_names = ", ".join(df.columns)

        basic_instructions = f"""
        You are a data analysis assistant for the current data which includes only the following columns: {column_names}. Help summarize, find specific values, and perform basic statistical operations (such as finding minimum, maximum, outliers, percentiles, comparisons > < <= >= =, range and everything related to hypothesis testing) on these columns. Evaluate any python scripts you generate with all relevant imports and show results in new prompt. While describing data mention both qualitative (1 line about what is) and quantitive details (range,outlier, how many missing or invalid format) of each or specified features. Decline questions not about data analysis of current data or {column_names}"""

        st.session_state["messages"] = [
            {"role": "system", "content": basic_instructions}
        ]

    # Handle user input
    prompt = st.chat_input(placeholder="Ask about the data...")

    if prompt:
        st.session_state["messages"].append(
            {"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()

        llm = ChatOpenAI(
            temperature=temp, model="gpt-3.5-turbo", openai_api_key=openai_api_key, streaming=True
        )

        pandas_df_agent = create_pandas_dataframe_agent(
            llm,
            df,
            verbose=True,
            agent_type=AgentType.OPENAI_FUNCTIONS,
            handle_parsing_errors=True,
        )

        with st.chat_message("assistant"):
            st_cb = StreamlitCallbackHandler(
                st.container(), expand_new_thoughts=True)
            try:
                response = pandas_df_agent.run(
                    st.session_state["messages"], callbacks=[st_cb])
                st.session_state["messages"].append(
                    {"role": "assistant", "content": response})

            except Exception as e:
                st.write("Sorry, an error occurred while processing your request.")
                st.write(str(e))
