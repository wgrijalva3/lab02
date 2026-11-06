# This creates the page for displaying data visualizations.
import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt

# PAGE CONFIGURATION
st.set_page_config(page_title="Visuals", page_icon="📈",)

# PAGE TITLE
st.title("Data Visualizations 📈")

# PART 1: GRAPHS FROM data.json
# --- YOUR CODE GOES HERE ---
with open("data.json") as f:
    json_data = json.load(f)
st.header("Most Streamed Songs on Spotify 🎵")
st.caption("Source: " + json_data["source"])
songs = pd.DataFrame(json_data["data_points"])
songs = songs.rename(columns={"label": "Song", "artist": "Artist", "streams_billions": "Streams (billions)", "release_year": "Release Year",})

# Chart 1 (static & advanced): Matplotlib scatter plot
st.subheader("Release Year vs. Streams")
fig, ax = plt.subplots()
ax.scatter(songs["Release Year"], songs["Streams (billions)"])
ax.set_title("Do Newer Songs Have More Streams?")
ax.set_xlabel("Release Year")
ax.set_ylabel("Streams (billions)")
st.pyplot(fig)

# Chart 2 (dynamic): bar chart with slider
st.subheader("Streams by Song")
min_year = int(songs["Release Year"].min())
max_year = int(songs["Release Year"].max())
year_range = st.slider("Show songs released between:", min_value=min_year, max_value=max_year, value=(min_year, max_year),)
in_range = songs[songs["Release Year"].between(year_range[0], year_range[1])]

if in_range.empty:
    st.warning("There were no songs released during this time period")
else:
    st.bar_chart(in_range.set_index("Song")["Streams (billions)"])
    # Extra credit:
    mean = round(float(in_range["Streams (billions)"].mean()), 2)
    median = round(float(in_range["Streams (billions)"].median()), 2)

    if "current_stats" not in st.session_state:
        st.session_state.current_stats = {"range": year_range, "mean": mean, "median": median}
        st.session_state.previous_stats = None
    elif st.session_state.current_stats["range"] != year_range:
        st.session_state.previous_stats = st.session_state.current_stats
        st.session_state.current_stats = {"range": year_range, "mean": mean, "median": median}

    prev = st.session_state.previous_stats
    mean_change = None if prev is None else round(mean - prev["mean"], 2)
    median_change = None if prev is None else round(median - prev["median"], 2)
    col1, col2 = st.columns(2)
    col1.metric("Mean Streams (billions)", mean, delta=mean_change)
    col2.metric("Median Streams (billions)", median, delta=median_change)


# PART 2: GRAPHS FROM data.csv
# --- YOUR CODE GOES HERE ---
st.divider()
st.header("Music Survey Results")
survey = pd.read_csv("data.csv")
 
if survey.empty:
    st.info("No survey responses yet. Fill out the Survey page first, then come back here.")
else:
    st.subheader("Chart 3: Favorite Genres") #static & advanced
    genre_counts = survey["Genre"].value_counts()
    fig2, ax2 = plt.subplots()
    ax2.pie(genre_counts, labels=genre_counts.index, autopct="%1.0f%%")
    ax2.set_title("Share of Survey Responses by Favorite Genre")
    st.pyplot(fig2)

    st.subheader("Chart 4: Listening Time by Genre") #Dynamic
    stat_choice = st.radio("Change data to view to:", ["Average Hours per day", "Total Hours per Day", "Number of Responses"], horizontal = True)

    if stat_choice == "Average Hours per Day":
        genre_stats = survey.groupby("Genre")["Hours"].mean()
    elif stat_choice == "Total Hours per Day":
        genre_stats = survey.groupby("Genre")["Hours"].sum()
    else:
        genre_stats = survey.groupby("Genre")["Hours"].count()
    st.bar_chart(genre_stats)

    csv_mean = round(float(genre_stats.mean()), 2)
    csv_median = round(float(genre_stats.median()), 2)

    if "csv_current_stats" not in st.session_state:
        st.session_state.csv_current_stats = {"choice": stat_choice, "mean": csv_mean, "median": csv_median}
        st.session_state.csv_previous_stats = None
    elif st.session_state.csv_current_stats["choice"] != stat_choice:
        st.session_state.csv_previous_stats = st.session_state.csv_current_stats
        st.session_state.csv_current_stats = {"choice": stat_choice, "mean": csv_mean, "median": csv_median}
 
    csv_prev = st.session_state.csv_previous_stats
    csv_mean_change = None if csv_prev is None else round(csv_mean - csv_prev["mean"], 2)
    csv_median_change = None if csv_prev is None else round(csv_median - csv_prev["median"], 2)
 
    col3, col4 = st.columns(2)
    col3.metric("Mean", csv_mean, delta=csv_mean_change)
    col4.metric("Median", csv_median, delta=csv_median_change)






