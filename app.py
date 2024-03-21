from flask import Flask, render_template, jsonify, request
from openai import OpenAI
from dotenv import dotenv_values
import json

config = dotenv_values(".env")

client = OpenAI(api_key=config["OPENAI_API_KEY"])

app = Flask(__name__,  template_folder='templates', static_folder='static', static_url_path='')
def get_colors(msg):
    prompt = f"""
    You are a color palette generating assistant that responds to text prompts for color palettes
    Your should generate color palettes that fit the theme, mood, or instructions in the prompt.
    The palettes should be between 2 and 8 colors.

    Q: Convert the following verbal description of a color palette into a list of colors: The Mediterranean Sea
    A: ["#006699", "#66CCCC", "#F0E68C", "#008000", "#F08080"]

    Q: Convert the following verbal description of a color palette into a list of colors: sage, nature, earth
    A: ["#EDF1D6", "#9DC08B", "#609966", "#40513B"]


    Desired Format: a JSON array of hexadecimal color codes

    Q: Convert the following verbal description of a color palette into a list of colors: {msg}
    A:
    """

    # response = client.completions.create(
    #     prompt=prompt, model="text-davinci-003", max_tokens=200
    # )

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="gpt-3.5-turbo",
        max_tokens=200,
    )

    # colors = json.loads(response.choices[0].text)
    colors = json.loads(response.choices[0].message.content)

    return colors

@app.route('/')
def index():
    # response = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "system", "content": "You are a helpful assistant."},
    #         {"role": "user", "content": "Give me a funny word to say to my friend."}
    #     ]
    # )
    return render_template('index.html')
    


@app.route('/palette' , methods=['POST'])
def get_palatte():
    msg = request.json.get('color')
    colors = get_colors(msg)
    return jsonify(colors)

    



if __name__ == '__main__':
    app.run(debug=True)