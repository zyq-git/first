from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def demo():
    return 'hello word'


if __name__ == '__main__':
    app.run()
