import streamlit as st
import os

from app.page import Page
from app.utils import load_directory


class TopicsPage(Page):
    key = 'topics'
    title = 'Topics & Code Examples'

    topic_path = os.path.join(os.path.dirname(__file__), '../../topic')

    def __init__(self):
        self.modules = load_directory(self.topic_path)

        self.query_topics = st.experimental_get_query_params().get('topic')

    def render(self):
        topic = st.sidebar.selectbox(
            'Choose a topic:',
            sorted(module.title for name, module in self.modules.items()
                   if not self.query_topics or name in self.query_topics))

        for name, module in self.modules.items():
            if module.title == topic:
                st.write('---')
                st.header(module.title)
                if hasattr(module, 'description'):
                    st.write(module.description)
                st.write('---')
                module.render()
                break
