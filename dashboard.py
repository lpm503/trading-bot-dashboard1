
import streamlit as st
import json
import pandas as pd
import os

st.set_page_config(page_title="Trading Bot Dashboard", layout="centered")

st.title("📊 Simulated Trading Dashboard")

# Load account data
account_file = "simulated_account.json"

if not os.path.exists(account_file):
    st.warning("No trading data found. Run the bot first.")
else:
    with open(account_file, "r") as f:
        account = json.load(f)

    st.subheader("💰 Account Summary")
    st.metric(label="Balance", value=f"${account['balance']:.2f}")
    st.write(f"**Open Position:** {account['position'] or 'None'}")
    if account['position']:
        st.write(f"**Entry Price:** ${account['entry_price']:.2f}")

    # Trade history
    if account['trade_history']:
        st.subheader("📈 Trade History")
        df = pd.DataFrame(account['trade_history'])
        st.dataframe(df[::-1])  # reverse for latest first
    else:
        st.info("No trades executed yet.")
