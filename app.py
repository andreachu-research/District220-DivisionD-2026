"""Division D website.

Install: python -m pip install 'streamlit>=1.50,<2'
Run:     streamlit run app.py
Edit the WEBSITE SETTINGS section below to update links and pictures.
"""
from pathlib import Path
from html import escape
import base64
import mimetypes
from urllib.parse import urlparse
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent

# -----------------------------------------------------------------------------
# WEBSITE SETTINGS — edit URLs and picture paths here
# Picture paths are relative to this file (for example, "assets/photo.png").
# Put the next upcoming contest first and set "spotlight" to True.
# -----------------------------------------------------------------------------
REGISTRATION_URL = "https://docs.google.com/forms/d/e/1FAIpQLSc25lCv_WfQp8ZECcZJKUcb4y-kr4W8WQaZUv4cvGsmrH_Zsw/viewform"

CONTESTS = [
    {
        "title": "Area 43 Contest",
        "date_time": "Wed, Oct 14, 2026 | 6 – 8 pm",
        "venue": "Room 401-F at Martin Luther King Jr. Library",
        "address": "901 G St NW, Washington, DC 20001",
        "details_url": "https://www.apple.com",
        "note": "Halloween-themed Area Contest",
        "image": "assets/contest_photo.png",
        "spotlight": True,
    },
    {
        "title": "Area 44 & 45 Contest",
        "note": "",
        "date_time": "Saturday, Oct 17, 2026 | 2 –4 pm",
        "venue": "Large Meeting Room at Southwest Library",
        "address": "900 Wesley Pl SW, Washington, DC 20024",
        "details_url": "",
        "image": "assets/contest_photo.png",
        "spotlight": False,
    },
    {
        "title": "Area 41 & 42 Contest",
        "note": "",
        "date_time": "Sunday, Oct 25, 2026 | 2 – 4 pm",
        "venue": "Lower-Level Meeting Room at Cleveland Park Library",
        "address": "3310 Connecticut Ave NW, Washington, DC 20008",
        "details_url": "",
        "image": "assets/contest_photo.png",
        "spotlight": False,
    },
    {
        "title": "Division D Contest",
        "note": "",
        "date_time": "Sunday, Dec 6, 2026 | 2 – 4 pm",
        "venue": "Meeting Room 1 at Georgetown Neighborhood Library",
        "address": "3260 R St NW, Washington, DC 20007",
        "details_url": "",
        "image": "assets/contest_photo.png",
        "spotlight": False,
    },
]

COMING_SOON_ITEMS = [
    {
        "image": "assets/journey.png",
        "title": "Your One-Page Toastmasters Journey",
        "description": "Explore your goals and discover your next steps.",
        # "note": "Project Compass · Chatbot prototype",
        "note": "",
        "url": "",
    },
    {
        "image": "assets/club_map.png",
        "title": "Find a Club",
        "description": "Discover clubs that fit your location, schedule, and interests.",
        # "note": "Project Compass · Chatbot prototype",
        "note": "",
        "url": "",
    },
]
# -----------------------------------------------------------------------------

st.set_page_config(page_title="District 220 Division D | Toastmasters", page_icon="🎤", layout="centered")
st.markdown("""
<style>
.stApp {background:#fff;color:#102c46;}
.block-container {max-width:1280px;padding-top:2rem;}
h1,h2,h3 {color:#102c46;}
.banner {padding:36px 40px;border-radius:12px;color:white;margin-bottom:20px;
 background:radial-gradient(ellipse at 110% -40%,#822039 0 40%,transparent 41%),
 linear-gradient(115deg,#0c304b,#16425e);}
.banner h1 {color:white;margin:0;font-size:clamp(2.5rem,6vw,4rem);padding:0;}
.banner p {margin:0;font-size:1.35rem;color:#e4edf4;}
.badge {display:inline-block;background:#f8e8ec;color:#822039;font-size:.8rem;
 font-weight:700;border-radius:8px;padding:7px 12px;margin-bottom:10px;}
.subtitle {color:#596679;font-size:1.15rem;margin-bottom:20px;}
.art {background:#eef4f9;border-radius:10px;padding:28px;font-size:3rem;
 text-align:center;margin-bottom:14px;}
.contest-grid {display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px;}
.contest-card {border:1px solid #dde2e8;border-radius:12px;padding:16px;display:flex;flex-direction:column;}
.contest-card.spotlight {border:2px solid #822039;}
.contest-card img {width:100%;height:180px;object-fit:cover;border-radius:8px;}
.contest-card h3 {font-size:1.35rem;margin:14px 0;}
.contest-card .contest-note {color:#822039;font-size:.95rem;font-weight:600;margin:-7px 0 8px;}
.contest-card p {color:#596679;margin:6px 0;}
.contest-card .venue-address {display:block;margin:3px 0 0 1.55rem;font-size:.9rem;}
.card-details {display:block;text-align:center;margin-top:12px;color:#10344e;}
.card-details.disabled {color:#737c89;}
.card-links {margin-top:auto;padding-top:10px;}
@media(max-width:1000px) {.contest-grid {grid-template-columns:repeat(2,minmax(0,1fr));}}
@media(max-width:600px) {.contest-grid {grid-template-columns:1fr;}}
.footer {background:#10344e;color:white;text-align:center;padding:18px;
 border-radius:8px;margin-top:32px;font-size:.9rem;}
button[role="tab"] {font-weight:600;font-size:1rem;}
button[role="tab"][aria-selected="true"] {color:#822039;}
[data-baseweb="tab-highlight"] {background:#822039;}
[data-testid="stLinkButton"] a[kind="primary"] {background:#822039;border-color:#822039;color:white;}
@media(max-width:600px) {.banner {padding:26px;} .block-container {padding:1rem;}}
</style>
<div class="banner"><h1>District 220 Division D</h1><p>Toastmasters</p></div>
""", unsafe_allow_html=True)

def badge(text):
    st.markdown(f'<span class="badge">{escape(text)}</span>', unsafe_allow_html=True)

def card_link(label, url, css):
    parsed = urlparse(url)
    if parsed.scheme in {"http", "https"} and parsed.netloc:
        return f'<a class="{css}" href="{escape(url, quote=True)}" target="_blank" rel="noopener noreferrer">{escape(label)}</a>'
    return f'<span class="{css} disabled" aria-disabled="true">{escape(label)}</span>'


def contest_card(contest):
    image = BASE_DIR / contest["image"]
    mime = mimetypes.guess_type(image.name)[0] or "image/png"
    encoded = base64.b64encode(image.read_bytes()).decode("ascii")
    spotlight = contest["spotlight"]
    badge_html = '<span class="badge">CONTEST SPOTLIGHT</span>' if spotlight else ''
    details = card_link("View Contest Details", contest["details_url"], "card-details")
    note = contest.get("note", "")
    note_html = f'<p class="contest-note">{escape(note)}</p>' if note else ""
    address = contest.get("address", "")
    address_html = f'<span class="venue-address">{escape(address)}</span>' if address else ""
    return f'''<article class="contest-card {'spotlight' if spotlight else ''}">
    {badge_html}<img src="data:{mime};base64,{encoded}" alt="Speaker at a library event">
    <h3>{escape(contest['title'])}</h3>{note_html}
    <p>📅 {escape(contest['date_time'])}</p>
    <p>📍 {escape(contest['venue'])}{address_html}</p>
    <div class="card-links">{details}</div></article>'''

contests, coming_soon = st.tabs(["Table Topics Contests", "Coming Soon"])

with contests:
    heading, registration = st.columns([4, 1], vertical_alignment="center")
    with heading:
        st.header("Table Topics Contests")
    with registration:
        st.link_button("Register Now", REGISTRATION_URL, type="primary", width="stretch")
    st.markdown(
        '<p class="subtitle">Admission is free, and walk-ins are welcome. '
        'Sign up for event updates or volunteer opportunities.</p>',
        unsafe_allow_html=True,
    )
    cards = "".join(contest_card(contest) for contest in CONTESTS)
    st.markdown(f'<div class="contest-grid">{cards}</div>', unsafe_allow_html=True)

with coming_soon:
    st.header("Your next chapter starts here")
    st.markdown('<p class="subtitle">Two new ways to explore Toastmasters.</p>', unsafe_allow_html=True)
    for item in COMING_SOON_ITEMS:
        with st.container(border=True):
            illustration, copy = st.columns([1, 1.2])
            with illustration:
                st.image(str(BASE_DIR / item["image"]), width="stretch")
            with copy:
                badge("COMING SOON")
                st.subheader(item["title"])
                st.write(item["description"])
                if item["note"]:
                    st.caption(item["note"])
                if item["url"]:
                    st.link_button("Learn More", item["url"])

st.markdown('<div class="footer">Division D · Connect, participate, and grow.</div>', unsafe_allow_html=True)
