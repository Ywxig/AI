from flask import Flask, request, render_template

from CuteON import Get_, Read_, Types, Write_
from CuteScript import CuteScript

import webbrowser as wb


app = Flask(__name__)

CONFIG = Read_.readAll("admin.sws")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parameters', methods=['POST'])
def parameters_process():
    paph = request.form["paph"]
    Write_.WriteLine(paph, request.form["radio"]  + "::" + request.form["name"] + "::" + request.form["value"])
    return render_template("index.html")

@app.route('/file', methods=['POST'])
def file_process():
    paph = request.form["paph"]
    text = request.form["text"]
    Write_.write(paph, text)
    return render_template("index.html")

if __name__ == '__main__':
    CuteScript.ConveyorBuilding(Read_.readLine("admin.sws", "BP-FILE"), config="admin.sws")
    app.run(host="0.0.0.0", port=8080)