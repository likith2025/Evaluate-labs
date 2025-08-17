# Simple Rule-Based Chatbot using if-else

print("🤖 Chatbot: Hello! I'm your simple chatbot. Type 'bye' to end the chat.")

while True:
    user_input = input("You: ").lower()  # convert to lowercase for easier matching
    
    # Exit condition
    if "bye" in user_input:
        print("🤖 Chatbot: Goodbye! Have a great day! 👋")
        break
    
    # Greeting responses
    elif "hello" in user_input or "hi" in user_input:
        print("🤖 Chatbot: Hello there! How can I help you today?")
    
    # Asking about chatbot's well-being
    elif "how are you" in user_input:
        print("🤖 Chatbot: I'm doing great! Thanks for asking. How are you?")
    
    # Asking chatbot's name
    elif "your name" in user_input:
        print("🤖 Chatbot: I'm a simple rule-based chatbot created with Python!")
    
    # Asking about the time (demo response)
    elif "time" in user_input:
        print("🤖 Chatbot: I can't check real time yet, but I know it’s always Python time! 🐍")
    
    # Asking about creator
    elif "who created you" in user_input:
        print("🤖 Chatbot: I was created by a Python programmer using if-else rules.")
    
    # Default fallback response
    else:
        print("🤖 Chatbot: Sorry, I didn't understand that. Could you please rephrase?")
