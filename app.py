from embedchain import App
from embedchain.config import AppConfig, AddConfig, ChunkerConfig, LlmConfig
import streamlit as st
from string import Template

# Defining the app function
def main():

    st.title("Chat Bot")

    # Configurations for Embedchain App
    app_config = AppConfig(log_level="DEBUG")
    chat_bot = App(config=app_config)

    # Custom Chunker Configuration
    chunker_config = ChunkerConfig(chunk_size=300)  # Assuming text data type
    add_config = AddConfig(chunker=chunker_config)

    # File Upload for Resources
    uploaded_file = st.file_uploader("Choose a file to upload", type=["txt", "pdf", "docx", "mp4"])
    
    if uploaded_file is not None:
        # Adding uploaded file with configurations
        chat_bot.add(uploaded_file, config=add_config)
        st.success("File uploaded successfully!")

    # Custom Query Configuration
    custom_query_template = Template(
        """
            Use the following information to respond to the human's query.
            Context: $context

            Keep the response brief. If you don't know the answer, just say that you don't know, don't try to make up an answer.

            Human: $query
            Response:"""
    )
    llm_config = LlmConfig(template=custom_query_template, number_documents=5)

    # Getting user input
    user_query = st.text_input("Ask a question:")

    # Querying the Embedchain App
    if user_query:
        answer = chat_bot.query(user_query, config=llm_config)
        st.write(f"Answer: {answer}")

# Running the main function
if __name__ == "__main__":
    main()
