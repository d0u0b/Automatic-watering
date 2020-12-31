from flask import Flask

app = Flask(__name__, static_folder="static")

@app.route("/")
def home():
    return app.send_static_file("index.html")

app.run(port=8080, host="0.0.0.0")