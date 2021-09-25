import streamlit as st
from abc import ABC


# Abstract view component for rendering Streamlit content
class View(ABC):
    def render(self):
        pass

    # TODO: add convenience functions accessible to View subclasses
