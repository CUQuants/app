"""
Created on Thu Sep  2

@author: diegoalvarez
@email: diego.alvarez@colorado.edu
@email: diegoalvarez3800@gmail.com
"""

import pandas as pd
import datetime as dt
import yfinance as yf
import streamlit as st

class SecurityInfo():
    
    def __init__(self, security):
        
        self.security = security
        self.ticker_info = yf.Ticker(self.security).get_info()
     
    def get_last_sentance(self):
        
        for i in reversed(range(len(self.info))):
            
            if len(self.info[i]) > 1:
                last_sentance = self.info[i]
                break
            
        return last_sentance
        
    def get_summary(self):
        
        self.info = self.ticker_info['longBusinessSummary']
        self.info = self.info.split(".")
        name = self.ticker_info['shortName'].strip(".")
        
        name_period = True
        
        for idx, i in enumerate(self.info):
            
            if i.strip() == name:
                
                first_sentance = str(self.info[idx].strip() + ". " + self.info[idx+1].strip() + ". ")
                name_period = False
                
                last_sentance = str(i.strip() + ". " + self.get_last_sentance().strip() + ".")
                st.write(first_sentance + last_sentance)
                break
                
        if name_period == True:
        
            first_sentance = self.info[0]
            last_sentance = self.get_last_sentance()
            st.write(first_sentance.strip() + ".", last_sentance.strip() + ".")
   

    def get_timeframe_dates(self):
    
        timeframe_start = pd.to_datetime(self.df.index[0]).date()
        timeframe_end = pd.to_datetime(self.df.index[len(self.df) - 1]).date()
        
        return (timeframe_start, timeframe_end)

    def security_types(self):
    
        security_open = st.checkbox("Open")
        security_high = st.checkbox("High")
        security_low = st.checkbox("Low")
        security_close = st.checkbox("Close")
        security_adj_close = st.checkbox("Adj Close")
        security_volume = st.checkbox("Volume")
        checkbox_list = [security_open, security_high, security_low, security_close, security_adj_close, security_volume]
        
        return checkbox_list
    
    def make_show_list(self, checkbox_list):
        
        show_list = []
            
        if checkbox_list[0] == True:
            show_list.append("Open")
            
        if checkbox_list[1] == True:
            show_list.append("High")
            
        if checkbox_list[2] == True:
            show_list.append("Low")
            
        if checkbox_list[3] == True:
            show_list.append("Close")
            
        if checkbox_list[4] == True:
            show_list.append("Adj Close")
         
        if checkbox_list[5] == True:
            show_list.append("Volume")
                
        return show_list
    

    def get_info(self):
        
        self.ticker_info = yf.Ticker(self.security).get_info()
        
        end = dt.date.today()
        start = dt.date(end.year - 50, end.month, end.day)
        self.df = yf.download(self.security[0], start, end)
    
        col1, col2 = st.columns((1, 2))

        with col1:
            show_list = self.make_show_list(self.security_types())
            
        with col2:
            
            dates_method = st.radio("select dates type", ["slider", "years back"])
            

            if dates_method == "slider":
            
                timeframe_dates = self.get_timeframe_dates()
                timeframe = st.slider("Select time frame:", value=(timeframe_dates[0], timeframe_dates[1]))
                start = timeframe[0]
                end = timeframe[1]
            
            if dates_method == "years back":
                
                years = st.number_input("select years", min_value = 1)
                end = dt.date.today()
                start = dt.date(end.year - years, end.month, end.day)
                    
            return (start, end, show_list)
        
    def normalize(self, df):
    
        min = df.min()
        max = df.max()
        x = df 
        y = (x - min) / (max - min)
        
        st.line_chart(y)

