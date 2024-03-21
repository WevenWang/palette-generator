from dotenv import dotenv_values

config = dotenv_values(".env")

from openai import OpenAI
client = OpenAI(api_key=config["OPENAI_API_KEY"])

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a color palatte generator that responds to text prompts."},
    {"role": "user", "content": "google color, Desired format: a json array of color hex codes. The palette should be 2 - 8 colors long. Example: [\"#FF0000\", \"#00FF00\", \"#0000FF\"]"}
    
  ]


)

print(completion.choices[0].message)
