import streamlit as st
import time

# --- 1. PAGE SETUP & BIGGER FONT CONFIGURATION ---
st.set_page_config(page_title="6 Month Anniversary! ❤️", page_icon="💖", layout="centered")

# --- 2. THE DYNAMIC BACKGROUND & SCALING CSS ---
st.markdown("""
<style>
/* 1. Dynamic background gradient (Restored!) */
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

/* 2. Global scaling - Make everything bigger and informal */
[data-testid="stMarkdownContainer"] p { font-size: 1.8rem !important; font-family: 'Comic Sans MS', cursive, sans-serif; color: #5D4037;}
h1 { font-size: 5rem !important; font-family: 'Comic Sans MS', cursive, sans-serif; color: #8E242C; text-align: center;}
h2 { font-size: 3rem !important; color: #8E242C;}
h3 { font-size: 2rem !important; color: #5D4037;}

/* 3. Button scaling and styling */
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

/* 4. Expander (Collapse box) scaling */
.streamlit-expanderHeader {
    font-size: 2rem !important;
}

/* 5. Metric scaling */
[data-testid="stMetricValue"] {
    font-size: 4rem !important;
    color: #8E242C;
}

/* 6. Define the Floating Hearts Background Animation */
@keyframes float {
  0% { transform: translateY(100vh) translateX(0px); opacity: 0; }
  10% { opacity: 1; }
  90% { opacity: 1; }
  100% { transform: translateY(-100vh) translateX(100px); opacity: 0; }
}

/* Base style for a single floating heart */
.heart {
  position: fixed;
  color: rgba(229, 115, 115, 0.5); /* Semi-transparent */
  z-index: -1; /* Put behind existing Streamlit content */
  font-family: "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", "Segoe UI Symbol";
}

/* Generate multiple hearts with different sizes, starting positions, and animation delays */
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
    <div class="heart">❤️</div>
    <div class="heart">💖</div>
    <div class="heart">💓</div>
    <div class="heart">❤️</div>
    <div class="heart">💖</div>
    <div class="heart">💓</div>
    <div class="heart">❤️</div>
    <div class="heart">💖</div>
    <div class="heart">💓</div>
    <div class="heart">❤️</div>
    <div class="heart">💖</div>
    <div class="heart">💓</div>
</div>
""", unsafe_allow_html=True)

# --- 3. THE APP CONTENT ---

# Initial celebratory welcome
st.markdown("# 🥳 WELCOME! 🥳")
st.write("Ready to check out our Top Secret Boyfriend Files?")

# --- NEW PASSWORD GATE (101125) ---
password = st.text_input("Enter the secret code (Hint: Our Date)", type="password")

if password == "101125":
    start_btn = st.button("Access Granted! Click Here", key="start_btn")

    if start_btn:
        # --- TRANSITION 1: Initial Click ---
        main_placeholder = st.empty()
        
        with main_placeholder.container():
            with st.spinner('Accessing secure memory core...'):
                time.sleep(1.5)
            
            st.balloons()
            st.markdown("<h1>Our 6 Month Milestone!</h1>", unsafe_allow_html=True)
            st.markdown("---")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Days We've Kept Each Other Happy", value="183 Days", delta="Since Month 1!")
            with col2:
                st.write("Wow, look how many days we have shared together!")

            st.markdown("---")
            st.markdown("<h2>A Secret Memory 🤫</h2>", unsafe_allow_html=True)
            
            with st.expander("Click to reveal Month 3 best memory..."):
                st.write("Do you remember when we got completely lost looking for that taco place?")
                st.info("🖼️ (Put a cute photo of you guys here!)")
                
            st.markdown("---")
            st.write("Ready for the grand finale?")
            final_btn = st.button("Click for Your Surprise!", key="final_btn")

            if final_btn:
                # --- TRANSITION 2: Final Click ---
                st.toast('Loading the finale animation! Prepare for joy!')
                
                with st.spinner('Igniting celebratory engines...'):
                    time.sleep(2)
                
                st.snow() 
                st.success("WE DID IT! Can't wait for another 6 months of adventures!")
                st.balloons()
elif password != "":
    st.error("Incorrect password! Come ON u got this babe")
    
