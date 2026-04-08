import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(page_title="Happy 5 Months!", page_icon="❤️")

# --- THE MAGIC COLOR CODE ---
# This adds a soft pink/red gradient background and makes the text a dark romantic burgundy
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
}
h1, h2, h3, p, .stMarkdown {
    color: #800020; 
}
</style>
""", unsafe_allow_html=True)


# 2. The Password Gate
st.markdown("### 🔒 Top Secret Boyfriend Files")
password = st.text_input("What is our secret word?", type="password")

if password.lower() == "pizza":
    
    # Trigger celebration!
    st.balloons()
    
    st.title("Happy 5 Months! ❤️")
    st.write("I built this little website just to say I love you and look back at our story so far.")
    
    st.divider()

    # --- INTERACTIVE FEATURE 1: Random Reason Generator ---
    st.header("💌 5 Reasons I Love You")
    st.write("Click the button below to see a random reason!")
    
    # You can change these quotes to whatever you want!
    reasons = [
        "Your beautiful smile.",
        "How we can laugh at the dumbest things.",
        "The way you support me.",
        "Every single date we've been on.",
        "Just being you."
    ]
    
    if st.button("Click for a reason!"):
        st.success(random.choice(reasons))

    st.divider()

    # --- INTERACTIVE FEATURE 2: The Cosmic Calculator ---
    st.header("✨ Our Cosmic Compatibility")
    st.write("I ran the astrological charts and analyzed our palm lines...")
    
    if st.button("Calculate Match Score"):
        st.metric(label="Final Score", value="100%", delta="Written in the stars! 🌠")
        st.snow() # Adds a cool falling animation

    st.divider()

    # --- THE TIMELINE ---
    st.header("🕰️ Our Story So Far...")

    st.subheader("Month 1: The Beginning")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Do you remember our first date? I was so nervous but...")
    with col2:
        st.info("🖼️ (Put a cute photo of you guys here!)")

    st.subheader("Months 2-4: The Adventures")
    with st.expander("Click here for a secret memory 🤫"):
        st.write("Remember that time we got lost? Best detour ever.")

    st.subheader("Month 5: Right Now")
    st.write("Five months in and I'm looking forward to everything coming next.")
    
    st.divider()
    st.write("Made with ❤️ by me.")

elif password:
    st.error("Access Denied! Think harder! 😂")
