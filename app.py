import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Netflix Data Dashboard")

# Load data
df = pd.read_csv("netflix_titles.csv")
df.columns = df.columns.str.strip().str.lower()

# Sidebar filter
st.sidebar.header("Filter")

rating_filter = st.sidebar.selectbox(
    "Select Rating",
    ["All"] + list(df['rating'].dropna().unique())
)

# Apply filter
if rating_filter != "All":
    filtered_df = df[df['rating'] == rating_filter]
else:
    filtered_df = df

# Basic info
st.write("Total rows:", len(filtered_df))

# Tabs
tab1, tab2, tab3 = st.tabs(["Data", "Charts", "Search"])

# ------------------ DATA TAB ------------------
with tab1:
    st.write("Dataset Preview")
    st.dataframe(filtered_df.head(50))

# ------------------ CHARTS TAB ------------------
with tab2:

    col1, col2 = st.columns(2)

    # Ratings
    with col1:
        st.write("Ratings Distribution")
        fig, ax = plt.subplots()
        filtered_df['rating'].value_counts().plot(kind='bar', ax=ax)
        st.pyplot(fig)

    # Release year
    with col2:
        st.write("Release Year Trend")
        fig, ax = plt.subplots()
        filtered_df['release_year'].value_counts().sort_index().plot(ax=ax)
        st.pyplot(fig)

    # User rating
    st.write("User Rating Score Distribution")
    fig, ax = plt.subplots()
    filtered_df['user_rating_score'].dropna().plot(kind='hist', ax=ax)
    st.pyplot(fig)

# ------------------ SEARCH TAB ------------------
with tab3:
    st.write("Search by Title")

    search = st.text_input("Enter movie name")

    if search:
        result = filtered_df[
            filtered_df['title'].str.contains(search, case=False, na=False)
        ]
        st.dataframe(result)

# Footer
st.write("Project by Swapnil")