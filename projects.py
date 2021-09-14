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
        
    def get_open_source_list(self):
        
        st.title("Open Source Projects")
        for i in range(len(self.open_source_project)):
            st.header(self.open_source_project[self.open_source_project.columns[0]][i])
            st.write(self.open_source_project[self.open_source_project.columns[1]][i])
    
    def get_list(self):
        st.write(self.codebase_library)       
        self.get_open_source_list()
    
    def get_prepared(self):
        
        for i in range(len(self.codebase_library)):
            
            row = self.codebase_library.iloc[i]
            st.write(row[1], row[2], row[3], row[4])
            break
            

        