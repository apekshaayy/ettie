import streamlit as st
import requests

st.set_page_config(page_title="Ettie Campus — Quiz", layout="wide")

st.title("Tell us about yourself")
st.write("Answer these 10 questions honestly — the more accurate, the better your matches.")

BACKEND_URL = "http://localhost:8000/api/quiz/submit/"

answers = {}

# 1. Sleep schedule
answers["sleep_schedule"] = st.radio(
    "1. Sleep schedule",
    ["Early bird", "Night owl", "Flexible"],
    horizontal=True
)

# 2. Cleanliness expectation
answers["cleanliness"] = st.slider(
    "2. Cleanliness expectation", 1, 5, 3,
    help="1 = very relaxed, 5 = very tidy"
)

# 3. Noise tolerance
answers["noise_tolerance"] = st.slider(
    "3. Noise tolerance while studying/sleeping", 1, 5, 3,
    help="1 = need silence, 5 = totally fine with noise"
)

# 4. Guest frequency
answers["guest_frequency"] = st.radio(
    "4. Guest frequency you're comfortable with",
    ["Never", "Rare", "Often", "No limit"],
    horizontal=True
)

# 5. Study style
answers["study_style"] = st.radio(
    "5. Study style",
    ["Silent focus", "Background noise ok", "Group study"],
    horizontal=True
)

# 6. Sharing philosophy
answers["sharing_philosophy"] = st.radio(
    "6. Sharing philosophy — food/supplies",
    ["Share freely", "Ask first", "Keep separate"],
    horizontal=True
)

# 7. Social expectation
answers["social_expectation"] = st.radio(
    "7. Social expectation from roommate",
    ["Close friends", "Friendly but separate", "Just cohabiting"],
    horizontal=True
)

# 8. Budget range
budget_col1, budget_col2 = st.columns(2)
with budget_col1:
    budget_min = st.number_input("8. Budget range — min (₹/month)", min_value=0, step=500, value=5000)
with budget_col2:
    budget_max = st.number_input("Budget range — max (₹/month)", min_value=0, step=500, value=10000)
answers["budget_range"] = {"min": budget_min, "max": budget_max}

# 9. Move-in timing
answers["move_in_date"] = st.date_input("9. Move-in timing")

# 10. Substance use
answers["substance_use"] = st.radio(
    "10. Substance use around shared space (smoking/drinking)",
    ["Comfortable", "Not comfortable"],
    horizontal=True
)

st.markdown("<div style='margin: 30px 0;'></div>", unsafe_allow_html=True)

# Optional free-text (for embedding-based nuance later)
extra_notes = st.text_area(
    "Anything else about your living style you'd like matches to know? (optional)",
    placeholder="e.g. I work night shifts, I have a cat, I'm a vegetarian..."
)
if extra_notes:
    answers["extra_notes"] = extra_notes

st.markdown("<div style='margin: 30px 0;'></div>", unsafe_allow_html=True)

if st.button("Get My Matches", type="primary"):
    # Convert date to string for JSON serialization
    payload_answers = dict(answers)
    payload_answers["move_in_date"] = str(answers["move_in_date"])

    with st.spinner("Finding your matches..."):
        try:
            response = requests.post(
                BACKEND_URL,
                json={"answers": payload_answers},
                timeout=10
            )
            response.raise_for_status()
            result = response.json()

            st.session_state["cumulative_score"] = result.get("cumulative_score")
            st.session_state["top_matches"] = result.get("top_matches", [])
            st.switch_page("pages/2_Matches.py")

        except requests.exceptions.ConnectionError:
            st.error("Couldn't reach the backend. Is the Django server running?")
        except requests.exceptions.RequestException as e:
            st.error(f"Something went wrong: {e}")