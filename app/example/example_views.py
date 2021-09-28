import streamlit as st
from dataclasses import dataclass

from app.view import View


class SimpleView(View):
    def render(self):
        st.write('Simple view')


@dataclass
class DataclassView(View):
    text: str

    def render(self):
        st.write(f'Dataclass view with string argument: {self.text}')


class InitializedView(View):
    def __init__(self, value):
        self.value = value

    def render(self):
        st.write('View with custom __init__ logic and call to helper method')
        self.render_value()

    def render_value(self):
        st.write(f'self.value = {self.value}')


if __name__ == '__main__':
    # Render each example view
    SimpleView().render()
    DataclassView(text='Example').render()
    InitializedView(123).render()
