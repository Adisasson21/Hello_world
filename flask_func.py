from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    print("hello")
    return "hello world"


app.run(host="0.0.0.0", port=5000, debug=True)
