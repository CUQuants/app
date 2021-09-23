import numpy as np
import pandas as pd
import streamlit as st

class Projects():
    
    def __init__(self):
    
        self.codebase_url = 'https://docs.google.com/spreadsheets/d/1seBg9Gu5S4xDxUjEwduufSQWTA15V3N-IdpzB5PEOnk/edit#gid=0'
        self.codebase_url = self.codebase_url.replace('/edit#gid=', '/export?format=csv&gid=')
        self.codebase_library = pd.read_csv(self.codebase_url)
        
        self.open_source_project_url = "https://docs.google.com/spreadsheets/d/1F1QzElHO0dz4t8JPOEmEPDq13aa60Lbz9ildPm_KTnU/edit#gid=0"
        self.open_source_project_url = self.open_source_project_url.replace('/edit#gid=', '/export?format=csv&gid=')
        self.open_source_project = pd.read_csv(self.open_source_project_url)
        
        self.packages_url = "https://docs.google.com/spreadsheets/d/1BVYK4qmgZaUJHw0x1Xq8G8EvuS-5-JIK009Ll1WeDNE/edit#gid=0"
        self.packages_url = self.packages_url.replace('/edit#gid=', '/export?format=csv&gid=')
        self.packages = pd.read_csv(self.packages_url)
        
    def get_open_source_list(self):
        
        st.title("Open Source Projects")
        st.write("If you are interested in working on any of these projects please fill out our form [here](https://forms.gle/oTh3nZJ4ffcd33KfA)")

        for i in range(len(self.open_source_project)):
            st.header(self.open_source_project[self.open_source_project.columns[0]][i])
            st.write(self.open_source_project[self.open_source_project.columns[1]][i])
            
        st.write('Backend Infrastructure list: [here](https://docs.google.com/spreadsheets/d/1falnY478mZZAY3lVGpDhpechekfTQvQK-F2DoxIvLyk/edit?usp=sharing)')
        st.write('Bugs list: [here](https://docs.google.com/spreadsheets/d/1h0mNp1qTaz2XPqChcETDdqLye0v_oXdT1v5dsbdSTig/edit?usp=sharing)')

    def get_packages_list(self):
        
        st.title("Integration of Packages:")
        st.write("If you are interested in working on any of these projects please fill out our form [here](https://forms.gle/9s5PyHr46ArMPuTG6)")

        for i in range(len(self.packages)):
            
            st.header(self.packages[self.packages.columns[0]][i])
            st.write(self.packages[self.packages.columns[1]][i])
            link = self.packages[self.packages.columns[2]][i]
            st.write("see examples:", link)
    
    def get_list(self):
        
        st.title("Projects and backend")
        st.write("If you are interested in working on any of these projects please fill out our form [here](https://forms.gle/rPC4N9WmpjPJ5Kxa6)")
        st.write(self.codebase_library)       
        self.get_open_source_list()
        

        self.get_packages_list()
    
    def get_prepared(self):
        
        for i in range(len(self.codebase_library)):
            
            st.write("problem here")
            row = self.codebase_library.iloc[i]
            st.write(row[1], row[2], row[3], row[4])
            break
            

        