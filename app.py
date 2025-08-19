import streamlit as st  

from main import generate_response

#Title of the app
st.title("Q&A Chatbot With Ollama")


## Select the Ollama model
st.sidebar.title("Settings")
llm=st.sidebar.selectbox("Select Open Source model",["Gemma3","mistral"])

## Adjust response parameter
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=500, value=300)

## MAin interface for user input
st.write("Go ahead and ask any question")
user_input=st.text_input("You:")



if user_input :
    response=generate_response(user_input,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the user input")
