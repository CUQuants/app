import os

import streamlit as st
import datetime as dt
import pandas as pd

from app.page import Page
from app.utils import load_directory, plot_time_series
from app.view import View
from app.page.securities.summary import SecuritySummary
from app.page.securities.data import SecurityData


class SecurityPage(Page):
    key = 'securities'
    title = 'Security Analysis'
    symbols_query_param = 'symbols'

    query_steps = st.experimental_get_query_params().get('steps', [])

    step_path = os.path.join(os.path.dirname(__file__), '../../step')

    def __init__(self):
        self.step_modules = load_directory(self.step_path)

    def render(self):
        # security_function_options = ['All', 'General']
        # security_function = st.sidebar.selectbox("Security function:", security_function_options)

        # Use symbols from URL query param
        default_symbols = st.experimental_get_query_params().get(self.symbols_query_param, '')
        if isinstance(default_symbols, list):
            default_symbols = ', '.join(default_symbols)

        symbols_text = st.text_input('Enter securities (comma-separated):', default_symbols).upper()
        symbols = [symbol.strip() for symbol in symbols_text.split(',') if len(symbol.strip())]

        # Save symbols to URL query param
        # st.experimental_set_query_params(**{self.securities_query_param: symbols_text or ''})

        # Details and visualization
        detail = SecurityDetail(SecurityData(symbols))
        current_data = detail.render()  # Returns data with differencing, normalization, etc.

        # Custom analysis steps
        if len(symbols):
            for i in range(100):  # Limit number of steps in case of infinite loop
                if i < len(self.query_steps):
                    # Load step from query param
                    module = self.step_modules.get(self.query_steps[i], None)
                    if not module or not module.is_valid(current_data):
                        continue
                else:
                    # Load step from dropdown
                    names = sorted(name for name, module in self.step_modules.items() if module.is_valid(current_data))
                    default_option = '...'
                    titles = [self.step_modules[name].title for name in names]
                    title = st.sidebar.selectbox('Next analysis step:', [default_option] + titles, key=f'step_{i}')
                    if title == default_option:
                        st.sidebar.write(f'**Column types:**', ', '.join(current_data.column_types))
                        st.sidebar.write(f'**Symbols:**', ', '.join(current_data.symbols))
                        break
                    module = self.step_modules[names[titles.index(title)]]

                st.write(f'#### {module.title}')
                # Render and update data for next step
                current_data = module.render(current_data, i) or current_data


class SecurityDetail(View):

    def __init__(self, data: SecurityData):
        self.data = data
        self.symbols = data.symbols

        if len(self.symbols) == 1:
            self.summary = SecuritySummary(self.symbols[0])
        else:
            self.summary = None

    def render(self):
        if len(self.symbols) == 0:
            return

        start, end, columns = self.render_data_options()

        if self.summary:
            self.render_summary()

        return self.plot_with_controls(start, end, columns)

    def render_summary(self):
        name_period = False
        if len(self.symbols) == 1:
            name = self.summary.ticker_info['shortName'].strip(".")
            name_period = True

            lines = self.summary.lines
            for i, line in enumerate(lines):
                if line.strip() == name:
                    first_sentence = str(line + ". " + lines[i + 1] + ". ")
                    name_period = False

                    last_sentence = str(line + ". " + self.summary.get_last_sentence() + ".")
                    st.write(first_sentence + last_sentence)
                    break

        if name_period:
            first_sentence = self.summary.lines[0]
            last_sentence = self.summary.get_last_sentence()
            st.write(first_sentence.strip() + ".", last_sentence.strip() + ".")

    def render_data_options(self):
        col1, col2 = st.columns((1, 2))

        with col1:
            # OHLCV column filter
            column_types = [col for col in self.data.column_types if st.checkbox(col, col == 'Adj Close', key=self.next_key())]

        with col2:
            dates_method = st.radio("Select dates type", ["Slider", "Months back", "Years back"], key=self.next_key())

            if dates_method == "Slider":
                start, end = st.slider("Select time frame:", value=self.data.get_start_end(), key=self.next_key())
            elif dates_method == "Months back":
                months = st.number_input("Select months:", min_value=1, key=self.next_key())
                end = dt.datetime.today()
                start = end - pd.DateOffset(months=months)
            elif dates_method == "Years back":
                years = st.number_input("Select years:", min_value=1, key=self.next_key())
                end = dt.datetime.today()
                start = end - pd.DateOffset(years=years)

        return start, end, column_types

    def plot_with_controls(self, start, end, columns):

        col1, col2 = st.columns((8, 2))

        with col2:
            log = st.checkbox("Logarithmic", len(self.data.symbols) > 1, key=self.next_key())
            diff = st.checkbox("Difference", key=self.next_key())
            normalize = st.checkbox("Normalize", key=self.next_key())
            standardize = st.checkbox("Standardize", key=self.next_key())
            trend_window = st.number_input("Moving Average", min_value=0, max_value=len(self.data.df.index), step=5,
                                           key=self.next_key())
            subtract_trend = st.checkbox("Subtract Trend", key=self.next_key()) if trend_window else 0

            transformed_data = self.data.transform(
                start=start,
                end=end,
                columns=columns,
                log=log,
                diff=diff,
                normalize=normalize,
                standardize=standardize,
                trend_window=trend_window,
                subtract_trend=subtract_trend,
            )
            df = transformed_data.df

        with col1:
            plot_time_series(df)

        return transformed_data
