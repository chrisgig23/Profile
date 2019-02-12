from flask import Flask, render_template, request, redirect
from flask import url_for, flash, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'chris.giglio.com@gmail.com'
app.config['MAIL_PASSWORD'] = 'sPunky23!'
app.config['MAIL_DEFAULT_SENDER'] = 'chris.giglio.com@gmail.com'
app.config['MAIL_MAX_EMAILS'] = None
# app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)


@app.route('/')
def welcomeHome():
    return render_template('index.html')

@app.route('/tictactoe')
def playGame():
    return render_template('game.html')

@app.route('/contact')
def contactMe():
    return render_template('contact.html')

@app.route('/testing')
def testingMail():
    msg = Message('Testing', recipients = ['cgiglio23@gmail.com'])
    mail.send(msg)

    return 'success'

if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0', port=5000)
