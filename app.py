from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

# Default todo list items
todo_items = ["DSA", "Numpy", "Java", "System Design"]

# Store each day's checklist status
checklist_status = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    date_today = datetime.date.today().isoformat()

    # Initialize today's status if not set
    if date_today not in checklist_status:
        checklist_status[date_today] = {item: False for item in todo_items}

    if request.method == 'POST':
        # Update checklist status based on form data
        for item in todo_items:
            checklist_status[date_today][item] = (item in request.form)
        return redirect(url_for('index'))

    return render_template('index.html', todo_items=todo_items, checklist=checklist_status[date_today])

if __name__ == '__main__':
    app.run(debug=True)
