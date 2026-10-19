import streamlit as st

from recommender import recommend_places


st.set_page_config(
    page_title="ASTANA PULSE AI",
    page_icon="🌆",
    layout="wide"
)


st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(
            135deg,
            #080B1A,
            #141B38
        );

        color: white;
    }

    h1, h2, h3 {
        color: white !important;
    }

    div.stButton > button {
        background: linear-gradient(
            90deg,
            #7C3AED,
            #2563EB
        );

        color: white;
        border-radius: 12px;
        border: none;
        padding: 12px 24px;
        font-weight: 600;
    }

    div.stButton > button:hover {
        color: white;
        border: 1px solid #A78BFA;
    }

    </style>
    """,
    unsafe_allow_html=True
)


st.title("🌆 ASTANA PULSE AI")

st.subheader(
    "Discover Astana with Artificial Intelligence"
)

st.write(
    "Find places based on your interests, "
    "available time and budget."
)

st.divider()


location = st.selectbox(
    "📍 Your location",
    [
        "Mega Silk Way",
        "Khan Shatyr",
        "Baiterek",
        "EXPO",
        "City Center",
        "Other"
    ]
)


time = st.selectbox(
    "⏰ Available time",
    [
        "30 minutes",
        "1 hour",
        "2 hours",
        "3 hours",
        "4 hours"
    ]
)


budget = st.slider(
    "💰 Your budget (KZT)",
    min_value=0,
    max_value=20000,
    value=5000,
    step=500
)


interests = st.multiselect(
    "❤️ What are you interested in?",
    [
        "Coffee",
        "Food",
        "Shopping",
        "Entertainment",
        "Culture",
        "Museums",
        "Nature",
        "Walking",
        "Relax",
        "Cinema"
    ]
)


st.divider()


if st.button("🔍 Find Recommendations"):

    st.success(
        "Your preferences have been received!"
    )

    st.write("📍 Location:", location)

    st.write("⏰ Available time:", time)

    st.write("💰 Budget:", budget)

    st.write("❤️ Interests:", interests)

    if "minutes" in time:
        available_minutes = int(time.split()[0])
    else:
        available_minutes = int(time.split()[0]) * 60

    results = recommend_places(
        budget=budget,
        interests=interests,
        available_time=available_minutes
    )

    if results:

        st.subheader(
            "✨ Recommended Places for You"
        )

        st.write(
            f"Found {len(results)} matching places."
        )

        for place in results:

            with st.container(border=True):

                st.markdown(
                    f"### 📍 {place['name']}"
                )

                st.write(
                    f"🏷️ Category: {place['category']}"
                )

                st.write(
                    f"📝 {place['description']}"
                )

                st.write(
                    f"📍 Location: {place['location']}"
                )

                st.write(
                    f"💰 Price: {place['price']} KZT"
                )

                st.write(
                    f"⏰ Duration: {place['duration']} minutes"
                )

                st.write(
                    "❤️ Tags: " + ", ".join(place["tags"])
                )

    else:

        st.warning(
            "No matching places found. "
            "Try changing your preferences."
        )


st.divider()

st.caption(
    "Built by The Clique | GDG Build with AI 2026"
)