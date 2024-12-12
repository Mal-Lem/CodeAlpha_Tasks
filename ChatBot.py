import nltk
from nltk.chat.util import Chat, reflections

# download the punkt tokenizer for sentence tokenization
nltk.download('punkt')

# define pairs of patterns and responses for the chatbot
# each pattern is a regular expression and each response corresponds to that pattern
pairs = [
    (r"hi|hello|hey", ["Hello! How can I assist you today?", "Hey! How can I help?"]),
    (r"what is your name?", ["I am a chatbot created by an AI!", "I'm your friendly chatbot."]),
    (r"how are you?", ["I'm doing great! How can I help you today?", "I'm doing well, thank you!"]),
    (r"bye|goodbye", ["Goodbye! Have a great day!", "It was nice talking to you. Bye!"]),
    (r"my name is (.*)", ["Hello %1, nice to meet you!", "Hi %1, how can I assist you today?"]),
    (r"what can you do?", ["I can chat with you, answer questions, and help with basic tasks.", "I can assist you with various tasks. Ask me anything!"]),
    (r"(.*) (your|my) (.*)", ["Let's not talk about that. How can I assist you further?", "I am not sure about that, but I'm here to help with anything else."]),
    (r"(.*) weather (.*)", ["I can't provide live weather updates, but you can check online.", "I'm not equipped to check the weather, but let me know if you need guidance on where to look!"]),
    (r"how old are you?", ["I don't have an age, I'm a virtual assistant.", "Age doesn't apply to me, I'm here to help you anytime!"]),
    (r"tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!"]),
    (r"thank you|thanks", ["You're welcome!", "Glad I could help!"]),
    (r"what is (.*)", ["That's an interesting question about %1. Let me look it up for you!", "I'm not sure about %1, but I can find out!"]),
    (r"do you like (.*)", ["I don't have preferences, but I'm here to assist you!", "I don't have feelings, but I think %1 sounds great!"]),
    (r"how to (.*)", ["Here's a guide to help you with %1.", "Let me explain how to %1 step by step."]),
    (r"can you (.*)", ["I can try to help you with %1!", "Sure, I can assist with %1. Let's get started!"]),
    (r"(.*) recipe for (.*) data scientist (.*)", 
     [
        "Here's the recipe for becoming a successful Data Scientist:\n"
        "1. Start with a strong foundation in mathematics (linear algebra, calculus, and statistics).\n"
        "2. Add programming skills: master Python and R.\n"
        "3. Sprinkle in SQL and data visualization tools (Tableau, Power BI, or Matplotlib).\n"
        "4. Mix thoroughly with machine learning and AI techniques (Scikit-learn, TensorFlow, PyTorch).\n"
        "5. Don't forget to season with real-world projects and Kaggle competitions.\n"
        "6. Bake with curiosity, patience, and continuous learning until you achieve mastery!"
     ]),
    (r"(.*)", ["I'm not sure how to respond to that, but let's keep talking!", "Can you tell me more about that?"])
]


# create the chatbot
chatbot = Chat(pairs, reflections)

# function to start the chatbot
def start_chat():
    print("Hello! I'm your friendly chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day.")
            break
        else:
            response = chatbot.respond(user_input)
            print("Chatbot:", response)

# start the chatbot
if __name__ == "__main__":
    start_chat()
