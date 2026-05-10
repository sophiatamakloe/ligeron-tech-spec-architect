import streamlit as st

st.title("Ligeron AI Spec Architect")

st.subheader("AI-Powered Product Specification Generator")

user_input = st.text_area(
    "Describe your startup idea or feature:"
)

if st.button("Generate Spec"):
    st.write("Generating product specification...")

    st.success("Specification generated successfully!")

    st.write(f"""
    ## Product Spec Draft

    Feature Idea:
    {user_input}

    Suggested MVP:
    - User authentication
    - Dashboard
    - AI workflow integration
    - Analytics tracking

    Business Value:
    Helps startups 
