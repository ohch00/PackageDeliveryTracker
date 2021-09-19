from flask import Flask, request, render_template, redirect
from flask_bootstrap import Bootstrap
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
        with open("tracking_list.txt", 'r+') as file:
            data = json.load(file)

            new_data = {
                "id": len(data),
                "sender": sender,
                "carrier": carrier,
                "tracking_number": tracking_number,
                "status": "None"
            }

            data.append(new_data)
            file.seek(0)
            json.dump(data, file, indent=4)

        return redirect('/')

    except:
        return "There was an issue adding the new tracking number. Please make sure the fields are not empty."


# search/filter tracking numbers
def filtering():
    sender = request.form['sender']
    carrier = request.form['carrier']
    tracking_number = request.form['tracking_number']
    status = request.form['status']

    try:
        return render_template('main.html', tracking_number=None)

    except:
        return "There was an issue searching for tracking numbers."


# delete tracking numbers
def delete():
    pass


# update tracking numbers
def edit():
    pass


# refresh tracking numbers
def refresh():
    pass


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(port=port, debug=True)
