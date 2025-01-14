import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the API with your key
genai.configure(api_key=os.getenv('NOT_API_KEY'))

# Initialize the model (use the "gemini-1.5-flash" model or whichever is appropriate)
model = genai.GenerativeModel("gemini-1.5-flash")

# System message to guide the model to respond in pirate speak
system_message = "You are a pirate chatbot. Respond only in pirate speak, using pirate slang and nautical terms. Do not reply in normal English."

# Function to generate responses in pirate speak
def generate_pirate_response(user_message, chat_history):
    # Combine the system message with the user's input and previous chat history to guide the model's response
    history = "\n".join(chat_history)
    prompt = f"{system_message}\n{history}\nUser: {user_message}\nPirate Response:"

    # Generate the response using the model
    response = model.generate_content(prompt)

    return response.text

# Example of interacting with the chatbot
if __name__ == "__main__":
    chat_history = []  # List to store conversation history
    while True:
        # Get user input
        message = input("Enter your message (or type 'exit' to quit): ")
        
        if message.lower() == 'exit':
            print("Exiting the chat...")
            break
        
        # Add the user's message to the history
        chat_history.append(f"User: {message}")
        
        # Get the pirate response
        pirate_response = generate_pirate_response(message, chat_history)
        
        # Add the pirate response to the history
        chat_history.append(f"Pirate Response: {pirate_response}")
        
        # Print the pirate response
        print("Pirate Response:", pirate_response)
