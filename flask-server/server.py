from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    message = "helloe there"
    return render_template('index.html', message=message)


# run the application
if __name__ == "__main__":
    app.run(debug=True)
