import streamlit as st

# Set page config
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🚀",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        max-width: 800px;
        padding: 2rem;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Main content
st.title("Welcome to My Web App!")
st.write("This is a simple web application built with Streamlit.")

# Add some interactive elements
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! 👋")

# Add a button
if st.button("Click me!"):
    st.balloons()
    st.success("You clicked the button! 🎉")

# Add some sample content
st.markdown("""
## About This App
This is a simple web application that demonstrates how to create and deploy a web app using Streamlit.

### Features:
- Interactive elements
- Custom styling
- Easy deployment to Streamlit Cloud
""")

# Add a sidebar
with st.sidebar:
    st.header("Navigation")
    st.write("Use the options below to navigate the app.")
    
    page = st.radio(
        "Go to",
        ["Home", "About", "Contact"]
    )
    
    if page == "About":
        st.info("This is the about page.")
    elif page == "Contact":
        st.info("Contact us at: example@email.com")
