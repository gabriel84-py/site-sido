from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('présentation.html')

@app.route('/actualités')
def actualités():
    return render_template('actualités.html')

@app.route('/références')
def références():
    return render_template('références.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/plan-accès')
def plan():
    return render_template('plan-accès.html')

@app.route('/recrutement')
def recrutement():
    return render_template('recrutement.html')


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port='5500')