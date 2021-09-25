import streamlit as st

from app.page import Page
from app.utils import read_google_drive


class ProjectsPage(Page):
    title = 'Projects and Backend'

    codebase_library = read_google_drive('1seBg9Gu5S4xDxUjEwduufSQWTA15V3N-IdpzB5PEOnk')
    open_source_project = read_google_drive('1F1QzElHO0dz4t8JPOEmEPDq13aa60Lbz9ildPm_KTnU')
    packages = read_google_drive('1BVYK4qmgZaUJHw0x1Xq8G8EvuS-5-JIK009Ll1WeDNE')

    def render(self):
        self.render_lists()

    def render_open_source_list(self):
        st.write(
            "If you are interested in working on any of these projects please fill out our form [here](https://forms.gle/oTh3nZJ4ffcd33KfA)")

        for i in range(len(self.open_source_project)):
            st.header(self.open_source_project[self.open_source_project.columns[0]][i])
            st.write(self.open_source_project[self.open_source_project.columns[1]][i])

        st.write(
            'Backend Infrastructure list: [here](https://docs.google.com/spreadsheets/d/1falnY478mZZAY3lVGpDhpechekfTQvQK-F2DoxIvLyk/edit?usp=sharing)')
        st.write(
            'Bugs list: [here](https://docs.google.com/spreadsheets/d/1h0mNp1qTaz2XPqChcETDdqLye0v_oXdT1v5dsbdSTig/edit?usp=sharing)')

    def render_packages_list(self):
        st.title("Integration of Packages:")
        st.write(
            "If you are interested in working on any of these projects please fill out our form [here](https://forms.gle/9s5PyHr46ArMPuTG6)")

        for i in range(len(self.packages)):
            st.header(self.packages[self.packages.columns[0]][i])
            st.write(self.packages[self.packages.columns[1]][i])
            link = self.packages[self.packages.columns[2]][i]
            st.write("see examples:", link)

    def render_lists(self):
        st.write(
            "If you are interested in working on any of these projects please fill out our form [here](https://forms.gle/rPC4N9WmpjPJ5Kxa6)")
        st.write(self.codebase_library)
        self.render_open_source_list()
        self.render_packages_list()

    def render_prepared(self):
        for i, row in self.codebase_library.iterrows():
            st.write("problem here")
            st.write(row[1], row[2], row[3], row[4])
            break
