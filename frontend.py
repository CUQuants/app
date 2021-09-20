import pandas as pd
import datetime as dt
import yfinance as yf
import streamlit as st

from projects import *
from inputType import *

st.set_page_config(layout="wide")

sidebar_options = ["security analysis", "projects and backend"]
sidebar = st.sidebar.selectbox("pick an option", sidebar_options)

if sidebar == "security analysis":
    
    st.title("Security Analysis")
    
    security_function_options = ["all", "general"]
    security_function = st.sidebar.selectbox("security function", security_function_options)
    
    security = st.text_input("Please enter security here (seperate):")
    input_type = inputType(security)
        
if sidebar == "projects and backend":

    projects = Projects()
    
    st.title("Projects and backend")
    projects.get_list()
    #test = projects.get_prepared()
    
    

