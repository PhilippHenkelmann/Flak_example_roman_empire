from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/culture')
def culture():
    return render_template('culture.html')

@app.route('/famous_people')
def famous_people():
    return render_template('famous_people.html')

@app.route('/redirect-to-history')
def redirect_to_history():
    return redirect(url_for('history'))

@app.route('/ancient_technology')
def ancient_technology():
    return render_template('ancient_technology.html')


if __name__ == "__main__":
    app.run(debug=True)
