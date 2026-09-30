import google.generativeai as genai

# Replace with your actual key
genai.configure(api_key="AIzaSyD1SEa50JvaLNLgpGOsWdnR-A22PURI1ic")

# FIX: Using the newly available 2.5 Flash model
model = genai.GenerativeModel('models/gemini-2.5-flash')

response = model.generate_content("Say: Hello, the JECRC Assistant backend is officially online!")
print(response.text)