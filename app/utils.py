import streamlit as st
from pathlib import Path
import pandas as pd


def input_symbols(query_key='symbols'):
    # Use symbols from URL query param
    default_symbols = st.experimental_get_query_params().get(query_key)
    if isinstance(default_symbols, list):
        default_symbols = ', '.join(default_symbols)

    symbols_text = st.text_input("Enter securities (comma-separated):", default_symbols).upper()
    return [symbol.strip() for symbol in symbols_text.split(",") if len(symbol.strip())]


def read_google_spreadsheet(key, gid=0):
    return pd.read_csv(f'https://docs.google.com/spreadsheets/d/{key}/export?format=csv&gid={gid}')


def read_file(path):
    return Path(path).read_text()


def normalize(df):
    min = df.min()
    max = df.max()
    return (df - min) / (max - min)


def standardize(df):
    return (df - df.mean()) / df.std()


def load_directory(path):
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
