import random

knowledge_base = {
    "best under 50000": "Some great DSLR options under ₹50,000 are Canon 1500D, Nikon D3500, and Canon 3000D.",
    "canon vs nikon": "Both brands are excellent. Canon offers better color science, while Nikon has superior dynamic range in some models.",
    "aperture": "Aperture controls the amount of light entering the lens. Lower f-number means more light and shallow depth of field.",
    "iso": "ISO measures light sensitivity. Higher ISO is good for low light, but can introduce noise.",
    "shutter speed": "Shutter speed is how long the sensor is exposed to light. Fast shutter = sharp images, slow = motion blur.",
    "lenses for beginners": "A good starter lens is a 50mm f/1.8 or an 18-55mm kit lens.",
    "beginner dslr": "Great beginner DSLRs include Canon 200D Mark II and Nikon D3500.",
    "professional dslr": "Professional options include Canon 5D Mark IV, Nikon D850, and Canon R6 (mirrorless)."
}

# Define keywords for each topic to match loosely
keywords = {
    "best under 50000": ["best", "under", "50000", "cheap", "budget"],
    "canon vs nikon": ["canon", "nikon", "compare", "vs", "difference"],
    "aperture": ["aperture", "f-stop", "f number"],
    "iso": ["iso", "sensitivity", "noise"],
    "shutter speed": ["shutter", "speed", "exposure"],
    "lenses for beginners": ["lens", "lenses", "beginner", "starter"],
    "beginner dslr": ["beginner", "first", "starter", "dslr"],
    "professional dslr": ["professional", "pro", "advanced", "dslr"]
}

default_response = "Sorry, I don't have that information yet. Please ask about DSLR models, lenses, settings, or comparisons."

def get_response(user_input):
    user_input = user_input.lower()
    for topic, keys in keywords.items():
        if any(k in user_input for k in keys):
            return knowledge_base[topic]
    return default_response

def start_chat():
    print("📸 Hello! I'm your DSLR Assistant Bot. Ask me anything about DSLR cameras. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("Bot: Thanks for chatting! Happy clicking! 📷")
            break
        response = get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    start_chat()
