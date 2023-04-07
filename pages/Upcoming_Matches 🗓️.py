# import streamlit
import streamlit as st
from data.repo import Repo as rp

st.write("# Upcoming Matches 🗓️")

# get the data
table = rp.scoreboard

# visualize it
st.table(table)