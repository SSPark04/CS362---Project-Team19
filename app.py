from flask import Flask, render_template
from routes import api

app = Flask(__name__)
app.register_blueprint(api)


@app.route("/")
def index():
    """
    Serve the main page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
