import streamlit as st
import os

st.set_page_config(page_title="Ettie Campus", layout="wide")

def header():
    col_logo, col_nav = st.columns([1, 4])

    with col_logo:
        st.image("assets/logo.svg", width=140)

    with col_nav:
        st.markdown("""
        <div class="nav-links">
            <a href="#home">Home</a>
            <a href="#about">About Us</a>
            <a href="#how-it-works">How It Works</a>
            <a href="#process">Process</a>
            <a href="https://github.com/apekshaayy" target="_blank">GitHub</a>
        </div>
        <style>
        .nav-links a {
            margin-left: 150px;
            text-decoration: none;
            color: black;
            font-size: 15px;
        }
        </style>
        """, unsafe_allow_html=True)

header()

st.set_page_config(page_title="Ettie Campus", layout="wide")
st.title("Looking for a roommate?")
st.write("Ettie Campus made it easier to find someone you'll actually enjoy living with.")
if st.button("Start Matching"):
    st.write("Quiz yet to be uploaded.")

st.markdown("<div style='margin: 50px 0;'></div>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:left;'>About Us</h2>", unsafe_allow_html=True)
st.write("At Ettie Campus, we believe that good roommates make great college memories. Browse verified student profiles, match by lifestyle, and connect before moving in. Find roommates, not randoms.")

st.markdown("<div style='margin: 50px 0;'></div>", unsafe_allow_html=True)

def how_it_works():
    st.markdown("<div id='how-it-works'></div>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>How It Works</h2>", unsafe_allow_html=True)
    steps = [
        {"img": "assets/photo1.jpg", "text": "Answer 10 questions and let us know about your preferences."},
        {"img": "assets/photo1.jpg", "text": "Get profiles of similar students on your campus."},
        {"img": "assets/photo1.jpg", "text": "Swipe right to match - just like the dating apps."},
        {"img": "assets/photo1.jpg", "text": "Once you match, share contacts, connect, and get yourself your roommate."},        
    ]

    cols = st.columns(4)
    for col, step in zip(cols, steps):
        with col:
            st.image(step["img"], use_container_width=True)
            st.markdown(f"<p class='step-text'>{step['text']}</p>", unsafe_allow_html=True)


def my_process():
    st.markdown('<div id="process"></div>', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>My Process</h2>", unsafe_allow_html=True)

    left, right = st.columns([1,1])

    with left:
        st.write("Know more about how I came up with Ettie Campus and what's next. Stay updated and maybe buy me a coffee :)")

    with right:
        row1_col1, row1_col2 = st.columns(2)
        with row1_col1:
            if st.button("Download Slides"):
                st.write("Coming up soon!")
        with row1_col2:
            st.link_button("Substack", "https://yoursubstack.com")

        row2_col1, row2_col2 = st.columns(2)
        with row2_col1:
            st.link_button("Portfolio", "https://tan-sovereign-0a6.notion.site/Portfolio-Apekshaa-Yadav-2bbb8958732580b1a30ae95f7a92a92b")
        with row2_col2:
            with open("assets/resume.pdf", "rb") as f:
                st.download_button("Download Resume", f, file_name="Apekshaa-Yadav-Resume.pdf")


def footer():
    st.image("assets/made-w-love.svg")

how_it_works()
st.markdown("<div style='margin: 50px 0;'></div>", unsafe_allow_html=True)
my_process()
st.markdown("<div style='margin: 50px 0;'></div>", unsafe_allow_html=True)
st.markdown("<div style='margin: 50px 0;'></div>", unsafe_allow_html=True)
footer()