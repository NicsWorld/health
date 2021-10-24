from flask import Flask, render_template
from ping3 import ping
app = Flask(__name__)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/api/wicnoods")
def wicnoods():
    wicnoods = ping('wicnoods.com')
    return str(wicnoods)

@app.route("/api/dinner")
def dinner():
    dinner = ping('dinner.dev')
    return str(dinner)

@app.route("/api/workout")
def workout():
    workout = ping('workout.lol')
    return str(workout)            