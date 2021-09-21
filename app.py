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
    status = request.form['status']

    try:
        with open("tracking_list.txt", 'r+') as file:
            data = json.load(file)

            new_data = {
                "id": len(data),
                "sender": sender,
                "carrier": carrier,
                "tracking_number": tracking_number,
                "status": status
            }

            data.append(new_data)
            file.seek(0)
            json.dump(data, file, indent=4)

        return redirect('/')

    except:
        return "There was an issue adding the new tracking number. Please make sure the fields are not empty."


# search/filter tracking numbers
@app.route('/filter', methods=['POST'])
def filtering():
    sender = request.form['sender'] or None
    carrier = request.form['carrier'] or None
    tracking_number = request.form['tracking_number'] or None
    status = request.form['status'] or None

    try:
        with open("tracking_list.txt", 'r+') as file:
            data = json.load(file)

            filtered_tracking = []

            for i in range(len(data)):
                for j in data[i].values():
                    if sender in j or carrier == j or tracking_number in j or status == j:
                        filtered_tracking.append(data[i])

        return render_template('main.html', tracking_list=filtered_tracking)

    except:
        return "There was an issue searching for tracking numbers."


# delete tracking numbers
@app.route('/delete/<int:id>')
def delete(id):
    try:
        with open("tracking_list.txt", 'r+') as file:
            data = json.load(file)

            for i in range(len(data)):
                for key, values in data[i].items():
                    if key == 'id' and values == id:
                        data.pop()
                        break

        with open("tracking_list.txt", 'w') as file:
            print(data)
            file.seek(0)
            json.dump(data, file, indent=4)

        return redirect('/')

    except:
        return "There was an issue deleting this tracking number."


# update tracking numbers
@app.route('/edit/<int:id>')
def edit(id):
    try:
        with open("tracking_list.txt", 'r') as file:
            data = json.load(file)
            display = None

            for i in range(len(data)):
                for key, values in data[i].items():
                    if key == 'id' and values == id:
                        display = data[i]
                        break

        return render_template('edit.html', i=display)

    except:
        return "There was an issue editing this tracking number."


@app.route('/edited/<int:id>', methods=['POST'])
def edit_process(id):
    try:
        sender = request.form['sender'] or None
        carrier = request.form['carrier'] or None
        tracking_number = request.form['tracking_number'] or None
        status = request.form['status'] or None
        check_null = [sender, carrier, tracking_number]

        for i in check_null:
            if i is None:
                raise Exception

        with open("tracking_list.txt", 'r+') as file:
            data = json.load(file)

            for i in range(len(data)):
                for key, values in data[i].items():
                    if key == 'id' and values == id:
                        data[i]['sender'] = sender
                        data[i]['carrier'] = carrier
                        data[i]['tracking_number'] = tracking_number
                        data[i]['status'] = status
                        break

            file.seek(0)
            json.dump(data, file, indent=4)

        return redirect('/')

    except:
        return "There was an issue editing the tracking number."


# refresh tracking numbers
def refresh():
    pass


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(port=port, debug=True)
