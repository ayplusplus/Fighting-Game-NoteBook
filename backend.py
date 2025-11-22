import os
import hashlib
import json
# Absolute path to the directory containing this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Directory to store user files
USER_DATA_DIR = os.path.join(BASE_DIR, 'user_data')

DATA_NOTES_DIR = os.path.join(BASE_DIR, 'data_notes')

# Create the directory if it doesn't exist
if not os.path.exists(USER_DATA_DIR):
    os.makedirs(USER_DATA_DIR)

if not os.path.exists(DATA_NOTES_DIR):
    os.makedirs(DATA_NOTES_DIR)

GAME_CHARACTERS = {
    'mk1' : ['Scorpion', 'Sub-Zero', 'Liu Kang', 'Raiden', 'Kitana',
        'Mileena', 'Kung Lao', 'Johnny Cage', 'Kenshi', 'Smoke',
        'Rain', 'Reptile', 'Ashrah', 'Havik', 'Baraka',
        'Geras', 'General Shao', 'Reiko', 'Tanya', 'Li Mei',
        'Sindel', 'Shang Tsung', 'Quan Chi', 'Ermac', 'Takeda',
        'Omni-Man', 'Peacemaker', 'Homelander', 'Ghostface', 'Conan'],

    'sf6' : ['Ryu', 'Ken', 'Chun-Li', 'Guile', 'Blanka', 'Dhalsim',
        'E. Honda', 'Zangief', 'Cammy', 'Dee Jay', 'Rashid',
        'Juri', 'Kimberly', 'Lily', 'JP', 'Marisa', 'Manon',
        'Luke', 'Jamie', 'A.K.I.', 'Ed', 'Akuma', 'Bison',
        'Terry', 'Mai', 'Elena'],

    '2xko' : [ 'Ahri', 'Braum', 'Darius', 'Ekko', 'Illaoi',
        'Jinx', 'Yasuo']
}

def hash_password(password):
    """
    Hash a password using SHA-512.
    Returns a hex string.
    """
    return hashlib.sha512(password.encode()).hexdigest()

def save_user(username, email, password):
    """
    Save a new user's info to a .txt file.
    """
    user_file = os.path.join(USER_DATA_DIR, f'{username}.txt')

    if os.path.exists(user_file):
        return False, "User already exists"

    with open(user_file, 'w') as f:
        f.write(f'Username: {username}\n')
        f.write(f'Email: {email}\n')
        f.write(f'Password: {hash_password(password)}\n')

    return True, "Account has been created"

def get_notes_file(username, game):
    """Receiving the path to a users notes file for a certain game."""
    return os.path.join(DATA_NOTES_DIR, f'{username}_{game}_notes.json')


def load_all_notes(username, game):
    """
    Load all character notes for a specific user and game
    """
    notes_file = get_notes_file(username, game)

    if os.path.exists(notes_file):
        with open(notes_file, 'r') as f:
            return json.load(f)

    return {}  # Return empty dict if file doesn't exist


def load_character_notes(username, game, character):
    """
    Load notes for ONE specific character
    Example: load_character_notes("john", "mk1", "Scorpion")
    Returns: The text notes for that character
    """
    all_notes = load_all_notes(username, game)
    return all_notes.get(character, "")  # Return empty string if no notes


def save_character_notes(username, game, character, content):
    """
    Save notes for one specific character
    This updates the json file with the new notes for that character
    """
    notes_file = get_notes_file(username, game)

    # Load existing notes for all characters
    all_notes = load_all_notes(username, game)

    # Update just this character's notes
    all_notes[character] = content

    # Save everything back to the file
    with open(notes_file, 'w') as f:
        json.dump(all_notes, f, indent=2)

    return True, "Notes saved successfully"


def get_characters_for_game(game):
    """
    Get the list of characters for a specific game
    Example: get_characters_for_game("mk1") returns the MK1 character list
    """
    return GAME_CHARACTERS.get(game, [])