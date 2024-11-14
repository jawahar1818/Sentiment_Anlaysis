pip install groq

# get the openai secret key
import getpass
import pandas as pd

import os
from groq import Groq

def get_response(example):
  response = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
      {
        "role": "system",
        "content": "You are an expert in restaurant marketing with a specialism in sentiment analysis. \n\nI will give you some reviews and I want you to return one word based on the sentiment. Positive, Negative or Neutral. "
      },
      {
        "role": "user",
        "content": "With all the new upgrades everything looks great and clean great staff"
      },
      {
        "role": "assistant",
        "content": "Positive"
      },
      {
        "role": "user",
        "content": "It'd McDonalds. It is what it is as far as the food and atmosphere go. The staff here does make a difference. They are all friendly, accommodating and always smiling. Makes for a more pleasant experience than many other fast food places."
      },
      {
        "role": "assistant",
        "content": "Positive"
      },
      {
        "role": "user",
        "content": "We stopped by for a quick breakfast.  It was not crowded inside, but there was a pretty long drive thru.\nOur order was supposed to have 3 food items and 2 drinks. They missed a food item. The lady ignored me when I told her.My husband went to get it, she finished her task then handed it to him without a word or smile or anything."
      },
      {
        "role": "assistant",
        "content": "Negative"
      },
      {
        "role": "user",
        "content": "The morning crew seems fast and efficient. Night crew is a whole different experience, lines down the street, hour long waits. If this was a one time occurrence it wouldn't be so bad but this is a nightly problem. Beyond this the staff is so highly rude you leave wanting to crash your car through the building. Don't forget they will mistake your order almost every single time as well and serve it to you cold."
      },
      {
        "role": "assistant",
        "content": "Negative"
      },
      {
        "role": "user",
        "content": "Me and my girlfriend came tonight to pick up our food after 11pm for a mobile order, they need a better system if you are walking on foot. The food tasted great, loved the McDonald's deal ordering from the app."
      },
      {
        "role": "assistant",
        "content": "Neutral"
      },
      {
        "role": "user",
        "content": "Been frequenting this location for a few years.Morning,mid-day and night,the food is always hot,fresh and served with a smile."
      },
      {
        "role": "assistant",
        "content": "Positive"
      },
     {
      "role": "user",
      "content": f"""{example} """
    }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return response.choices[0].message.content

get_response("""I work for door dash and they locked us all out to wait in a long line for no reason at 10. I tried to beg them to open it because I'm door dash and they refused. Covid is over get a new job""")

df = pd.read_csv('https://raw.githubusercontent.com/analyticswithadam/Python/main/Data/McD%20Reviews.csv')
df['Review'] = df['Review'].str.strip()

df.head()

df['Review']

df2 = df[100:120].copy()
df2

df2['open_ai_Sentiment'] = df2['Review'].apply(get_response)
df2