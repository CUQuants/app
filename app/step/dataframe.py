import streamlit as st

title = 'Show DataFrame'


def is_valid(data):
    return True


def render(data, index):
    df = data.df

    st.write(df)
