import streamlit as st
from datetime import date

# 1. Page Configuration (Changes the tab title and icon)
st.set_page_config(page_title="Happy 5 Months!", page_icon="❤️")

# 2. The Password Gate
st.markdown("### 🔒 Top Secret Boyfriend Files")
password = st.text_input("What is our secret word?", type="password")

# Change "pizza" to whatever inside joke you want!
if password.lower() == "pizza":
    
    # Trigger celebration!
    st.balloons()
    
    # 3. The Main Header
    st.title("Happy 5 Months! ❤️")
    st.write("I built this little website just to say I love you and look back at our story so far.")
    
    # 4. A Fun Stat Counter
    st.metric(label="Days Since We Started Dating", value="150+ Days", delta="And counting!")
    st.divider() # Adds a nice horizontal line

    # 5. The Timeline Section
    st.header("🕰️ Our Story So Far...")

    # Month 1
    st.subheader("Month 1: The Beginning")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Do you remember our first date? I was so nervous but...")
    with col2:
        # To use a real photo, put it in your GitHub repo and change the name below:
        # st.image("first_date.jpg", caption="Our first selfie!")
        st.info("🖼️ (Put a cute photo of you guys here!)")

    # Month 2-4 (Using an expander for a hidden memory)
    st.subheader("Months 2-4: The Adventures")
    st.write("We did so much in such a short time...")
    
    with st.expander("Click here for a secret memory 🤫"):
        st.write("Remember that time we got lost trying to find that restaurant? Best detour ever.")

    # Month 5
    st.subheader("Month 5: Right Now")
    st.write("Five months in and I'm looking forward to everything coming next.")
    
    # A cute sign-off
    st.divider()
    st.write("Made with ❤️ (and a little bit of Python code) by me.")

elif password:
    # If she types the wrong thing
    st.error("Access Denied! Think harder! 😂")