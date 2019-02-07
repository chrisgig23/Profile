from flask import Flask, render_template, request, redirect
from flask import url_for, flash, jsonify

app = Flask(__name__)


@app.route('/')
def welcomeHome():
    return render_template('index.html')

@app.route('/tictactoe')
def playGame():
    return render_template('game.html')

@app.route('/contact')
def contactMe():
    return render_template('contact.html')

if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0', port=5000)
