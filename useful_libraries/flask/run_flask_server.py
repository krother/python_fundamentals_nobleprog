"""
Start a web server:

1) python -m pip install flask
2) start the program
3) go to http://localhost:5000 in the browser

"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello():
    return """<h1>Hello World!</h1>"""

@app.route("/hello/<name>")
def hello_name(name):
    return f"""<h1>Hello {name}!</h1>"""

@app.route("/")
def main():
    return render_template('main.html',
              title='Start page',
              animals=['cat', 'dog', 'fish', 'platypus']
              )


if __name__ == "__main__":
    app.run()
