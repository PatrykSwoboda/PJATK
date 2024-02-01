import pandas as pd
import numpy as np
import streamlit as st

data = st.file_uploader('Tu wrzuc swoje dane', type=['csv'])
if data is not None:
    df = pd.read_csv(data, na_values=[" ", np.nan])
    st.dataframe(df.head(10))
