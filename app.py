import streamlit as st
import time
from datetime import datetime
import streamlit.components.v1 as components
import base64
import os
import json

# --- 1. PAGE SETUP & BIGGER FONT CONFIGURATION ---
st.set_page_config(page_title="my little surprise for you", page_icon="💖", layout="centered")

# --- 2. THE DYNAMIC BACKGROUND & SCALING CSS ---
st.markdown("""
<style>
/* Dynamic background gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(-45deg, #ff9a9e, #fecfef, #ff9a9e, #fecfef);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}

@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Global scaling */
[data-testid="stMarkdownContainer"] p { font-size: 1.8rem !important; font-family: 'Comic Sans MS', cursive, sans-serif; color: #5D4037;}
h1 { font-size: 5rem !important; font-family: 'Comic Sans MS', cursive, sans-serif; color: #8E242C; text-align: center;}
h2 { font-size: 3rem !important; color: #8E242C; text-align: center;}
h3 { font-size: 2rem !important; color: #5D4037;}

/* Button scaling and styling */
.stButton>button {
    font-size: 2.2rem !important;
    padding: 15px 40px !important;
    border-radius: 50px !important;
    background-color: #E57373 !important;
    color: white !important;
    border: 2px solid white !important;
    font-family: 'Comic Sans MS', cursive, sans-serif;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background-color: #EF5350 !important;
    transform: translateY(-4px) scale(1.05);
    box-shadow: 0px 6px 15px rgba(0,0,0,0.2) !important;
}

/* Expander scaling */
.streamlit-expanderHeader {
    font-size: 2rem !important;
}

/* Floating Hearts Background Animation */
@keyframes float {
  0% { transform: translateY(100vh) translateX(0px); opacity: 0; }
  10% { opacity: 1; }
  90% { opacity: 1; }
  100% { transform: translateY(-100vh) translateX(100px); opacity: 0; }
}

.heart {
  position: fixed;
  color: rgba(229, 115, 115, 0.5); 
  z-index: -1; 
  font-family: "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", "Segoe UI Symbol";
}

.heart:nth-child(1) { font-size: 25px; left: 10%; animation: float 20s linear infinite; animation-delay: 0s; }
.heart:nth-child(2) { font-size: 40px; left: 25%; animation: float 25s linear infinite; animation-delay: 2s; }
.heart:nth-child(3) { font-size: 30px; left: 40%; animation: float 18s linear infinite; animation-delay: 4s; }
.heart:nth-child(4) { font-size: 50px; left: 55%; animation: float 22s linear infinite; animation-delay: 6s; }
.heart:nth-child(5) { font-size: 35px; left: 70%; animation: float 28s linear infinite; animation-delay: 1s; }
.heart:nth-child(6) { font-size: 45px; left: 85%; animation: float 15s linear infinite; animation-delay: 3s; }
.heart:nth-child(7) { font-size: 28px; left: 15%; animation: float 21s linear infinite; animation-delay: 5s; }
.heart:nth-child(8) { font-size: 42px; left: 30%; animation: float 24s linear infinite; animation-delay: 7s; }
.heart:nth-child(9) { font-size: 33px; left: 45%; animation: float 19s linear infinite; animation-delay: 2s; }
.heart:nth-child(10) { font-size: 55px; left: 60%; animation: float 23s linear infinite; animation-delay: 4s; }
.heart:nth-child(11) { font-size: 38px; left: 75%; animation: float 27s linear infinite; animation-delay: 6s; }
.heart:nth-child(12) { font-size: 48px; left: 90%; animation: float 16s linear infinite; animation-delay: 1s; }
</style>

<div class="heart-container">
    <div class="heart">❤️</div><div class="heart">💖</div><div class="heart">💓</div>
    <div class="heart">❤️</div><div class="heart">💖</div><div class="heart">💓</div>
    <div class="heart">❤️</div><div class="heart">💖</div><div class="heart">💓</div>
    <div class="heart">❤️</div><div class="heart">💖</div><div class="heart">💓</div>
</div>
""", unsafe_allow_html=True)

# --- HELPER FUNCTION FOR SLIDESHOW ---
def get_base64_image(file_name):
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

# --- 3. THE TIME LOCK LOGIC WITH LIVE TICKING COUNTDOWN & BACKDOOR ---

UNLOCK_DATE = datetime(2026, 5, 10, 0, 0, 0)
current_time = datetime.now()

is_developer = st.query_params.get("dev") == "admin"

if current_time < UNLOCK_DATE and not is_developer:
    st.markdown("<h1>⏳ Top Secret Files ⏳</h1>", unsafe_allow_html=True)
    st.markdown("<h2>Access is currently locked.</h2>", unsafe_allow_html=True)
    
    countdown_html = """
    <style>
    body {
        margin: 0; display: flex; justify-content: center; align-items: center;
        font-family: 'Comic Sans MS', cursive, sans-serif; color: #8E242C;
    }
    .countdown-container { display: flex; gap: 15px; text-align: center; }
    .time-box {
        background: rgba(255, 255, 255, 0.6); padding: 15px 20px;
        border-radius: 15px; border: 2px solid white;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1); width: 80px;
    }
    .number { font-size: 3rem; font-weight: bold; }
    .label { font-size: 1rem; color: #5D4037; margin-top: 5px; font-weight: bold;}
    </style>
    
    <div class="countdown-container">
        <div class="time-box"><div class="number" id="days">--</div><div class="label">DAYS</div></div>
        <div class="time-box"><div class="number" id="hours">--</div><div class="label">HOURS</div></div>
        <div class="time-box"><div class="number" id="mins">--</div><div class="label">MINS</div></div>
        <div class="time-box"><div class="number" id="secs">--</div><div class="label">SECS</div></div>
    </div>
    
    <script>
    var countDownDate = new Date("May 10, 2026 00:00:00").getTime();
    var x = setInterval(function() {
      var now = new Date().getTime();
      var distance = countDownDate - now;

      var days = Math.floor(distance / (1000 * 60 * 60 * 24));
      var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((distance % (1000 * 60)) / 1000);

      document.getElementById("days").innerHTML = days;
      document.getElementById("hours").innerHTML = hours;
      document.getElementById("mins").innerHTML = minutes;
      document.getElementById("secs").innerHTML = seconds;

      if (distance < 0) {
        clearInterval(x);
        document.querySelector(".countdown-container").innerHTML = "<h2>Time's up! Refresh the page! 🎉</h2>";
      }
    }, 1000);
    </script>
    """
    
    components.html(countdown_html, height=180)
    st.markdown("<p style='text-align: center;'>No peeking early! Check back when the clock strikes midnight. 💖</p>", unsafe_allow_html=True)
    st.stop()


# --- 4. THE APP CONTENT ---

st.markdown("# 🥳 WELCOME! 🥳")
st.write("Ready to check out our Top Secret Boyfriend Files?")

password = st.text_input("Enter the secret code (Hint: Our Date)", type="password")

if password == "101125":
    start_btn = st.button("Access Granted! Click Here", key="start_btn")

    if start_btn:
        main_placeholder = st.empty()
        
        with main_placeholder.container():
            with st.spinner('Accessing secure memory core...'):
                time.sleep(1.5)
            
            st.balloons()
            st.markdown("<h1>Our 6 Month Milestone!</h1>", unsafe_allow_html=True)
            st.markdown("---")
            
            # --- CREATING THE TWO TABS ---
            tab_story, tab_gallery = st.tabs(["🕰️ Our Story", "📸 Full Gallery"])
            
            # === TAB 1: THE STORY & SLIDESHOW ===
            with tab_story:
                st.markdown("<h2>The Early Days</h2>", unsafe_allow_html=True)
                st.write("Back when we spent half our lives PBL...")
                st.image("starting days.jpeg", caption="Where it all began ❤️", use_container_width=True) 
                
                st.markdown("---")
                st.markdown("<h2>A Secret Memory 🤫</h2>", unsafe_allow_html=True)
                
                with st.expander("Click to reveal..."):
                    st.write("Our late-night Discord calls were the best part of my day.")
                    st.image("discord 1.jpeg", caption="😂", use_container_width=True) 
                    
                st.markdown("---")
                st.markdown("<h2>Right Now 💖</h2>", unsafe_allow_html=True)
                st.write("Half a year down, and I'm looking forward to everything coming next.")
                st.image("us .jpeg", caption="Us.", use_container_width=True)

                st.markdown("---")
                st.markdown("<h2>🎬 Memory Reel 🎬</h2>", unsafe_allow_html=True)
                st.write("A quick look back at all the smiles...")
                
                # Setup the images for the slideshow
                gallery_images = [
                    "video call SS 1.jpeg", "her 1.jpeg", "her smile 3.jpeg", "selfie 3.jpeg", "she kiss me.jpeg",
                    "discord 2.jpeg", "discord 4.jpeg", "her eyes 1.jpeg", "selfie 1.jpeg", "selfie 4.jpeg", "her smile.jpeg",
                    "discord 3.jpeg", "her smile 2.jpeg", "me kiss her.jpeg", "selfie 2.jpeg", "selfie 5.jpeg"
                ]
                
                # Convert images to base64 so HTML can read them
                b64_imgs = [f"data:image/jpeg;base64,{get_base64_image(img)}" for img in gallery_images if get_base64_image(img)]
                
                if b64_imgs:
                    slideshow_html = f"""
                    <div style="display: flex; justify-content: center; width: 100%;">
                        <img id="slideshow-img" src="{b64_imgs[0]}" style="width: 100%; max-width: 450px; height: 500px; object-fit: cover; border-radius: 15px; border: 3px solid white; box-shadow: 0px 4px 15px rgba(0,0,0,0.2); transition: opacity 0.5s ease-in-out;">
                    </div>
                    <script>
                        var images = {json.dumps(b64_imgs)};
                        var i = 0;
                        var imgElem = document.getElementById("slideshow-img");
                        setInterval(function() {{
                            imgElem.style.opacity = 0; // fade out
                            setTimeout(function() {{
                                i = (i + 1) % images.length;
                                imgElem.src = images[i];
                                imgElem.style.opacity = 1; // fade in
                            }}, 500);
                        }}, 3000); // Change image every 3 seconds
                    </script>
                    """
                    components.html(slideshow_html, height=550)
                else:
                    st.write("(Upload your images to GitHub to see the slideshow!)")

                st.markdown("---")
                st.write("Ready for the grand finale?")
                final_btn = st.button("Click for Your Surprise!", key="final_btn")

                if final_btn:
                    st.toast('Loading the finale animation! Prepare for joy!')
                    
                    with st.spinner('Igniting celebratory engines...'):
                        time.sleep(2)
                    
                    st.snow() 
                    st.success("WE DID IT! Can't wait for another 6 months of adventures!")
                    st.balloons()
            
            # === TAB 2: THE FULL GALLERY GRID ===
            with tab_gallery:
                st.markdown("<h2>📸 All Our Memories 📸</h2>", unsafe_allow_html=True)
                st.write("Take your time looking through all of them here.")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.image("video call SS 1.jpeg", use_container_width=True)
                    st.image("her 1.jpeg", use_container_width=True)
                    st.image("her smile 3.jpeg", use_container_width=True)
                    st.image("selfie 3.jpeg", use_container_width=True)
                    st.image("she kiss me.jpeg", use_container_width=True)
                with col2:
                    st.image("discord 2.jpeg", use_container_width=True)
                    st.image("discord 4.jpeg", use_container_width=True)
                    st.image("her eyes 1.jpeg", use_container_width=True)
                    st.image("selfie 1.jpeg", use_container_width=True)
                    st.image("selfie 4.jpeg", use_container_width=True)
                    st.image("her smile.jpeg", use_container_width=True)
                with col3:
                    st.image("discord 3.jpeg", use_container_width=True)
                    st.image("her smile 2.jpeg", use_container_width=True)
                    st.image("me kiss her.jpeg", use_container_width=True)
                    st.image("selfie 2.jpeg", use_container_width=True)
                    st.image("selfie 5.jpeg", use_container_width=True)

elif password != "":
    st.error("Incorrect password! Think harder! 😂")
