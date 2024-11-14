# Daily Checklist App

This is a simple Flask web application that i created to maintain a checklist of items to study.

### Features

- A daily checklist of tasks.
- Mark tasks as complete with checkboxes.
- The app uses dark mode styling for a sleek interface.
- Task statuses are saved per day, and the app remembers them across page reloads.
  
### Technologies Used

- **Flask**: A Python web framework to build the app.
- **Bootswatch (Darkly)**: A dark theme for the Bootstrap framework.
- **HTML, CSS**: For structuring and styling the front-end.

### Setup Instructions

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/daily-checklist-app.git
    cd daily-checklist-app
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate     # For Windows
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Open your browser and navigate to:

    ```
    http://127.0.0.1:5000
    ```

    You should see the daily checklist with a dark mode interface.

