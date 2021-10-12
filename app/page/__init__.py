import streamlit as st

from app.view import View


class Page(View):
    """
    Base class for top-level page views.
    """
    key = ''
    title = 'Unnamed Page'
