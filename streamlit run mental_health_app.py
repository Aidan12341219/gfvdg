import streamlit as st
import pandas as pd
import datetime

# Set the page title and layout
st.set_page_config(page_title="Mental Health Tracker", layout="wide")

# Title of the app
st.title("Mental Health Tracker")

# Sidebar navigation
st.sidebar.header("Navigation")
app_mode = st.sidebar.radio("Select Mode", ["Home", "Track Mood", "Resources", "Daily Journal"])

# Home Page
if app_mode == "Home":
    st.header("Welcome to Your Mental Health Tracker")
    st.write("""
    This app helps you track your mood, set daily check-ins, and find mental health resources. 
    Your mental health is important, and this tool aims to support you in nurturing your well-being.
    """)
    st.image("https://www.holidify.com/images/cmsuploads/compressed/mental_health_20210526144430.jpg", use_column_width=True)

# Mood Tracking Page
elif app_mode == "Track Mood":
    st.header("Mood Tracker")
    
    # Input for tracking mood
    mood = st.radio("How are you feeling today?", ("Very Happy", "Happy", "Neutral", "Sad", "Very Sad"))
    energy_level = st.slider("How would you rate your energy today?", 1, 10, 5)
    stress_level = st.slider("How stressed do you feel today?", 1, 10, 5)
    
    # Timestamp for tracking
    today = datetime.date.today()
    
    # Create a DataFrame to store mood logs
    if 'mood_log' not in st.session_state:
        st.session_state.mood_log = pd.DataFrame(columns=["Date", "Mood", "Energy Level", "Stress Level"])

    # Save the mood log entry
    if st.button("Log Mood"):
        new_entry = {
            "Date": today,
            "Mood": mood,
            "Energy Level": energy_level,
            "Stress Level": stress_level
        }
        st.session_state.mood_log = st.session_state.mood_log.append(new_entry, ignore_index=True)
        st.success("Your mood has been logged!")
    
    # Display mood log
    st.subheader("Your Mood Log")
    st.write(st.session_state.mood_log)

# Resources Page
elif app_mode == "Resources":
    st.header("Mental Health Resources")

    st.write("""
    Here are some mental health resources to support you:
    """)
    
    st.markdown("""
    - [National Suicide Prevention Lifeline](https://suicidepreventionlifeline.org) - Call 1-800-273-8255
    - [Mental Health America](https://www.mhanational.org)
    - [Crisis Text Line](https://www.crisistextline.org) - Text HOME to 741741
    - [Therapists Directory](https://www.psychologytoday.com/us/therapists)
    """)
    
    st.write("If you need more resources or are in immediate danger, please reach out to a healthcare professional.")
    
# Daily Journal Page
elif app_mode == "Daily Journal":
    st.header("Daily Journal")
    
    # Journal input
    journal_entry = st.text_area("Write about your day, thoughts, or feelings:", height=200)
    
    if st.button("Save Journal Entry"):
        if 'journal_entries' not in st.session_state:
            st.session_state.journal_entries = pd.DataFrame(columns=["Date", "Journal Entry"])
        
        today = datetime.date.today()
        new_journal_entry = {
            "Date": today,
            "Journal Entry": journal_entry
        }
        st.session_state.journal_entries = st.session_state.journal_entries.append(new_journal_entry, ignore_index=True)
        st.success("Your journal entry has been saved!")
    
    # Display past journal entries
    if 'journal_entries' in st.session_state and len(st.session_state.journal_entries) > 0:
        st.subheader("Your Past Journal Entries")
        st.write(st.session_state.journal_entries)
    else:
        st.write("No journal entries found yet.")
