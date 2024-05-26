from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock database for storing user data and concept history
users = {}
concept_history = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            users[username] = password
            return redirect(url_for('login'))
        else:
            return 'Username already exists!'
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('create_concept'))
        else:
            return 'Invalid username or password!'
    return render_template('login.html')

@app.route('/create_concept', methods=['GET', 'POST'])
def create_concept():
    if request.method == 'POST'):
        concept = request.form['concept']
        # Simulate video generation and explanation (not implemented)
        # Storing concept history (not implemented)
        return render_template('concept_created.html', concept=concept)
    return render_template('create_concept.html')

if __name__ == '__main__':
    app.run(debug=True)
