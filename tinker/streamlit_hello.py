"""A tiny web app in Python. Needs streamlit installed (a grown-up step)."""

import streamlit as st

st.title("Hello, world.")
st.write("You just made a web app. In Python. With like 5 lines of code.")

# TODO(you): change the title above, or add another line below.
# Try st.write("...") or st.button("Click me") or st.slider("Pick a number", 0, 100)

name = st.text_input("What's your name?")
if name:
    st.write(f"Hi, {name}.")
