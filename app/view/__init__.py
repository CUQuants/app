import streamlit as st
from abc import ABC


class View(ABC):
    """
    Abstract base class for creating reusable Streamlit components.
    By convention, all data initialization (self.x = y) should occur in `__init__(...)`,
    while streamlit rendering should occur in the `render()` method.

    This is an example of decoupling, a.k.a. Separation of Concerns (SoC),
    which improves code readability and maintainability in the long run.

    Refer to `examples/example_views.py` for additional information and code snippets.
    """

    def render(self):
        pass

    # TODO: add convenience functions accessible to View subclasses
