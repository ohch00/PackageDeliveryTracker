from flask import Flask, request, render_template
from tracking_list import tracking_list
import os

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("main.html", tracking_list=tracking_list)


@app.route('/add')
def add():
    return 0


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(port=port, debug=True)
