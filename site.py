import streamlit as st
import webbrowser

st.title("🎯 Focus Group Dashboard")


if st.button("Open FindFocusGroups"):
    webbrowser.open("https://www.findfocusgroups.com/paid-focus-groups/new-york-city/")

if st.button("Open App . Respondent"):
    webbrowser.open("https://app.respondent.io/respondents/v2/dashboard/")

if st.button("Open User Interviews"):
    webbrowser.open("https://www.userinterviews.com/studies?sort=-id")

st.text_area("Paste links here to track")
