import streamlit as st


st.sidebar.image("logo.jpg")

# Add "About" section to the sidebar
st.sidebar.header("About")

with st.sidebar:
    st.markdown(
        "Welcome to STRIDE GPT, an AI-powered tool designed to help teams produce better threat models for their applications."
    )
    st.markdown(
        "Threat modelling is a key activity in the software development lifecycle, but is often overlooked or poorly executed. STRIDE GPT aims to help teams produce more comprehensive threat models by leveraging the power of Large Language Models (LLMs) to generate a threat list, attack tree and/or mitigating controls for an application based on the details provided."
    )
    st.markdown("Created by [Matt Adams](https://www.linkedin.com/in/matthewrwadams/).")
    # Add "Star on GitHub" link to the sidebar
    st.sidebar.markdown(
        "⭐ Star on GitHub: [![Star on GitHub](https://img.shields.io/github/stars/mrwadams/stride-gpt?style=social)](https://github.com/mrwadams/stride-gpt)"
    )
    st.markdown("""---""")