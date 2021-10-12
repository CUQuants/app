import streamlit as st
import pandas as pd
from sklearn.decomposition import PCA

title = 'Principal Component Analysis (PCA)'


def is_valid(data):
    return len(data.symbols) > 1


def render(data):
    df = data.df

    df = df.dropna()

    series = st.selectbox('Series:', data.get_columns())
    n_components = st.slider('Components:', 1, len(data.symbols), value=min(len(data.symbols), 10), step=1)

    model = PCA(n_components, svd_solver='full')

    X_pca = model.fit_transform(df[series])
    X_reduced = model.inverse_transform(X_pca)

    df_reduced = pd.DataFrame(X_reduced, columns=data.symbols)

    st.bar_chart(pd.Series(model.explained_variance_ / model.explained_variance_.sum(), name='Explained variance %'))

    st.line_chart(df_reduced)
