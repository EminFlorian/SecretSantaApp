from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Display
users = []

@app.route('/')
def home():
    return render_template('index.html', users=users)

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    if name:
        users.append(name)
    return redirect(url_for('home'))

@app.route('/generate', methods=['GET'])
def generate_secret_santa():
    if len(users) < 2:
        return "Need at least 2 participants to generate Secret Santa pairs."
    
    # Usr Shuffle
    random.shuffle(users)
    
    # Shuffle Pairs
    pairs = {users[i]: users[(i + 1) % len(users)] for i in range(len(users))}
    
    # Display
    return render_template('pairs.html', pairs=pairs)

if __name__ == '__main__':
    app.run(debug=True)
