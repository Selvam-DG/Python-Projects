from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPEN_API_KEY")

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_prompt"]
        chat_response = openai.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role" : "system", "content":"You are a helpful assistant."},
                {"role" : "user", "content":user_input}
            ]           
        )
        response = chat_response.choices[0].message.content.strip()
    return render_template("index.html", response = response)

if __name__ == "__main__":
    app.run()
