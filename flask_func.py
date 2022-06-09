from flask import Flask
from func import func_print

app = Flask(__name__)


@app.route('/')
def hello():

    return func_print()


app.run(host="0.0.0.0", port=5000, debug=True)