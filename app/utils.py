import streamlit as st
from pathlib import Path
import pandas as pd


def read_google_drive(key, gid=0):
    return pd.read_csv(f'https://docs.google.com/spreadsheets/d/{key}/export?format=csv&gid={gid}')


def read_file(path):
    return Path(path).read_text()


def normalize(df):
    min = df.min()
    max = df.max()
    return (df - min) / (max - min)


def standardize(df):
    return (df - df.mean()) / df.std()
