from flask import Flask, request
import os


app = Flask(__name__)


@app.route("/status")
def status():
    return("The Form Output Server is up and running")

@app.route("/form_output", methods=["POST"])
def form_output():
    data = request.form
    data = dict(data.lists())
    cwd = os.getcwd()
    filename = os.path.join(cwd, "form_return.txt")

    with open(filename, 'w') as f:
        f.write(str(data))
    return("All is well")