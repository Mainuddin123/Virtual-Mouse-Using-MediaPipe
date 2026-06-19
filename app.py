import streamlit as st
from pathlib import Path
import subprocess

# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="AI Virtual Mouse",
    page_icon="🖱",
    layout="wide"
)

# =====================================
# Header
# =====================================

st.title("🖱 AI Virtual Mouse")

st.markdown("---")

# =====================================
# Start Mouse Controller
# =====================================

if st.button("▶ Start Virtual Mouse"):
    subprocess.Popen(["python", "run_mouse.py"])
    st.success("Virtual Mouse Started")

# =====================================
# Project Overview
# =====================================

st.header("Project Overview")

st.write("""
This project uses:

- OpenCV
- MediaPipe Hand Tracking
- Gesture Recognition
- Virtual Mouse Control
- Video Recording
- Frame Capture
- Real-Time Processing
""")

# =====================================
# Supported Gestures
# =====================================

st.header("Supported Gestures")

st.write("👉 Index Finger → Cursor Movement")
st.write("👌 Thumb + Index Finger → Left Click")
st.write("👍 Thumb + Middle Finger → Right Click")
st.write("🤏 Thumb + Ring Finger → Drag")
st.write("✌ Index + Middle Finger → Scroll")

# =====================================
# Captured Frames
# =====================================

st.markdown("---")

st.header("📸 Captured Frames")

frame_folder = Path("captured_frames")

frames = []

if frame_folder.exists():

    frames = sorted(frame_folder.glob("*.jpg"))

    st.success(f"Total Frames Saved: {len(frames)}")

    if frames:
        st.image(
            str(frames[-1]),
            caption="Latest Captured Frame",
            use_container_width=True
        )
    else:
        st.warning("No frames available.")

else:
    st.warning("captured_frames folder not found.")

# =====================================
# Recorded Videos
# =====================================

st.markdown("---")

st.header("🎥 Recorded Videos")

video_folder = Path("saved_videos")

videos = []

if video_folder.exists():

    videos = list(video_folder.glob("*.mp4"))

    if videos:

        selected_video = st.selectbox(
            "Select Video",
            [v.name for v in videos]
        )

        video_path = video_folder / selected_video

        try:
            with open(video_path, "rb") as f:
                video_bytes = f.read()

            st.video(video_bytes)

        except Exception as e:
            st.error(f"Unable to load video: {e}")

    else:
        st.warning("No videos found.")

else:
    st.warning("saved_videos folder not found.")

# =====================================
# Project Statistics
# =====================================

st.markdown("---")

st.header("📊 Project Statistics")

col1, col2 = st.columns(2)

with col1:
    st.metric("Frames Saved", len(frames))

with col2:
    st.metric("Videos Recorded", len(videos))

# =====================================
# Features
# =====================================

st.markdown("---")

st.header("🚀 Features")

st.write("""
✔ Real-Time Hand Tracking

✔ Cursor Control using Index Finger

✔ Left Click Gesture

✔ Right Click Gesture

✔ Drag and Drop Gesture

✔ Scroll Gesture

✔ Frame Saving

✔ Video Recording

✔ Streamlit Dashboard

✔ Modular Project Structure
""")

# =====================================
# Footer
# =====================================

st.markdown("---")

st.success("Virtual Mouse Project Successfully Running")

st.info(
    "Click 'Start Virtual Mouse' to launch the webcam-based mouse controller."
)