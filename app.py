from flask import Flask, request, render_template, redirect
from tracking_list import tracking_list
import os

app = Flask(__name__)


@app.route('/')
def root():
    return render_template("main.html", tracking_list=tracking_list)


# page to add new tracking numbers to sheet
@app.route('/add', methods=['POST'])
def add():
    sender = request.form['sender'] or None
    carrier = request.form['carrier'] or None
    tracking_number = request.form['tracking_number'] or None
    status = request.form['status'] or None

    try:
        return redirect('/')

    except:
        return "There was an issue adding the new tracking number. Please make sure the fields are not empty."

# search/filter tracking numbers

# delete tracking numbers

# update tracking numbers


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(port=port, debug=True)
