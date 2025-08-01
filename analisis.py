import streamlit as st 
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def tampilkan_analisis():
    tab1, tab2, tab3, tab4 = st.tabs(["Business Understanding", "Data Understanding", "Data Preparation", "Analysis & Insight"])

    with tab1:
        st.header("Business Understanding")
        st.image("https://comparic.pl/wp-content/uploads/2024/01/freepik-ETH-Ethereum-3.jpg", width=700)
        with st.expander("Background"):
            st.write("""
                    Pasar aset kripto seperti Ethereum (ETH) merupakan salah satu pasar aset yang memiliki volatilitas harga yang sangat tinggi. 
                     Fluktuasi harga yang cepat membuat para trader dan investor menghadapi tantangan besar dalam membuat keputusan investasi yang tepat waktu dan menguntungkan. 
                     Oleh karena itu, diperlukan alat bantu berbasis data yang mampu memprediksi pergerakan harga di masa depan secara akurat.
                     Dengan bantuan machine learning atau model statistik, prediksi jangka pendek dapat dilakukan untuk membantu pengambilan keputusan dalam aktivitas trading atau manajemen risiko.
                     """)
        with st.expander("Problem"):
            st.write("""
                    Dengan volatilitas harga yang tinggi, apakah ada model prediksi yang dapat memprediksi harga Ethereum dengan akurasi yang tinggi?
                    """)
        with st.expander("Objective"):
            st.write("""
                    1. Mengembangkan model prediksi harga Ethereum (ETH) berbasis time series forecasting.
                    2. Model ini akan memanfaatkan data historis harga Ethereum setiap 15 menit (interval 15m).   
                     """)
        with st.expander("Goals"):
            st.write("""
                    1. Memprediksi harga Ethereum dengan model prediksi
                    2. Memberikan rekomendasi actionable terhadap fluktuasi harga seperti kapan saatnya beli atau jual Ethereum.
                     """)

    with tab2:
        st.header("Data Understanding")
        st.image("https://www.texastaxcredit.com/wp-content/uploads/2025/06/115282614.jpg", width=700)
        data = pd.read_csv("ETH_15min_2017_to_2025-07-25 new.csv")
        st.write(data)

        with st.expander("Data Dictionary"):
            st.write('''
                    1. `datetime` : Tanggal dan waktu harga Ethereum
                    2. `open`:  Harga awal dalam periode 15 menit
                    3. `high`:  Harga Tertinggi dalam periode 15 menit
                    4. `low`: Harga terendah dalam periode 15 menit
                    5. `close` :  Harga penutupan
                    6. `volume` :  Jumlah total transaksi Ethereum dalam periode 15 menit
                    ''')
            
        with st.expander("Data Understanding"):
            st.write("""
                    1. Data berisi 6 kolom dan 277.966 baris. 
                    2. Variabel utama yang menjadi analisis dan acuan pada model prediksi adalah close (harga penutupan)
                    3. Periode waktu dalam dataset dari 17-08-2017 s/d 27-07-2025
                     """)

    with tab3:
        st.header("Data Preparation")
        st.image("https://www.newsbtc.com/wp-content/uploads/2023/09/Ethereum.jpeg?fit=1920%2C1080", width=700)
        st.write("""
                1. Dataset tidak memiliki nilai NULL dan tidak adanya missing value 
                2. Data yang menjadi fokus yaitu close
                3. Tidak ada data duplikat
                4. Tipe data fitur datetime dirubah dari object ke datetime
                 """)
    
    with tab4:
        st.header("Exploratory Data Analysis")

        with st.expander("Fundamental Introduction"):
            st.subheader('Bitcoin as The Cryptocurrency Fundamental')
            st.write("Grafik berikut menunjukkan siklus pergerakan harga Bitcoin.")
            st.image('https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgviKfQt36kh8UhY5J84FEZ_wj7T4OKaUgmDzFaRealaaa6ykWdaXNmkjFzm43SYx4XamKdLK3Ll5R-ckn-V1_0n5lhlxjPMb8mjF7_P3bqMfAF0kRQJ7gqrRoo4_B9YlfaK-FbyDieNZ4mXPiqsxjv0o2yMQ_63aZ3k0vhBg-lFYXi47Wl6cD3KXwfPsM/w0/siklus%204%20tahunan.png')
            st.write('''
                    Secara umum pasar aset crypto berpusat pada Bitcoin (BTC) dan aset crypto lainnya seperti Ethereum, mengikuti Bitcoin. Lalu Bitcoin memliki siklus 4 tahunan seperti pada gambar.
                     Dalam gambar, dapat diketahui bahwa Bitcóin mengalami siklus 4 tahunan selama 3 kali dari tahun 2012 - 2022. Selama siklus ini juga aset crypto lainnya cenderung mengikuti oola pergerakan harga dari Bitcoin ini.
                    ''')
        
        with st.expander("Ethereum vs Bitcoin"):
            st.subheader('Correlation Bitcoin & Ethereum Price')
            st.write("Grafik berikut menunjukkan perbandingan pergerakan harga Bitcoin dan Ethereum.")
            st.image('https://www.tradingview.com/x/xhIZjg3p/')
            st.write('''
                 Seperti pada gambar, Ethereum memiliki pola pergerakan harga sangat mirip dengan Bitcoin khususnya dalam konteks dataset ini dari 2017 - 2025. Sehingga dapat dikatakan bahwa Ethereum dan BItcoin ini memiliki korelasi linear, positif dan kuat.
                Jadi Ethereum juga dipengaruhi oleh siklus 4 tahunan dari Bitcoin dans sehingga memiliki pola pergerakan harga yang cenderung sama dengan BItcoin.
                    ''')
            
        with st.expander("Ethereum Highest vs Lowest Price"):
            st.subheader('Ethereum All Time High Price & Lowest Price')
            st.write("Grafik berikut menunjukkan harga tertinggi dan terendah Ethereum.")
            df = pd.read_csv('ETH_15min_2017_to_2025-07-25 new.csv')
            df['datetime'] = pd.to_datetime(df['datetime'])
            df = df.set_index('datetime')

            # Ambil harga penutupan
            close = df['close']

            # Mencari tanggal dan nilai harga tertinggi dan terendah global
            max_price = close.max()
            max_price_date = close.idxmax()

            min_price = close.min()
            min_price_date = close.idxmin()

            # Streamlit Header
            st.subheader('Tren Harga Penutupan ETH (Makro)')
            st.write("Grafik berikut menunjukkan harga tertinggi dan terendah sepanjang periode data yang tersedia.")

            # Visualisasi matplotlib ke Streamlit
            fig, ax = plt.subplots(figsize=(16,8), dpi=200)
            ax.plot(close.index, close.values, label='Harga Penutupan ETH', color='black', linewidth=1)

            # Tambahkan tanda lingkaran pada titik tertinggi dan terendah
            ax.scatter(max_price_date, max_price, color='red', s=100, edgecolors='black',
           label=f'Tertinggi: {max_price:.2f} USDT\n({max_price_date.date()})', zorder=5)
            ax.scatter(min_price_date, min_price, color='blue', s=100, edgecolors='black',
           label=f'Terendah: {min_price:.2f} USDT\n({min_price_date.date()})', zorder=5)

            # Tambahkan label dan format
            ax.set_title('Harga Penutupan ETH dengan Tanda Harga Tertinggi dan Terendah', fontsize=14)
            ax.set_xlabel('Tanggal', fontsize=14)
            ax.set_ylabel('Harga Penutupan (USDT)', fontsize=14)
            ax.tick_params(axis='x', labelsize=12)
            ax.tick_params(axis='y', labelsize=12)
            ax.legend(fontsize=12)
            ax.grid(True)

            # Tampilkan grafik di Streamlit
            st.pyplot(fig)

            # Tampilkan info analisis dalam bentuk tabel
            st.markdown("Informasi Ringkasan Harga")
            st.table({
                "Tanggal Harga Tertinggi": [max_price_date.strftime('%Y-%m-%d')],
                "Harga Tertinggi (USDT)": [f"{max_price:.2f}"],
                "Tanggal Harga Terendah": [min_price_date.strftime('%Y-%m-%d')],
                "Harga Terendah (USDT)": [f"{min_price:.2f}"]
            })
            st.write('''
                Seperti pada gambar, Ethereum memiliki harga yang tertinggi 4846.85 USD pada tanggal 10 November 2021.
                     Dan memiliki harga terendah 82.17 USD pada tanggal 15 Desember 2018.
                    ''')
            
        with st.expander("Bitcoin vs Ethereum Lowest & Highest"):
            st.subheader('Correlation Bitcoin vs Ethereum All Time High Price & Lowest Price')
            st.write("Grafik berikut menunjukkan perbandingan harga tertinggi dan terendah Bitcoin & Ethereum.")
            st.image('https://www.tradingview.com/x/UomV2zu3/')
            st.write('''
                   Bisa dilihat juga dari chart ini bahwa harga tertinggi dan terendah dari  Ethereum yang sama dengan Bitcoin.
                     Disarankan analisis pergerakan harga Ethereum  memerhatikan pergerakan harga Bitcóin juga, karena memilik korelasi berdasarkan data hitstoris.
                    ''')

        with st.expander("Ethereum Moving Average"):
            st.subheader('Ethereum Price by Moving Average 7 & 30')
            st.write("Grafik berikut menunjukkan pergerakan harga Ethereum berdasarkan MA 7 & 30.")
            

            # Resample harian (mean atau last tergantung preferensi)
            df_daily = df['close'].resample('1D').mean().to_frame()
            df_daily.columns = ['close']

            # Fitur tambahan
            df_fe = df_daily.copy()
            df_fe['lag_1'] = df_fe['close'].shift(1)
            df_fe['lag_2'] = df_fe['close'].shift(2)
            df_fe['ma_7'] = df_fe['close'].rolling(window=7).mean()
            df_fe['ma_30'] = df_fe['close'].rolling(window=30).mean()
            df_fe['day_of_week'] = df_fe.index.dayofweek

            # Tampilkan beberapa data awal
            with st.expander("Lihat Data Awal"):
                st.dataframe(df_fe)
            
            # Plot harga dan moving average
            fig, ax = plt.subplots(figsize=(16, 9), dpi=200)
            ax.plot(df_fe.index, df_fe['close'], label='Harga Penutupan', linewidth=1.2)
            ax.plot(df_fe.index, df_fe['ma_7'], label='MA 7 Hari', linestyle='--')
            ax.plot(df_fe.index, df_fe['ma_30'], label='MA 30 Hari', linestyle='--')

            ax.set_title("Harga ETHUSDT dan Moving Average", fontsize=14)
            ax.set_xlabel("Tahun", fontsize=14)
            ax.set_ylabel("Harga (USDT)", fontsize=14)
            ax.legend(fontsize=12)
            ax.tick_params(axis='x', labelsize=12)
            ax.tick_params(axis='y', labelsize=12)
            ax.grid(True)
            st.pyplot(fig)
            st.image('chart MA 7 & 30.png')
            st.write('''
                   Dilihat dari chart disamping, Ethereum memiliki pola pergerakan harga yang dapat dibaca berdasarkan Moving Average nya.
                     Jika harga naik melewati moving average 7 & 30 maka harga akan cenderung naik untuk beberapa minggu.
                     Sebaliknya jika harga turun melewati moving average 7 & 30 maka harga akan cenderung turun untuk beberapa minggu kedepan.
                     Disarankan dalam analisis harga Ethereum  memerhatikan MA 7 dan 30. 
                    ''')

