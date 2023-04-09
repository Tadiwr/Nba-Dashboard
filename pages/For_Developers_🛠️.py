import sys
sys.path.append("../data")

import streamlit as st

st.write("# About 🤔❓")

st.write("### Whats the purpose of this dashboard?")
st.write("""This dashboard is to help NBA Fans who want an all in one solution
        to get NBA Statistics! I am making an effort to add more and more features 
        and statistics for the dashboard. If you are a developer and you want to contribute to
        this dashboard you can check out the github repository. Links down below 
""")

issues_link = "https://github.com/Tadiwr/Nba-Dashboard/issues"

st.write("# Current Issues ⚠️")
st.write("- ⌛ Its takes a long time to initialy fetch data for the first time daily")
st.write("- I don't know if you noticed but the home page(the page you initialy load in!) is called main instead of Home 🏡")
f"For the rest of the issues you can check them out " + f"[here]({issues_link})"


github_logo = "../assets/dashboard.png"
repo_link = "https://github.com/Tadiwr/Nba-Dashboard"
github_account_link = "https://github.com/Tadiwr"

f"###### [Github 🦑]({repo_link})"
f"###### [Portfolio 👨🏾‍💻]({github_account_link})"
