import sys
from threading import Thread
sys.path.append("./data")
sys.path.append("./backend")
from main import run_pipeline
import streamlit as st
import pandas as pd
from data.repo import Repo as rp
from widgets import widgets as wg

# Setting Page Layout and title
st.set_page_config(
    page_title="NBA STATS",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("NBA Statistics Dashboard🏀")
st.write("Made with 💚 by Tadiwa Shangwa")

option = st.radio(
    label="",
    options=["Wins", "Loses", "Points"],
    horizontal=True
)

if option == "Wins":
    wg.wins_widget()
elif option == "Points":
    wg.points_widgets()
else:
    wg.loses_widgets()

pipeline_thread = Thread(target=run_pipeline()) 

if __name__ == "__main__":
    pipeline_thread.start()
