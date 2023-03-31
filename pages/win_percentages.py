import sys
sys.path.append("../data")

import streamlit as st
from data.repo import Repo as rp
import utils.utils as ut 

st.title("Win Percentages 🍾")
"\n"
data = rp.static.get_win_percentages()

"---------------------------------"
ave = round(data["Win Percentage"].mean(), 2)
col1, col2, col3 = st.columns(3)

def avepec():
    col1.write("### Average Win Percentage")
    col1.metric(
        label="",
        value=ave
    )

def max():
    df = data.sort_values(by="Win Percentage")
    max = df.iloc[-1]
    col2.write("### Heights Win Percentage")
    col2.metric(
        label=max["Team"],
        value=max["Win Percentage"]
    )

def min():
    df = data.sort_values(by="Win Percentage")
    min = df.iloc[0]
    col3.write("### Lowest Win Percentage")
    col3.metric(
        label=min["Team"],
        value=min["Win Percentage"]
    )

avepec()
max()
min()
"--------------------------------"
st.bar_chart(data, x = "Team", y="Win Percentage")
"----------------------------------------------"
st.table(data)
