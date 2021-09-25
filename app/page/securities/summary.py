import streamlit as st
import yfinance as yf
import pandas as pd
import datetime as dt


# TODO: move to standalone wrapper library
class SecuritySummary:
    """
    Wrapper for simplified access to details about a specific security.
    """

    def __init__(self, symbol):
        self.symbol = symbol

        self.ticker_info = yf.Ticker(self.symbol).get_info()
        self.lines = [line.strip() for line in self.ticker_info['longBusinessSummary'].split(".") if line.strip()]

    def get_last_sentence(self):
        return self.lines[-1] if len(self.lines) else None
