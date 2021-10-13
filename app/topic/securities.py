import streamlit as st

from app.page.securities import SecurityData, SecurityDetail, SecuritySummary
from app.utils import input_symbols

title = 'Security Data'
description = 'Demonstrates how to programmatically fetch and display data from Yahoo Finance.'


def render():
    symbols = input_symbols()

    st.write('Symbols:', symbols)

    data = SecurityData(symbols)

    if len(symbols) == 0:
        # Empty list
        return

    # Render data visualization and return transformed data
    data_transformed = SecurityDetail(data).render()

    df = data_transformed.df  # Access to `pd.DataFrame`

    st.write(df)

    # Retrieve summary of first symbol
    summary = SecuritySummary(symbols[0])
    st.write('Ticker Info:', summary.ticker_info)
