# ai_agent_gemini_live_v2.py
# ----------------------------------------------------
# AI Agent using Google Gemini API (AI Studio key)
# Enhanced: knows current date, time, weather, and live IPL results
# ----------------------------------------------------

import google.generativeai as genai
from datetime import datetime
import requests
import feedparser  # for reading RSS feeds

# ---------------------------
# Step 1: Configure API Key
# ---------------------------
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
 

# ---------------------------
# Step 2: Initialize Model
# ---------------------------
model = genai.GenerativeModel("gemini-2.5-flash")

# ---------------------------
# Step 3: Conversation Memory
# ---------------------------
conversation = [
    {"role": "system", "content": "You are a helpful and intelligent AI assistant. Answer clearly and politely."}
]

# ---------------------------
# Step 4: Helper Functions
# ---------------------------

def get_today():
    """Return current date and time."""
    now = datetime.now()
    return now.strftime("%A, %B %d, %Y, %H:%M:%S")

def get_weather(city="London"):
    """Fetch current weather using free wttr.in API."""
    try:
        response = requests.get(f"https://wttr.in/{city}?format=3")
        return response.text
    except:
        return "Weather info not available."

def extract_location(user_input):
    """Simple extractor to detect weather location from user query."""
    user_input = user_input.lower()
    if "weather in" in user_input:
        loc = user_input.split("weather in")[-1].strip()
        return loc.title()
    return None

def get_ipl_results():
    """
    Fetch latest IPL results using ESPN Cricinfo RSS feed.
    Free and public.
    """
    rss_url = "https://www.espncricinfo.com/rss/content/story/feeds/ipl.xml"
    try:
        feed = feedparser.parse(rss_url)
        if feed.entries:
            # Return the 3 latest headlines
            results = "\n".join([f"- {entry.title}" for entry in feed.entries[:3]])
            return results
        else:
            return "No IPL results found at the moment."
    except:
        return "Unable to fetch IPL results."

def is_ipl_query(user_input):
    """Detect if user is asking about IPL."""
    return "ipl" in user_input.lower() or "indian premier league" in user_input.lower()

# ---------------------------
# Step 5: AI Agent Function
# ---------------------------

def ai_agent(user_input: str) -> str:
    """Handles user input and returns Gemini response with live context."""
    
    # Add user input to conversation
    conversation.append({"role": "user", "content": user_input})

    # Live context: date/time
    today = get_today()
    live_context = f"System Note: Today's date and time is {today}."

    # Live weather if requested
    location = extract_location(user_input)
    if location:
        weather = get_weather(location)
        live_context += f" Current weather in {location}: {weather}."

    # Live IPL results if requested
    if is_ipl_query(user_input):
        ipl_results = get_ipl_results()
        live_context += f" Latest IPL results:\n{ipl_results}"

    # Combine conversation into prompt
    chat_context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation])
    chat_context += f"\n{live_context}"

    # Generate AI response
    response = model.generate_content(chat_context)
    answer = response.text.strip()

    # Save AI response
    conversation.append({"role": "assistant", "content": answer})

    return answer

# ---------------------------
# Step 6: Interactive Chat Loop
# ---------------------------

if __name__ == "__main__":
    print("🤖 Hello! I’m your live AI Agent (Gemini + real-time info).")
    print("I can answer your questions, provide weather updates, and IPL results.")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("🤖 Goodbye!")
            break
        
        try:
            answer = ai_agent(user_input)
            print("AI:", answer)
            print()
        except Exception as e:
            print("⚠️ Error:", e)
            print()
