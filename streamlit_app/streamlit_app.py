import streamlit as st


# Sidebar navigation
st.sidebar.title("DashBoard")

selected = st.sidebar.selectbox("Go to :",["Home","About Us","Check DeepFake"])

if selected == "Home":
    from home import show as home
    home()

elif selected == "About Us":
    from aboutus import show as about
    about()

elif selected == "Check DeepFake":
    from check_deepfake import show as generate
    generate()
