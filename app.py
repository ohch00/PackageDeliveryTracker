from flask import Flask, request, render_template
import os

app = Flask(__name__)

f = open('tracking_list.txt', 'r')
content = f.read()


@app.route('/')
def root():
    return render_template("main.html", tracking_list=content)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(port=port, debug=True)
