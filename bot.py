"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import telebot

import keep_alive

import google.generativeai as genai

genai.configure(api_key="AIzaSyBEUAD5p-QtWz9QTfcL_Seiai9RmxMxvlM")

bot = telebot.TeleBot("6857654451:AAGJbpXD4eiTkRQL8sQf664IS8d3XLS-xGk")

keep_alive.keep_alive()

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-latest",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

convo = model.start_chat(
  history=[{
        
        "role": "user",
        "parts": ["Hi"]
  },
  {
        "role": "model",
        "parts": ["Apakah kamu AI?"]
  }
  ]
)

# response = convo.send_message("hallo")

# print(convo.text)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    convo.send_message(message.text)
    response = convo.last.text
    bot.reply_to(message, response)

if __name__== "__main__":
    print("Bot Started Running")
    bot.polling()