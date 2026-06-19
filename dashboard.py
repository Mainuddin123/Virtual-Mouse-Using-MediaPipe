import streamlit as st
from pathlib import Path

# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="AI Virtual Mouse",
    page_icon="🖱",
    layout="wide"
)

# =====================================
# Custom CSS
# =====================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #334155
    );
    color: white;
}

h1,h2,h3 {
    color: #f8fafc !important;
}

div[data-testid="stMetric"] {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #475569;
}

.block-container {
    padding-top: 2rem;
}

.custom-card {
    background-color: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,0.15);
    margin-bottom: 20px;
}

.footer {
    text-align: center;
    padding: 20px;
    border-radius: 15px;
    background-color: rgba(255,255,255,0.08);
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# Header
# =====================================

st.markdown("""
<h1 style='text-align:center;'>
🖱 AI Virtual Mouse
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<div class='custom-card'>
<h3>🚀 Computer Vision Project</h3>

Control your computer mouse using hand gestures with
OpenCV, MediaPipe and Python.

</div>
""", unsafe_allow_html=True)

# =====================================
# Project Overview
# =====================================

st.header("📌 Project Overview")

st.markdown("""
<div class='custom-card'>

This project uses:

- OpenCV
- MediaPipe Hand Tracking
- Gesture Recognition
- Virtual Mouse Control
- Video Recording
- Frame Capture
- Real-Time Processing

</div>
""", unsafe_allow_html=True)

# =====================================
# Supported Gestures
# =====================================

st.header("🤚 Supported Gestures")

st.markdown("""
<div class='custom-card'>

👉 Index Finger → Cursor Movement

👌 Thumb + Index Finger → Left Click

👍 Thumb + Middle Finger → Right Click

🤏 Thumb + Ring Finger → Drag

✌ Index + Middle Finger → Scroll

</div>
""", unsafe_allow_html=True)

# =====================================
# Workflow
# =====================================

st.header("⚙ Project Workflow")

st.markdown("""
<div class='custom-card'>

1️⃣ Capture Webcam Feed

2️⃣ Preprocess Frames

3️⃣ Detect Hand Landmarks

4️⃣ Recognize Gestures

5️⃣ Execute Mouse Actions

6️⃣ Save Frames

7️⃣ Record Video

8️⃣ Display Dashboard Results

</div>
""", unsafe_allow_html=True)

# =====================================
# Captured Frames
# =====================================

st.header("📸 Captured Frames")

frames = []

frame_folder = Path("captured_frames")

if frame_folder.exists():

    frames = sorted(frame_folder.glob("*.jpg"))

    st.success(
        f"Total Frames Saved: {len(frames)}"
    )

    if len(frames) > 0:

        st.image(
            str(frames[-1]),
            caption="Latest Captured Frame",
            use_container_width=True
        )

else:

    st.info(
        "Captured frames not available on cloud deployment."
    )

# =====================================
# Videos
# =====================================

st.header("🎥 Recorded Videos")

videos = []

video_folder = Path("saved_videos")

if video_folder.exists():

    videos = list(video_folder.glob("*.mp4"))

    if len(videos) > 0:

        selected_video = st.selectbox(
            "Select Video",
            [v.name for v in videos]
        )

        with open(
            video_folder / selected_video,
            "rb"
        ) as f:

            st.video(f.read())

else:

    st.info(
        "Recorded videos not available on cloud deployment."
    )

# =====================================
# Statistics
# =====================================

st.header("📊 Project Statistics")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Frames Saved",
        len(frames)
    )

with col2:
    st.metric(
        "Videos Recorded",
        len(videos)
    )

# =====================================
# Features
# =====================================

st.header("🚀 Key Features")

st.markdown("""
<div class='custom-card'>

✔ Real-Time Hand Tracking

✔ Cursor Movement

✔ Left Click Gesture

✔ Right Click Gesture

✔ Drag & Drop

✔ Scroll Control

✔ Frame Capture

✔ Video Recording

✔ Streamlit Dashboard

✔ Modular Architecture

</div>
""", unsafe_allow_html=True)

# =====================================
# Demo Video
# =====================================

demo_video = Path("refe.mp4")

if demo_video.exists():

    st.header("🎬 Demo Video")

    st.video(str(demo_video))

# =====================================
# Footer
# =====================================

st.markdown("""
<div class='footer'>

<h3>💻 Deployed By Khaja Mainuddin</h3>

<p>
Artificial Intelligence & Data Science Student
</p>

<p>
Built using Python • OpenCV • MediaPipe • Streamlit
</p>

⭐ Thank You For Visiting ⭐

</div>
""", unsafe_allow_html=True)