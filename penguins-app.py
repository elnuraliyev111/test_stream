
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Penguin Prediction App
This app predicts the **Palmer Penguin** species!
Data obtained from the [palmerpenguins library] in R by Allison Horst.
""")

st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file]""")