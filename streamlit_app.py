import pandas as pd
import numpy as np
import random
import plotly.express as px
import statsmodels.formula.api as smf
from plotly.subplots import make_subplots
import plotly.graph_objects as go

data = st.file_uploader('Tu wrzuc swoje dane', type=['csv'])
if data is not None:
    df = pd.read_csv(data, na_values=[" ", np.nan])
    st.dataframe(df.head(10))
