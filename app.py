import streamlit as st

st.set_page_config(
    page_title="ASTANA PULSE AI",
    page_icon="🏙️",
    layout="wide"
)

st.title("🏙️ ASTANA PULSE AI")

st.subheader(
    "Discover Astana with Artificial Intelligence"
)

st.write(
    "Your personal AI-powered Smart City assistant."
)

st.divider()

st.header("✨ Find Your Perfect Place")

location = st.text_input(
    "📍 Where are you now?",
    placeholder="Example: Mega Silk Way"
)

time = st.selectbox(
    "⏰ How much free time do you have?",
    [
        "30 minutes",
        "1 hour",
        "2 hours",
        "3+ hours"
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
        "Nature",
        "Museums",
        "Entertainment",
        "Shopping",
        "Culture",
        "Quiet places"
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

    st.info(
        "AI recommendations will appear here soon."
    )

st.divider()

st.caption(
    "Built by The Clique | GDG Build with AI 2026"
)