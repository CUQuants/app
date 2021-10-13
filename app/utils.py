import streamlit as st
from pathlib import Path
import pandas as pd


def input_symbols(query_key='symbols'):
    # Use symbols from URL query param
    default_symbols = ', '.join(st.experimental_get_query_params().get(query_key, []))

    symbols_text = st.text_input("Enter securities (comma-separated):", default_symbols).upper()
    return [symbol.strip() for symbol in symbols_text.split(",") if len(symbol.strip())]


def read_google_spreadsheet(key, gid=0):
    return pd.read_csv(f'https://docs.google.com/spreadsheets/d/{key}/export?format=csv&gid={gid}')


def read_file(path: str):
    return Path(path).read_text()


def normalize(df: pd.DataFrame):
    min = df.min()
    max = df.max()
    return (df - min) / (max - min)


def standardize(df: pd.DataFrame):
    return (df - df.mean()) / df.std()


def load_directory(path: str):
    import os
    import importlib.util

    modules = {}

    for filename in os.listdir(path):
        if filename.endswith('.py'):
            name = filename[:-len(".py")]
            spec = importlib.util.spec_from_file_location(
                f'app.topic.{name}',
                os.path.join(path, filename),
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            modules[name] = module

    return modules


# Plot data with (series, symbol) column layout (e.g. Yahoo Finance)
def plot_time_series(df: pd.DataFrame):
    # Prevent error caused by MultiIndex columns
    if df.columns.nlevels > 1:
        df = df.copy()
        cols = df.columns
        if len(df.columns.get_level_values(0).unique()) <= 1:
            cols = [col[1:] for col in cols]
        df.columns = [', '.join(col) for col in cols]
    st.line_chart(df)
