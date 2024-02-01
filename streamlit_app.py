import pandas as pd
import numpy as np
import streamlit as st
import datetime
import time

data = st.file_uploader('Tu wrzuc swoje dane', type=['csv'])
if data is not None:
    df.pd.read_csv(data)
    st.dataframe(df.head(10))
