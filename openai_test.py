#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 13:37:04 2023

@author: thear
"""
# import os
import openai


with open("/Users/thear/Documents/openai_key.txt", "r") as file:
    openai.api_key = file.read()

# openai.Model.list()


# # Create a prompt for the language model
# prompt = "What is the meaning of life?"

# # Generate a text completion using the GPT-3 language model
# response = openai.Completion.create(
#     engine="davinci",
#     prompt=prompt,
#     max_tokens=10
# )

# # Print the generated text completion
# print(response.choices[0].text)





from PIL import Image
import requests
from io import BytesIO


while True:
    
    prompt_input = input("Enter a description: ")
    print()
    
    if prompt_input.lower() == "stop" :
        break
    
    response = openai.Image.create(
      prompt= prompt_input,
      n=1,
      size="512x512"
    )
    
    
    # Use requests to download the image
    image_url = response['data'][0]['url']
    
    # Use requests to download the image
    image_data = requests.get(image_url).content
    
    # Open the image using PIL
    image = Image.open(BytesIO(image_data))
    
    # Display the image using Python
    image.show()



