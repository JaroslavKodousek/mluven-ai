import streamlit as st
import os
from dotenv import load_dotenv
from src.mluvenai.utils.app2 import st_app, st_connecting

st.header("Welcome to the Mluven AI App")
st.write(
    "This is a simple Streamlit application to demonstrate the Mluven AI capabilities."
)
api_key_inserted = False

if "play_app" not in st.session_state:
    st.session_state.play_app = False

with st.sidebar:
    st.subheader("API keys")
    load_dotenv()
    open_ai_apikey = os.getenv("OPENAI_API_KEY", "")
    if open_ai_apikey:
        st.success("OpenAI API Key is set.")
        api_key_inserted = True
    else:
        st.write("Insert your OpenAI API key.")
        if st.text_input("Groq API Key", type="password"):
            st.success("API Key set successfully!")
            api_key_inserted = True

if api_key_inserted:
    play_app = False
    st_connecting()
    cefr_level = st.radio(
        "Select your CEFR level:",
        options=[
            "A1 (Absolute Beginner)",
            "A2 (Beginner)",
            "B1 (Intermediate)",
            "B2 (Upper Intermediate)",
            "C1 (Advanced)",
            "C2 (Proficient)",
        ],
        index=2,
        help="Select your language proficiency level.",
    )

    language_to_practice = st.selectbox(
        "Select a language to practice:",
        options=["English", "German", "Spanish", "Polish", "Czech", "Italian"],
        index=0,
    )
    if st.button("Start Practicing"):
        st.session_state.play_app = True

    if st.session_state.play_app:
        st.write(
            f"You are practicing {language_to_practice} at the {cefr_level} level."
        )
        st.write(
            "You can now start practicing your language skills with Mluven AI."
        )
        st_app()