
import numpy as np
import matplotlib.pyplot as plt
from arch import arch_model
from sklearn.metrics import mean_absolute_error, mean_squared_error
from datetime import timedelta

def predict_with_arch(df_daily, p=1, forecast_days=30):
    data = df_daily['close']
    returns = 100 * data.pct_change().dropna()

    split_idx = int(len(returns) * 0.8)
    train = returns.iloc[:split_idx]
    test = returns.iloc[split_idx:]

    model = arch_model(train, vol='ARCH', p=p)
    res = model.fit(disp='off')

    forecast_test = res.forecast(horizon=len(test), reindex=False)
    volatility_test = forecast_test.variance.values[-1, :] ** 0.5
    test_start_idx = split_idx + 1

    base_test = data.iloc[test_start_idx:test_start_idx + len(volatility_test)].values
    predicted_price = base_test * (1 + volatility_test / 100)
    actual_price = data.iloc[test_start_idx:test_start_idx + len(volatility_test)].values

    # Metrik evaluasi
    mape = np.mean(np.abs((actual_price - predicted_price) / actual_price)) * 100
    mae = mean_absolute_error(actual_price, predicted_price)
    rmse = np.sqrt(mean_squared_error(actual_price, predicted_price))

    # Forecast ke depan
    forecast_future = res.forecast(horizon=forecast_days)
    future_volatility = forecast_future.variance.values[-1, :] ** 0.5
    last_price = data.iloc[-1]
    forecast_price = [last_price * (1 + v / 100) for v in future_volatility]

    split_date = data.index[test_start_idx]

    return actual_price, predicted_price, forecast_price, split_date, mape, mae, rmse

def plot_arch_forecast(df_daily, actual_price, predicted_price, forecast_price, split_date, return_fig=False):
    fig, ax = plt.subplots(figsize=(14, 6))

    train_data = df_daily[df_daily.index < split_date]
    test_data = df_daily[df_daily.index >= split_date][:len(actual_price)]
    forecast_dates = [test_data.index[-1] + timedelta(days=i+1) for i in range(len(forecast_price))]

    ax.plot(train_data.index, train_data['close'], color='green', label='Train Data')
    ax.plot(test_data.index, actual_price, color='blue', label='Test Actual')
    ax.plot(test_data.index, predicted_price, color='orange', label='Predicted (ARCH)')
    ax.plot(forecast_dates, forecast_price, color='red', label='Forecast (Next Days)')
    ax.axvline(x=split_date, color='gray', linestyle='--', label='Train/Test Split')

    ax.set_title('ARCH Model — Train, Test, Prediction & Forecast')
    ax.set_xlabel('Date')
    ax.set_ylabel('ETH Price')
    ax.legend()
    ax.grid(True)
    plt.tight_layout()

    return fig if return_fig else plt.show()