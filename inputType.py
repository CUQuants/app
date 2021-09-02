import yfinance as yf
import datetime as dt
import streamlit as st

from securityInfo import *

class inputType:
    
    def __init__(self, text_input):
        
        self.text_input = text_input.split(",")
        
        if len(self.text_input) == 1:
            self.output = "single"
            
            info = SecurityInfo(text_input)
            info.get_summary()
            dates = info.get_info()
        
            df = yf.download(text_input, dates[0], dates[1])[dates[2]]
            st.line_chart(df)
        
        if len(self.text_input) == 2:
            self.output = "pair"
            
            security_info = SecurityInfo(text_input)
            dates = security_info.get_info()
            df = yf.download(text_input, dates[0], dates[1])[dates[2]]
            
            columns = []
            for i in df.columns:
                columns.append(i[1])
            
            df.columns = columns
            col1, col2 = st.columns((9,1))
            
            with col1:
                st.line_chart(df)
                
            with col2:            
                normalize_check = st.checkbox("normalize")
                
            if normalize_check == True:
                st.subheader("Normalized Prices")
                security_info.normalize(df)
                
        
        if len(self.text_input) > 2:
            self.output = "portfolio"
            
            security_info = SecurityInfo(text_input)
            dates = security_info.get_info()
            df = yf.download(text_input, dates[0], dates[1])[dates[2]]
            
            columns = []
            for i in df.columns:
                columns.append(i[1])
            
            df.columns = columns
            
            col1, col2 = st.columns((9,1))
            
            with col1:
                st.line_chart(df)
                
            with col2:            
                normalize_check = st.checkbox("normalize")
            
            if normalize_check == True:
                st.subheader("Normalized Prices")
                security_info.normalize(df)
        
            