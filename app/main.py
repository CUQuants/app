import streamlit as st
import datetime as dt
import requests_cache

from app.view import View
from app.page.projects import ProjectsPage
from app.page.securities import SecurityPage


class Main(View):
    def __init__(self):
        self.cache_hours = 1
        requests_cache.install_cache(expire_after=dt.timedelta(hours=self.cache_hours))

        self.main_pages = [
            SecurityPage(),
            ProjectsPage(),
        ]

    def render(self):
        st.set_page_config(layout="wide")

        # TODO: Include a button to reset cache?
        # st.sidebar.button('Clear Cache', lambda: requests_cache.clear())

        page_title = st.sidebar.selectbox("Select page:", [page.title for page in self.main_pages])

        for page in self.main_pages:
            if page.title == page_title:
                st.title(page.title)
                page.render()
                break
