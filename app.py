from flask import Flask, render_template, request
from google import genai
from pydantic import BaseModel
import os
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/question_lobby")
def question_lobby():
    return render_template("question_lobby.html")

@app.route("/question")
def question():
    return render_template("question.html")

@app.route("/question2s",methods=["post"])
def question2():
    device=request.form["device"]
    return render_template("question2s.html",device=device)

@app.route("/gemini",methods=["post"])
def gemini():

    class recommendation(BaseModel):
        device_name: str
        detail: list[str]

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    device_choice=request.form["device_choice"]
    device_use=request.form["device_use"]
    device_os=request.form["os"]
    device_point=request.form["device_point"]

    response = client.models.generate_content(
          model="gemini-2.0-flash",
          contents=f"予算は{device_choice}、osは{device_os}で、主な用途は{device_use}、こだわるポイントは{device_point}のスマートフォンを教えてください",
          config={
              "response_mime_type": "application/json",
              "response_schema": list[recommendation],
          },
      )
# Use the response as a JSON string.
    print(response.text)

# Use instantiated objects.
    my_recommendation: list[recommendation] = response.parsed