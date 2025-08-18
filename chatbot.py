import json
import random

# Load intents
with open("intents.json") as f:
    intents = json.load(f)

def get_response(user_input):
    user_input = user_input.lower()
    for intent, data in intents.items():
        for keyword in data["examples"]:
            if keyword.lower() in user_input or user_input in keyword.lower():
                return random.choice(data["responses"])
    return "Sorry, I don't understand. Please rephrase your question or visit the official PC&CMD website: https://pccmdpunjab.gov.pk/"
