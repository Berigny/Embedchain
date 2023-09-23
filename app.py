# Importing necessary libraries
from embedchain import App
import streamlit as st

# Defining the app function
def main():

    st.title("Naval Chat Bot")

    # Initializing the Embedchain App
    naval_chat_bot = App()

    # Adding online resources
    naval_chat_bot.add("https://www.youtube.com/watch?v=3qHkcs3kG44")
    naval_chat_bot.add("https://navalmanack.s3.amazonaws.com/Eric-Jorgenson_The-Almanack-of-Naval-Ravikant_Final.pdf")
    naval_chat_bot.add("https://nav.al/feedback")
    naval_chat_bot.add("https://nav.al/agi")

    # Adding local resources
    naval_chat_bot.add(("Who is Naval Ravikant?", "Naval Ravikant is an Indian-American entrepreneur and investor."))

    # Getting user input
    user_query = st.text_input("Ask a question:", value="What unique capacity does Naval argue humans possess when it comes to understanding explanations or concepts?")

    # Querying the Embedchain App
    if user_query:
        answer = naval_chat_bot.query(user_query)
        st.write(f"Answer: {answer}")

# Running the main function
if __name__ == "__main__":
    main()
