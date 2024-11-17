# -*- coding: utf-8 -*-
"""LLM_docker_image.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lFuCenteW8dv0iq_zx7kQTLZwwFXRtqV
"""

from transformers import pipeline

# Load pre-trained model for text generation (conversational AI)
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-small")

def chat():
    print("Hello! I'm a chatbot. Type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        response = chatbot(user_input, max_length=1000, pad_token_id=50256, temperature=0.7,truncation=True)
        print("Chatbot: ", response[0]['generated_text'])

if __name__ == "__main__":
    chat()