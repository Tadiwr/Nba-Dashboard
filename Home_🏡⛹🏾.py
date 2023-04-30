import sys
sys.path.append("./data")
import streamlit as st
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
    label="What stats do you want to view?",
    options=["Wins", "Loses", "Points"],
    horizontal=True
)

if option == "Wins":
    wg.wins_widget()
elif option == "Points":
    wg.points_widgets()
else:
    wg.loses_widgets()

