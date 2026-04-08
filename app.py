import streamlit as st
import random
import time

# 1. Page Configuration (Updated to 6 Months)
st.set_page_config(page_title="Happy 6 Months!", page_icon="❤️", layout="centered")

# --- THE MAGIC CSS WITH DYNAMIC BACKGROUND AND STYLIZED ARROWS ---
st.markdown("""
<style>
/* 1. Dynamic background gradient */
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

/* 2. Red header bar */
[data-testid="stHeader"] {
    background-color: #ff3366;
}

/* 3. Text color */
h1, h2, h3, p, .stMarkdown {
    color: #800020 !important; 
}

/* 4. Beautiful buttons */
div[data-testid="stButton"] button {
    background-color: #ff3366;
    color: white !important;
    border-radius: 30px;
    border: 2px solid white;
    padding: 10px 24px;
    font-weight: bold;
    transition: all 0.3s ease;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}

/* Button Hover Animation */
div[data-testid="stButton"] button:hover {
    transform: translateY(-4px) scale(1.05);
    background-color: #ff1a53;
    box-shadow: 0px 6px 15px rgba(0,0,0,0.2);
}

/* 5. The Heartbeat Animation */
@keyframes heartbeat {
  0% { transform: scale(1); }
  14% { transform: scale(1.3); }
  28% { transform: scale(1); }
  42% { transform: scale(1.3); }
  70% { transform: scale(1); }
}

.beating-heart {
    font-size: 120px;
    text-align: center;
    animation: heartbeat 1.5s infinite;
    margin-top: -20px;
    margin-bottom: 20px;
}

/* 6. The Stylized Curly Arrows */
@keyframes wiggle {
    0% { transform: rotate(0deg); }
    25% { transform: rotate(5deg); }
    50% { transform: rotate(0deg); }
    75% { transform: rotate(-5deg); }
    100% { transform: rotate(0deg); }
}

.curly-arrow {
    font-size: 80px;
    text-align: center;
    color: #ff3366;
    margin: -10px 0;
    display: flex;
    justify-content: center;
    align-items: center;
    animation: wiggle 3s infinite ease-in-out;
}
</style>
""", unsafe_allow_html=True)


# 2. The Password Gate
st.markdown("### 🔒 Top Secret Boyfriend Files")
password = st.text_input("What is our secret word?", type="password")

# Remember to change "pizza" to your actual inside joke!
if password.lower() == "pizza":
    
    # Trigger celebration!
    st.balloons()
    
    # The Big Animated Heart
    st.markdown('<div class="beating-heart">❤️</div>', unsafe_allow_html=True)
    
    # Centered Title (Updated to 6 Months)
    st.markdown("<h1 style='text-align: center;'>Happy 6 Months!</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2em;'>I built this little website just to say I love you.</p>", unsafe_allow_html=True)
    
    st.divider()

    # --- THE TABS ---
    tab1, tab2, tab3 = st.tabs(["🕰️ Our Story", "💌 Love Notes", "✨ Cosmic Match"])

    with tab1:
        st.header("Follow the timeline ➔")
        
        st.subheader("Month 1: The Beginning 💘")
        st.write("Do you remember our first date? I was so nervous but...")
        # st.image("month_1.jpg", caption="Our first picture!")
        st.info("🖼️ (Put a cute photo of you guys here!)")
        
        # New Giant Wiggling Arrow
        st.markdown('<div class="curly-arrow">➥</div>', unsafe_allow_html=True)
        
        st.subheader("Months 2-5: The Adventures 🏹")
        with st.expander("Click here for a secret memory 🤫"):
            st.write("Remember that time we got lost? Best detour ever.")
            
        # New Giant Wiggling Arrow
        st.markdown('<div class="curly-arrow">➥</div>', unsafe_allow_html=True)

        st.subheader("Month 6: Right Now 💖")
        st.write("Half a year down, and I'm looking forward to everything coming next.")

    with tab2:
        st.header("💌 5 Reasons I Love You")
        st.write("Click the button below to see a random reason!")
        
        reasons = [
            "Your beautiful smile.",
            "How we can laugh at the dumbest things.",
            "The way you support me.",
            "Every single date we've been on.",
            "Just being you."
        ]
        
        if st.button("Click for a reason! 💌"):
            with st.spinner("Finding the perfect reason..."):
                time.sleep(0.8) 
            st.success(random.choice(reasons))

    with tab3:
        st.header("✨ Our Cosmic Compatibility")
        st.write("I ran the astrological charts and analyzed our palm lines...")
        
        if st.button("Calculate Match Score 🔭"):
            st.snow()
            st.metric(label="Final Score", value="100%", delta="Written in the stars! 🌠")

    st.divider()
    st.write("Made with ❤️ by me.")

elif password:
    st.error("Access Denied! Think harder! 😂")
