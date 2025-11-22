from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import os
import secrets
from backend import (USER_DATA_DIR, hash_password, save_user,
                     load_character_notes, save_character_notes,
                     get_characters_for_game, load_all_notes, GAME_CHARACTERS)
from functools import wraps

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Secure secret key for sessions


# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Please login first', 'error')
            return redirect(url_for('logininfo'))
        return f(*args, **kwargs)

    return decorated_function


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['textbox'].strip()
        return render_template('index.html', users_text=text)
    return render_template('index.html')


# Dashboard - now passes character lists to template
@app.route('/dashboard')
@login_required
def dashboard():
    username = session.get('username')
    # Pass all game characters to the dashboard
    return render_template('dashboard.html',
                           username=username,
                           game_characters=GAME_CHARACTERS)


# Notebook route - now requires character in URL
@app.route('/notebook/<game>/<character>')
@login_required
def notebook(game, character):
    username = session.get('username')

    # Validate game name
    valid_games = ['mk1', 'sf6', '2xko']
    if game not in valid_games:
        flash('Invalid game selected', 'error')
        return redirect(url_for('dashboard'))

    # Validate character exists for this game
    characters = get_characters_for_game(game)
    if character not in characters:
        flash('Invalid character selected', 'error')
        return redirect(url_for('dashboard'))

    # Game display names
    game_names = {
        'mk1': 'Mortal Kombat 1',
        'sf6': 'Street Fighter 6',
        '2xko': '2XKO'
    }

    # Load notes for this character
    notes = load_character_notes(username, game, character)

    # Get all notes to know which characters have notes
    all_notes = load_all_notes(username, game)
    characters_with_notes = list(all_notes.keys())

    return render_template('notebook.html',
                           game=game,
                           game_name=game_names[game],
                           characters=characters,
                           selected_character=character,
                           notes=notes,
                           characters_with_notes=characters_with_notes,
                           username=username)


# Save notes route
@app.route('/save_notes', methods=['POST'])
@login_required
def save_notes_route():
    username = session.get('username')
    game = request.form.get('game')
    character = request.form.get('character')
    content = request.form.get('content', '')

    if not character:
        return jsonify({'success': False, 'message': 'No character selected'}), 400

    success, message = save_character_notes(username, game, character, content)

    if success:
        return jsonify({'success': True, 'message': message})
    else:
        return jsonify({'success': False, 'message': message}), 400


@app.route('/login', methods=['GET', 'POST'])
def logininfo():
    if request.method == 'POST':
        username = request.form['username'].strip().lower()
        password = request.form['password'].strip()

        user_file = os.path.join(USER_DATA_DIR, f'{username}.txt')
        print(f"Looking for: {user_file}")  # Debug

        if os.path.exists(user_file):
            with open(user_file, 'r') as f:
                lines = [line.strip() for line in f.readlines()]
                stored_password = lines[2].split(': ')[1]

            if stored_password == hash_password(password):
                session['username'] = username
                flash('Login Successful', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid password', 'error')
        else:
            flash('User not found', 'error')

        return render_template('login.html')
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('user').strip().lower()
        email = request.form.get('email').strip()
        password = request.form.get('pass').strip()
        password_confirm = request.form.get('passc').strip()

        if not username or not email or not password or not password_confirm:
            flash('All fields are required', 'error')
            return render_template('signUp.html')

        if password != password_confirm:
            flash('Passwords do not match', 'error')
            return render_template('signUp.html')

        if len(password) < 6:
            flash('Password must be at least 6 characters', 'error')
            return render_template('signUp.html')

        success, message = save_user(username, email, password)
        if success:
            flash(message, 'success')
            return redirect(url_for('logininfo'))
        else:
            flash(message, 'error')
            return render_template('signUp.html')

    return render_template('signUp.html')


@app.route('/logout')
@login_required
def logout():
    session.pop('username', None)
    flash('You have been logged out', 'success')
    return redirect(url_for('logininfo'))


if __name__ == '__main__':
    app.run(debug=True)