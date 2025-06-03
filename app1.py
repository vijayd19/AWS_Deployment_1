import streamlit as st

st.title("🔐 Streamlit Secrets Test")

# Try to access the OpenAI API key from secrets
try:
    openai_key = st.secrets["OPENAI_API_KEY"]
    st.success("✅ OpenAI API key found in secrets!")
    st.write("First 5 characters of key:", openai_key[:5] + "..." + openai_key[-4:])
    st.write("Available secrets:", list(st.secrets.keys()))
except KeyError:
    st.error("❌ OPENAI_API_KEY not found in Streamlit secrets.")
    st.info("Make sure you've added it to .streamlit/secrets.toml locally or in the Streamlit Cloud 'Secrets' tab.")
