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

