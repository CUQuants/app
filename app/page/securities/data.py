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

    def __init__(self, symbols):
        self.symbols = symbols

        end = dt.date.today()
        start = dt.date(end.year - 50, end.month, end.day)

        self.df = yf.download(self.symbols, start, end) if len(symbols) else pd.DataFrame()
        self.df.sort_index(inplace=True)

    def get_start_end(self):
        return self.df.index[0].to_pydatetime(), self.df.index[-1].to_pydatetime()

    def get_columns(self):
        if isinstance(self.df.columns, pd.MultiIndex):
            return self.df.columns.levels[0]
        return self.df.columns

    def preprocess(self, start=None, end=None, columns=None, log=False, diff=False, normalize=False, standardize=False):
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

        return df
