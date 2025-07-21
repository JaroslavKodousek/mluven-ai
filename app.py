import streamlit as st

st.header("Welcome to the Mluven AI App")
st.write("This is a simple Streamlit application to demonstrate the Mluven AI capabilities.")
api_key_inserted = False

with st.sidebar:
    st.subheader("API keys")
    st.write("Insert your Groq API key.")
    if st.text_input("Groq API Key", type="password"):
        st.success("API Key set successfully!")
        api_key_inserted = True

if api_key_inserted:
    st.write("You can now use the Mluven AI features.")
