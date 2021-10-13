import streamlit as st
from abc import ABC

_next_id = 0


class View(ABC):
    """
    Abstract base class for creating reusable Streamlit components.
    By convention, all data initialization (self.x = y) should occur in `__init__(...)`,
    while streamlit rendering should occur in the `render()` method.

    This is an example of decoupling, a.k.a. Separation of Concerns (SoC),
    which improves code readability and maintainability in the long run.

    Refer to `examples/example_views.py` for additional information and code snippets.
    """

    # Is this the root element? Only one should exist at a time
    __root__ = False

    # Set up unique key generation
    def __new__(cls, *args, **kw):
        global _next_id
        view = super(View, cls).__new__(cls)
        if view.__root__:
            _next_id = 0
        view._id = _next_id
        _next_id += 1
        view._next_key = 0
        return view

    # Return the next unique Streamlit input key
    def next_key(self, name=None):
        key = f'view_{self._id}_{name or self._next_key}'
        self._next_key += 1
        return key

    def render(self):
        pass

    # TODO: add convenience functions accessible to View subclasses
