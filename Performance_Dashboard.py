st.title("BTC Performance Dashboard")

col1, col2 = st.columns(2)
col1.metric("Last Std Return", f"{df['std_ret_fwd'].iloc[-1]:.4f}")
col2.metric("Mean Volatility", f"{df['vol'].mean():.4f}")

st.subheader("Recent Return Distribution")
st.line_chart(df['std_ret_fwd'].tail(300))
