# app.py

import streamlit as st
from datetime import date
import folium
from streamlit_folium import st_folium
import streamlit.components.v1 as components
from base64 import b64encode
import base64

# --- Background Image ---
# --- Background Image ---
st.set_page_config(page_title="A Journey of Us 💑", page_icon="💖", layout="wide")

# 
st.markdown("""
    <style>
    @keyframes floatUpDisappear {
        0% {
            bottom: -100px;
            opacity: 0;
            transform: translateX(-50%) scale(0.5);
        }
        10% {
            opacity: 1;
            transform: translateX(-50%) scale(1.2);
        }
        100% {
            bottom: 120%;
            opacity: 0;
            transform: translateX(-50%) scale(0.8);
        }
    }

    .floating-heart {
        position: fixed;
        bottom: -100px;
        left: 50%;
        font-size: 500px;
        color: #ff4d6d;
        z-index: 9999;
        pointer-events: none;
        animation: floatUpDisappear 5s ease-in-out forwards;
    }
    </style>

    <div class="floating-heart">❤️</div>
""", unsafe_allow_html=True)


def set_background(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# --- Page Config ---
set_background("imageonline-co-brightnessadjusted.jpg")

# Page config



# Centered CSS + full layout control
st.markdown("""
    <style>
        body {
            text-align: center;
        }
        .centered-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem;
            text-align: center;
        }

        .stApp {
            text-align: center;
        }

        .stMarkdown, .stText, .stSubheader, .stTitle, .stCaption {
            text-align: center !important;
        }

        .stSlider > label, .stButton > button {
            margin-left: auto;
            margin-right: auto;
        }

        .stAudio, .stVideo {
            display: flex;
            justify-content: center;
        }

        /* Text color for dark background */
        .stApp, .stMarkdown, .stText, .stSubheader, .stTitle, .stCaption, p, div {
            color: #f0f0f0 !important;
        }

        a {
            color: #a8d0e6 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("💖 A Journey of Us 💑")
st.markdown("---")

# Love Letter
st.subheader("💌 A Love Letter")
st.markdown("""
<div class="centered-container">
<p>
Dear <strong>Babling 💖</strong>,<br><br>

From the moment our paths crossed, you've been the light of my life.<br>
Every day with you is a chapter in the most beautiful story I could ever imagine.<br>
This little app is a glimpse into our journey — the smiles, the memories, the love. 💕<br><br>

With all my heart,<br>
<strong>Subhayan 💖</strong>
</p>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# Auto Image Slideshow
st.subheader("📸 Our Memories")

photo_files = [
    ("valentine.jpg", "First Valentine 💘"),
    ("victoria.jpg", "Trip to Victoria Memorial 🌸"),
    ("goofy_selfie.jpg", "Goofy Selfies 😝"),
    ("holi_together.jpg", "Special Holi Moment 🌈🎨"),
    ("official meet with kakima.jpg", "Official Meet with Kakima 🤝"),
    ("dada bday celeb.jpg", "Dada's Birthday Celebration 🎂🎉"),
    ("ganga ghat.jpg", "Ganga Ghat Visit 🌊🌅")
]

encoded_images = []
captions = []

for img_path, caption in photo_files:
    try:
        with open(img_path, "rb") as img_file:
            img_bytes = img_file.read()
            img_base64 = b64encode(img_bytes).decode("utf-8")
            encoded_images.append(f"data:image/jpeg;base64,{img_base64}")
            captions.append(caption)
    except FileNotFoundError:
        st.error(f"Image not found: {img_path}")

if encoded_images:

    # Convert Python lists to JS arrays as strings with quotes
    js_images = "[" + ",".join([f'"{img}"' for img in encoded_images]) + "]"
    js_captions = "[" + ",".join([f'"{cap}"' for cap in captions]) + "]"

    html_code = f"""
    <div style="display: flex; flex-direction: column; align-items: center;">
        <img id="slideshow" src={encoded_images[0]}
             style="max-width: 400px; width: 90%; height: auto; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);"/>
        <p id="caption" style="font-size: 17px; font-weight: bold; margin-top: 8px; color: #444; text-align: center;">
            {captions[0]}
        </p>
    </div>

    <script>
        const images = {js_images};
        const captions = {js_captions};
        let index = 0;
        setInterval(() => {{
            index = (index + 1) % images.length;
            document.getElementById("slideshow").src = images[index];
            document.getElementById("caption").textContent = captions[index];
        }}, 3000);
    </script>
    """

    components.html(html_code, height=600)


# Map of Places



# Create folium map centered around Kolkata

# Create folium map centered around Kolkata
# Map Section
st.subheader("🗺️ Places We've Been")

# Create and populate the map
m = folium.Map(location=[22.54, 88.35], zoom_start=13, control_scale=True)

# Add your markers
folium.Marker([22.5448, 88.3426], popup="Victoria Memorial 🌸", tooltip="Victoria Memorial",
              icon=folium.Icon(color="red", icon="heart")).add_to(m)

folium.Marker([22.5284, 88.3340], popup="Botanical Garden 🌿", tooltip="Botanical Garden",
              icon=folium.Icon(color="green", icon="leaf")).add_to(m)

folium.Marker([22.5121, 88.3637], popup="Rabindra Sarobar 🌅", tooltip="Rabindra Sarobar",
              icon=folium.Icon(color="purple", icon="star")).add_to(m)

folium.Marker([22.5006, 88.3598], popup="South City Mall 🛍️", tooltip="South City Mall",
              icon=folium.Icon(color="blue", icon="shopping-cart")).add_to(m)

folium.Marker([22.5647, 88.3387], popup="Ganga Ghat 🌊", tooltip="Ganga Ghat",
              icon=folium.Icon(color="cadetblue", icon="tint")).add_to(m)

# Display the map with proper height
with st.container():
    st_folium(m, use_container_width=True, height=700)

# Mobile height fix
st.markdown("""
<style>
/* Ensure iframe height on all devices */
iframe[title="streamlit_folium.st_folium"] {
    height: 700px !important;
    width: 100% !important;
    border: none;
}
@media only screen and (max-width: 600px) {
    iframe[title="streamlit_folium.st_folium"] {
        height: 600px !important;
    }
}
</style>
""", unsafe_allow_html=True)


# Add optional content to fill space & make it feel complete

st.markdown("📸 Stay tuned for more memories and adventures...")

# Optional: Reduce default Streamlit padding
st.markdown("""
    <style>
        .block-container {
            padding-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)
st.markdown("---")
# Timeline
st.subheader("🗓️ Our Love Timeline")
timeline = {
    "2025-01-06": "💘 We met for the first time",
    "2025-02-10": "🌆 First official outing",
    "2025-02-14": "🌸 First Valentine Together",
    "2025-02-15": "💍 First Proposal",
    "2025-02-19": "🌿 Rabindra Sarobar visit",
    "2025-03-03": "💝 Date in Southcity",
    "2025-03-11": "🎨🎄 First Holi",
    "2025-03-25": "🌺 Botanical Garden visit",
    "2025-05-05": "👩‍❤️‍👨 Kamolika didi meet with us",
    "2025-05-10": "🏛️ Jorasanko visit",
    "2025-06-05": "🌊 Ganga Ghat visit",
    "2025-06-22": "👗👕 First twinning dress",
    "2025-06-23": "🎂 Dada bday celebration",
    "2025-06-27": "👩‍👩‍👦 First official outing with Kakima",
    "2025-07-22": "🎬🍿 First movie date"
}

for d, event in sorted(timeline.items()):
    st.markdown(f"**{d}** — {event}")

st.markdown("---")

# Playlist
st.subheader("🎶 Our Songs")
st.markdown("""
- **Perfect** — Ed Sheeran  
- **Can't Help Falling in Love** — Elvis Presley  
- **All of Me** — John Legend  
""")
st.audio("ED SHEERAN - Perfect (Lyrics)  Well, I found a girl, beautiful and sweet.mp3", format="audio/mp3")
st.markdown("---")

# Video
st.subheader("🎥 A Video Just for You")
st.markdown("Here's something special I made with all my heart...")

try:
    video_file = open('VID-20250523-WA0011.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
except FileNotFoundError:
    st.warning("Video file not found. Please place your video in the 'videos' folder.")
st.markdown("---")

# Surprise
st.subheader("🎁 A Special Surprise")
if st.button("Click to Reveal"):
    st.balloons()
    st.success("You are the best part of my every day. ❤️ I love you.")

# Footer
st.markdown("---")
st.caption("Made with ❤️ love by [Sonai ❤️]")
