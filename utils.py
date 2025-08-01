import pandas as pd

def load_and_preprocess_data(path):
    df = pd.read_csv(path, parse_dates=['datetime'])
    df.set_index('datetime', inplace=True)
    df = df[['close']]
    
    # Resample ke harian dengan harga penutupan terakhir
    df_daily = df.resample('1D').last().dropna()
    
    return df_daily
