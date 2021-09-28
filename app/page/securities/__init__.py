import streamlit as st
import datetime as dt
from dateutil import relativedelta

from app.page import Page
from app.view import View
from app.page.securities.summary import SecuritySummary
from app.page.securities.data import SecurityData


class SecurityPage(Page):
    title = 'Security Analysis'
    symbols_query_param = 'symbols'

    def render(self):
        security_function_options = ["All", "General"]
        security_function = st.sidebar.selectbox("Security function:", security_function_options)

        # Use symbols from URL query param
        default_symbols = st.experimental_get_query_params().get(self.symbols_query_param, '')
        if isinstance(default_symbols, list):
            default_symbols = ", ".join(default_symbols)

        symbols_text = st.text_input("Enter securities (comma-separated):", default_symbols).upper()
        symbols = [symbol.strip() for symbol in symbols_text.split(",") if len(symbol.strip())]

        # Save symbols to URL query param
        # st.experimental_set_query_params(**{self.securities_query_param: symbols_text or ''})

        detail = SecurityDetail(symbols)
        detail.render()


class SecurityDetail(View):

    def __init__(self, symbols):
        self.symbols = symbols

        if len(self.symbols) == 1:
            self.summary = SecuritySummary(self.symbols[0])
        else:
            self.summary = None

        self.data = SecurityData(self.symbols)

        # if len(self.symbols) == 1:
        #     self.output = "single"
        # elif len(self.symbols) == 2:
        #     self.output = "pair"
        # elif len(self.symbols) > 2:
        #     self.output = "portfolio"

    def render(self):
        if len(self.symbols) == 0:
            return

        start, end, columns = self.render_data_options()

        if self.summary:
            self.render_summary()

        self.plot_with_controls(start, end, columns)

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
            columns = [col for col in self.data.get_columns() if st.checkbox(col, col == 'Adj Close')]

        with col2:
            dates_method = st.radio("Select dates type", ["Slider", "Months back", "Years back"])

            if dates_method == "Slider":
                start, end = st.slider("Select time frame:", value=self.data.get_start_end())

            if dates_method == "Months back":
                months = st.number_input("Select months:", min_value=1)
                end = dt.date.today()
                start = end - relativedelta(months=months)

            if dates_method == "Years back":
                years = st.number_input("Select years:", min_value=1)
                end = dt.date.today()
                start = end - relativedelta(years=years)

        return start, end, columns

    def plot_with_controls(self, start, end, columns):

        col1, col2 = st.columns((8, 2))

        with col2:
            log = st.checkbox("Logarithmic", len(self.data.symbols) > 1)
            diff = st.checkbox("Difference")
            normalize = st.checkbox("Normalize")
            standardize = st.checkbox("Standardize")
            trend_window = st.number_input("Moving Average", min_value=0, max_value=len(self.data.df.index), step=5)
            subtract_trend = st.checkbox("Subtract Trend") if trend_window else 0

            df = self.data.preprocess(
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

        with col1:
            # Prevent error caused by MultiIndex columns
            if len(self.symbols) > 1:
                df.columns = [', '.join(col) for col in df.columns]

            st.line_chart(df)
