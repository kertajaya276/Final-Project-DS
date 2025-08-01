import streamlit as st
st.set_page_config(page_title="Portfolio",
                   layout="wide", page_icon=":rocket:")
st.title("Ethereum Price Prediction")
st.header("Sang Nyoman kertajaya")
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman",
                        ["About Me", "Analysis", "Prediction", "Contact"])

if page == 'Contact':
    import kontak
    kontak.tampilkan_kontak()
elif page == 'About Me':
    import tentang
    tentang.tampilkan_tentang()
elif page == 'Analysis':
    import analisis
    analisis.tampilkan_analisis()
elif page == 'Prediction':
    import prediksi
    prediksi.prediksi()