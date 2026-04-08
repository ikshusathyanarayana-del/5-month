import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(page_title="Happy 5 Months!", page_icon="❤️", layout="centered")

# --- THE UPGRADED MAGIC CSS ---
st.markdown("""
<style>
/* 1. Background gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
}

/* 2. Make the very top header bar red */
[data-testid="stHeader"] {
    background-color: #ff3366;
}

/* 3. Change all text to a dark burgundy so it's readable */
h1, h2, h3, p, .stMarkdown {
    color: #800020 !important; 
}

/* 4. Beautiful, animated buttons */
div[data-testid="stButton"] button {
    background-color: #ff3366;
    color: white !important;
    border-radius: 30px;
    border: 2px solid white;
    padding: 10px 24px;
    font-weight: bold;
    transition: all 0.3s ease; /* Smooth animation */
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}

/* 5. Button Hover Animation - makes it pop up */
div[data-testid="stButton"] button:hover {
    transform: translateY(-4px) scale(1.05);
    background-color: #ff1a53;
    box-shadow: 0px 6px 15px rgba(0,0,0,0.2);
}

/* 6. Make the success box semi-transparent white */
[data-testid="stNotification"] {
    background-color: rgba(255, 255, 255, 0.8) !important;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)


# 2. The Password Gate
st.markdown("### 🔒 Top Secret Boyfriend Files")
password = st.text_input("What is our secret word?", type="password")

if password.lower() == "pizza":
    
    # Trigger celebration!
    st.balloons()
    
    # Centered Title
    st.markdown("<h1 style='text-align: center;'>❤️ Happy 5 Months! ❤️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2em;'>I built this little website just to say I love you.</p>", unsafe_allow_html=True)
    
    st.divider()

    # --- TABS TO FIX SCROLLING ---
    # This creates three clickable tabs at the top! No more scrolling!
    tab1, tab2, tab3 = st.tabs(["🕰️ Our Story", "💌 Love Notes", "✨ Cosmic Match"])

    with tab1:
        st.header("Follow the timeline ➔")
        
        st.subheader("Month 1: The Beginning 💘")
        st.write("Do you remember our first date? I was so nervous but...")
        st.info("🖼️ (Put a cute photo of you guys here!)")
        
        st.write("⬇️") # Arrow guiding down
        
        st.subheader("Months 2-4: The Adventures 🏹")
        with st.expander("Click here for a secret memory 🤫"):
            st.write("Remember that time we got lost? Best detour ever.")
            
        st.write("⬇️") # Arrow guiding down

        st.subheader("Month 5: Right Now 💖")
        st.write("Five months in and I'm looking forward to everything coming next.")

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
            # Adds a tiny loading animation before showing the text
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
