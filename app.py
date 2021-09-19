from flask import Flask, request, render_template, redirect
import os
import json

app = Flask(__name__)


@app.route('/')
def root():
    try:
        with open("tracking_list.txt", 'r') as file:
            data = file.read()
            tracking_list = json.loads(data)

        return render_template("main.html", tracking_list=tracking_list)

    except:
        with open("tracking_list.txt", 'a+') as file:
            file.write('[]')
            file.close()


# page to add new tracking numbers to sheet
@app.route('/add', methods=['POST'])
def add():
    sender = request.form['sender'] or None
    carrier = request.form['carrier'] or None
    tracking_number = request.form['tracking_number'] or None

    try:
        return redirect('/')

    except:
        return "There was an issue adding the new tracking number. Please make sure the fields are not empty."


# search/filter tracking numbers
def filter():
    sender = request.form['sender'] or None
    carrier = request.form['carrier'] or None
    tracking_number = request.form['tracking_number'] or None
    status = request.form['status'] or None

    try:
        return redirect('/')

    except:
        return "There was an issue adding the new tracking number. Please make sure the fields are not empty."


# delete tracking numbers
def delete():
    pass


# update tracking numbers
def update():
    pass


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(port=port, debug=True)
