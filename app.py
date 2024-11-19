import json
import os
from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

# File to store checklist data
DATA_FILE = 'checklist_data.json'

# Default todo list items
todo_items = [
    "DSA 1", 
    "DSA 2",
    "DSA 3",
    "Numpy", 
    "Java", 
    "System Design"
]

# Load checklist data from the file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save checklist data to the file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)

@app.route('/', methods=['GET', 'POST'])
def index():
    date_today = datetime.date.today().isoformat()

    # Load data from the file
    checklist_status = load_data()

    # Initialize today's status if not set
    if date_today not in checklist_status:
        checklist_status[date_today] = {item: False for item in todo_items}

    if request.method == 'POST':
        # Update checklist status based on form data
        for item in todo_items:
            checklist_status[date_today][item] = (item in request.form)
        save_data(checklist_status)  # Save updated data
        return redirect(url_for('index'))

    return render_template('index.html', todo_items=todo_items, checklist=checklist_status[date_today])

if __name__ == '__main__':
    app.run(debug=True)
