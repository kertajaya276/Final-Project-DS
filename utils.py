# import pandas as pd
# from sklearn.metrics import mean_absolute_percentage_error, mean_absolute_error

#     # utils.py
# def load_internal_data():
#     df = pd.read_csv("ETH_15min_2017_to_2025-07-25 new.csv", parse_dates=['datetime'])
#     return df

# def preprocess_data(df, horizon):
#     # Pastikan kolom datetime dalam format datetime
#     df['datetime'] = pd.to_datetime(df['datetime'])

#     # Set kolom datetime sebagai index
#     df.set_index('datetime', inplace=True)

#     # Resample ke data harian (bisa diganti ke frekuensi lain sesuai kebutuhan)
#     df = df['close'].resample('1D').mean().dropna().to_frame()

#     # Buat fitur lag sederhana
#     df['lag_1'] = df['close'].shift(1)
#     df['lag_2'] = df['close'].shift(2)
#     df['lag_3'] = df['close'].shift(3)

#     # Drop NA
#     df = df.dropna()

#     return df

# def evaluate_mape(y_true, y_pred):
#     return mean_absolute_percentage_error(y_true, y_pred) * 100
    

# # utils.py
# import pandas as pd
# from sklearn.metrics import mean_absolute_percentage_error

# def load_internal_data():
#     # Pastikan kolom datetime terdeteksi dengan benar
#     df = pd.read_csv("ETH_15min_2017_to_2025-07-25 new.csv", parse_dates=['datetime'])
#     return df

# def preprocess_data(df, horizon):
#     # Pastikan kolom datetime dalam format datetime
#     df['datetime'] = pd.to_datetime(df['datetime'])

#     # Set kolom datetime sebagai index
#     df.set_index('datetime', inplace=True)

#     # Resample ke data harian (bisa disesuaikan dengan model)
#     df = df['close'].resample('1D').mean().dropna().to_frame()

#     # Buat fitur lag sederhana (tidak dipakai di ARCH, tapi bisa berguna untuk eksplorasi)
#     df['lag_1'] = df['close'].shift(1)
#     df['lag_2'] = df['close'].shift(2)
#     df['lag_3'] = df['close'].shift(3)

#     # Drop NA karena adanya lag
#     df = df.dropna()

#     return df

# def evaluate_mape(y_true, y_pred):
#     return mean_absolute_percentage_error(y_true, y_pred) * 100


import pandas as pd

def load_and_preprocess_data(path):
    df = pd.read_csv(path, parse_dates=['datetime'])
    df.set_index('datetime', inplace=True)
    df = df[['close']]
    
    # Resample ke harian dengan harga penutupan terakhir
    df_daily = df.resample('1D').last().dropna()
    
    return df_daily
