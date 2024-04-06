import google.generativeai as genai
genai.configure(api_key="AIzaSyAY5c9AURVhn-iyfcnhKTX6isLukn0lN4o")
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat()
while True:
    message = input("You: ")
    response = chat.send_message(message)
    print("Gemini: " + response.text)
