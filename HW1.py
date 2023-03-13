from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def profile():
    return render_template("JP_profilepage.html")

app.run(host="localhost", port=5001, debug=True)
