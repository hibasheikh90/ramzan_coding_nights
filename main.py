
# Import required libraries
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
import time  # For animation effects

# Apply custom CSS for a black background
st.markdown("""
    <style>
        body {
            background-color: black !important;
        }
        .stApp {
            background-color: black;
        }
    </style>
""", unsafe_allow_html=True)

# List of available time zones
TIME_ZONES = [
    "🌍 UTC",
    "🇵🇰 Asia/Karachi",
    "🇺🇸 America/New_York",
    "🇬🇧 Europe/London",
    "🇯🇵 Asia/Tokyo",
    "🇦🇺 Australia/Sydney",
    "🇺🇸 America/Los_Angeles",
    "🇩🇪 Europe/Berlin",
    "🇦🇪 Asia/Dubai",
    "🇮🇳 Asia/Kolkata",
]

# Animated title with blue neon lighting effect
st.markdown("""
    <h1 style='text-align: center; 
               color: #00ccff;
               text-shadow: 0px 0px 20px #00ccff, 0px 0px 40px #0099ff, 0px 0px 60px #0066ff;'>
        ⚡ Time Zone Converter 🌍
    </h1>
""", unsafe_allow_html=True)

# Multi-select dropdown for choosing time zones
selected_timezone = st.multiselect(
    "🕰️ Select Timezones", TIME_ZONES, default=["🌍 UTC", "🇵🇰 Asia/Karachi"]
)

# Display current time for selected time zones
st.markdown("""
    <h2 style='color: #00ccff;
               text-shadow: 0px 0px 15px #00ccff, 0px 0px 30px #0099ff, 0px 0px 45px #0066ff;'>
        ⏱️ Selected Timezones
    </h2>
""", unsafe_allow_html=True)

for tz in selected_timezone:
    # Get and format current time for each selected timezone with AM/PM
    current_time = datetime.now(ZoneInfo(tz.split(" ")[1])).strftime("%Y-%m-%d %I:%M:%S %p")
    # Display timezone and its current time
    st.write(f"**{tz}**: ⏲️ {current_time}")

# Section for time conversion with animation
st.markdown("""
    <h2 style='color: #00ccff;
               text-shadow: 0px 0px 15px #00ccff, 0px 0px 30px #0099ff, 0px 0px 45px #0066ff;'>
        🔄 Convert Time Between Timezones
    </h2>
""", unsafe_allow_html=True)
st.markdown("⚡ *Easily convert time from one timezone to another at the speed of light!*")

# Time input field with current time as default
current_time = st.time_input("⏰ Current Time", value=datetime.now().time())
# Dropdown to select source timezone
from_tz = st.selectbox("🌐 From Timezone", TIME_ZONES, index=0)
# Dropdown to select target timezone
to_tz = st.selectbox("🌍 To Timezone", TIME_ZONES, index=1)

# Convert button with animation effect
if st.button("⚡ Convert Time"):
    # Show a glowing loading effect
    with st.spinner("⚡ Converting time... Hold tight!"):
        time.sleep(2)  # Simulating loading effect
    
    # Combine today's date with input time and source timezone
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz.split(" ")[1]))
    # Convert time to target timezone and format it with AM/PM
    converted_time = dt.astimezone(ZoneInfo(to_tz.split(" ")[1])).strftime("%Y-%m-%d %I:%M:%S %p")
    
    # Display the converted time with a success message
    st.success(f"⚡ Converted Time in {to_tz}: {converted_time}")

    # Simulating neon lighting effect using markdown animation
    st.markdown("""
        <div style="text-align: center;">
            <h2 style='color: #00ccff;
                       text-shadow: 0px 0px 20px #00ccff, 0px 0px 40px #0099ff, 0px 0px 60px #0066ff;'>
                ✨ Time Converted Successfully! ✨
            </h2>
        </div>
    """, unsafe_allow_html=True)

# Footer with blue neon glowing effect
st.markdown("---")
st.markdown("""
    <h4 style='text-align: center; 
               color: #00ccff;
               text-shadow: 0px 0px 15px #00ccff, 0px 0px 30px #0099ff, 0px 0px 45px #0066ff;'>
        👩‍💻 Developed by <b>Hiba Sheikh</b> 💡
    </h4>
""", unsafe_allow_html=True)
