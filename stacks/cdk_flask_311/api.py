"""A basic Flask app."""
import sys

from flask import Flask, render_template

app = Flask(__name__)
app.debug = False
app.url_map.strict_slashes = False


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", product="Flask", version=sys.version)


@app.route("/api", methods=["GET"])
def api():
    return {"hello": "world", "stack": "Flask"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
