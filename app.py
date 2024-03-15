from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy data for illustration purposes
users = {'admin': 'password'}
activities = [{'type': 'Run', 'distance': 5, 'date': '2024-03-16'}]

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', activities=activities)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return 'Invalid username or password'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/log_activity', methods=['GET', 'POST'])
def log_activity():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        # Simplified example; in a real app, you'd save this data to a database
        activity = {
            'type': request.form['type'],
            'distance': request.form['distance'],
            'date': request.form['date']
        }
        activities.append(activity)  # Assuming 'activities' is a global list
        return redirect(url_for('home'))
    
    return render_template('log_activity.html')

@app.route('/welcome')
def welcome():
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(debug=True)
