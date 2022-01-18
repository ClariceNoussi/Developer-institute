from flask import Flask

app = flask.Flask(__name__)

@app.route('/<username>')
def index(username):
    numbers=[o-100]
    for i in numbers
    return {numbers}

if __name__ == "__main__":
    app.run()