import streamlit as st
from utils import load_and_preprocess_data
from model_arch import predict_with_arch, plot_arch_forecast

def prediksi():
    st.title("📈 Ethereum Price Forecast with ARCH Model")

    # Load data
    data_path = "ETH_15min_2017-08-17_to_2025-07-27 new.csv"
    df_daily = load_and_preprocess_data(data_path)

    # Tampilkan data harga harian
    with st.expander("📊 Show Daily ETH Price"):
        st.line_chart(df_daily)

    # Sidebar input
    st.sidebar.header("🔧 ARCH Model Settings")
    p = st.sidebar.slider("Order p (ARCH)", min_value=1, max_value=5, value=1)
    forecast_days = st.sidebar.slider("Forecast Days", min_value=7, max_value=60, value=30)

    if st.button("🔮 Run ARCH Forecast"):
        with st.spinner("Training ARCH model and forecasting..."):
            actual, predicted, forecast, split_date, mape, mae, rmse = predict_with_arch(
                df_daily, p=p, forecast_days=forecast_days
            )

            fig = plot_arch_forecast(
                df_daily,
                actual_price=actual,
                predicted_price=predicted,
                forecast_price=forecast,
                split_date=split_date,
                return_fig=True
            )

            st.success("Forecast completed!")
            st.pyplot(fig)

            # Tampilkan metrik evaluasi
            st.markdown("### 📊 Evaluation Metrics (on Test Set)")
            col1, col2, col3 = st.columns(3)
            col1.metric("MAPE", f"{mape:.2f} %")
            col2.metric("MAE", f"{mae:.2f}")
            col3.metric("RMSE", f"{rmse:.2f}")