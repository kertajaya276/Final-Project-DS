import streamlit as st

def tampilkan_kontak():
    st.title("Contact")
    st.write("Hubungi saya melalui tautan berikut:")

    # LinkedIn
    st.markdown(
        "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/snkertajaya)"
    )

    # GitHub
    st.markdown(
        "[![GitHub](https://img.shields.io/badge/GitHub-Profile-black)](https://github.com/kertajaya276)"
    )
    # Email
    st.write("📧 Email: kertajaya630@gmail.com")