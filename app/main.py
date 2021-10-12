import streamlit as st
import datetime as dt
import requests_cache

from app.page.topics import TopicsPage
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
            TopicsPage(),
        ]

        # TODO: move logic into Page subclasses
        query = st.experimental_get_query_params()
        default_page_key = query.get('page')
        if 'topic' in query:
            default_page_key = 'topics'
        elif 'symbols' in query:
            default_page_key = 'securities'
        self.default_page_key = [*(page.key for page in self.main_pages if page.key == default_page_key), None][0]

    def render(self):
        st.set_page_config(page_title='CU Quants', layout='wide')

        # TODO: Include a button to reset cache?
        # st.sidebar.button('Clear Cache', lambda: requests_cache.clear())

        default_page_index = 0
        if self.default_page_key:
            default_page_index = [page.key for page in self.main_pages].index(self.default_page_key)

        page_title = st.sidebar.selectbox(
            'Select page:',
            [page.title for page in self.main_pages],
            index=default_page_index,
        )

        for page in self.main_pages:
            if page.title == page_title:
                st.title(page.title)
                page.render()
                break
