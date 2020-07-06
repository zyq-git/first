from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def demo():
    return render_template('demo.html')


@app.route('/test')
def test():
    return '测试'

if __name__ == '__main__':
    app.debug = True
    app.run()
