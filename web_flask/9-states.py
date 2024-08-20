#!/usr/bin/python3
"""
Starts the Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Remove the current SQLAlchemy session after each request.
    """
    storage.close()


@app.route("/states", defaults={"id": 1}, strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_by_id(id):
    """
    Displays a HTML page with a state object.
    """
    states = storage.all(State).values()
    if id == 1:
        return render_template("9-states.html", states=states)
    else:
        for state in states:
            if state.id == id:
                return render_template("9-states.html", state=state)
        return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
