import google.generativeai as genai
genai.configure(api_key="AIzaSyAY5c9AURVhn-iyfcnhKTX6isLukn0lN4o")
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("What is Python")
print(response.text)