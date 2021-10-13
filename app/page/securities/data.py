import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import datetime as dt

from app import utils


# TODO: move to standalone wrapper library
class SecurityData:
    """
    Wrapper around a `pandas.DataFrame` consisting of OHLCV data for one or more securities.
    """

    def __init__(self, symbols, df: pd.DataFrame = None):
        if df is None:
            end = dt.date.today()
            start = dt.date(end.year - 50, end.month, end.day)

            df = yf.download(symbols, start, end) if len(symbols) else pd.DataFrame()
            df.sort_index(inplace=True)

        if len(symbols) == 1 and df.columns.nlevels == 1:
            # Add symbol column if missing
            symbol = symbols[0]
            df = pd.DataFrame({(col, symbol): df[col] for col in df.columns})

        self.symbols = symbols
        self.column_types = df.columns.get_level_values(0).unique() if df.columns.nlevels > 1 else df.columns
        self.df = df

    def get_start_end(self):
        return self.df.index[0].to_pydatetime(), self.df.index[-1].to_pydatetime()

    def transform(
            self,
            df=None,
            start=None,
            end=None,
            columns=None,
            log=False,
            diff=False,
            normalize=False,
            standardize=False,
            trend_window=0,
            subtract_trend=False,
    ):
        if df is None:
            df = self.df

        if start is not None:
            df = df[df.index >= start]

        if end is not None:
            df = df[df.index <= end]

        if columns is not None:
            df = df[list(columns)]

        if log:
            df = np.log10(df)

        if diff:
            df = df.diff()

        if normalize:
            df = utils.normalize(df)

        if standardize:
            df = utils.standardize(df)

        if trend_window > 0:
            df_trend = df.rolling(trend_window).mean()
            df = df - df_trend if subtract_trend else df_trend

        return SecurityData(self.symbols, df)
