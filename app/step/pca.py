import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

from app.page.securities import SecurityData
from app.utils import plot_time_series

title = 'Principal Component Analysis (PCA)'


def is_valid(data):
    return len(data.symbols) > 1


def render(data, index):
    df = data.df

    df = df.dropna()

    series = st.selectbox('Series:', data.column_types, key=f'pca_series_{index}')

    model = PCA(len(data.symbols), svd_solver='full')

    X_pca = model.fit_transform(df[series])
    # X_reduced = model.inverse_transform(X_pca)
    # df_reduced = pd.DataFrame(X_reduced, columns=data.symbols)

    pca_contributions = model.explained_variance_ / model.explained_variance_.sum()

    # st.bar_chart(pd.Series(pca_contributions, name='Explained variance %'))

    fig, ax = plt.subplots(1, figsize=(16, 5))
    ax.set_xlabel('PCA component')
    ax.set_ylabel('Contribution')
    ax.bar([str(i) for i in range(len(pca_contributions))], pca_contributions)
    st.pyplot(fig)

    n_components = st.slider('Components:', 1, len(data.symbols), value=min(len(data.symbols), 3), step=1,
                             key=f'pca_ncomponents_{index}')

    df_pca = pd.DataFrame({(series, f'PCA {i}'): x for i, x in zip(range(n_components), X_pca.T)})

    plot_time_series(df_pca)

    return SecurityData(df_pca.columns.get_level_values(1).unique(), df)
