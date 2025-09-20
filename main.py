import streamlit as st
import pandas as pd

class SessionState:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

@st.cache(allow_output_mutation=True)
def get_session():
    return SessionState(df=pd.DataFrame())

session_state = get_session()

# Creating a dictionary with some data
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 35, 40, 25]
}

# Creating a DataFrame with the data
df = pd.DataFrame(data)

# Assigning this DataFrame to session_state
session_state.df = df
