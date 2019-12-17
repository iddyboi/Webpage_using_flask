from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/contact')
def about():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
