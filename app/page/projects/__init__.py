import streamlit as st

from app.page import Page
from app.utils import read_google_drive


class ProjectsPage(Page):
    title = 'Projects and Backend'

    sheet_id = '1y-0I1ObMmBNRjSCXQHVt81bBOaz5_X6r0jRvElhtYxM'

    topics = read_google_drive(sheet_id, 0)
    packages = read_google_drive(sheet_id, 329368905)
    open_source_projects = read_google_drive(sheet_id, 985331080)

    def render(self):
        self.render_topics()
        st.markdown('---')
        self.render_open_source_projects()
        st.markdown('---')
        self.render_packages()

    def render_topics(self):
        st.write(
            "If you are interested in working on any of these projects please fill out our form [here](https://forms.gle/rPC4N9WmpjPJ5Kxa6)")
        st.write(self.topics)

    def render_open_source_projects(self):
        st.header("Open-Source Projects")
        st.write(
            "If you are interested in working on any of these projects please fill out our form [here](https://forms.gle/oTh3nZJ4ffcd33KfA)")

        for i, row in self.open_source_projects.iterrows():
            st.subheader(row['Name'])
            st.write(row['Description'])

        st.write('Backend Infrastructure list [here](https://github.com/CUQuants/app/issues)')
        st.write('Bugs list: [here](https://github.com/CUQuants/app/issues)')

    def render_packages(self):
        st.header("Integration of Packages")
        st.write(
            "If you are interested in working on any of these projects please fill out our form [here](https://forms.gle/9s5PyHr46ArMPuTG6)")

        for i, row in self.packages.iterrows():
            st.subheader(row['Name'])
            st.write(row['Description'])
            st.write(f"Examples [here]({row['Link']})")

    def render_prepared(self):
        for i, row in self.open_source_projects.iterrows():
            st.write("problem here")
            st.write(row[1], row[2], row[3], row[4])
            break
