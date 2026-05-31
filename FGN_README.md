# Fighting Game Notebook

A full-stack web application built with Flask and Python that allows fighting game players to securely create accounts, log in, and manage personal character notes across multiple games. Whether you're labbing combos, tracking frame data, or planning your gameplan — this app keeps your notes organized per game and per character.

---

## 🎮 Supported Games & Characters

| Game | Characters |
|------|------------|
| Mortal Kombat 1 | Scorpion, Sub-Zero, Liu Kang, Raiden, Kitana, Mileena, Kung Lao, Johnny Cage, Kenshi, Smoke, Rain, Reptile, Ashrah, Havik, Baraka, Geras, General Shao, Reiko, Tanya, Li Mei, Sindel, Shang Tsung, Quan Chi, Ermac, Takeda, Omni-Man, Peacemaker, Homelander, Ghostface, Conan |
| Street Fighter 6 | Ryu, Ken, Chun-Li, Guile, Blanka, Dhalsim, E. Honda, Zangief, Cammy, Dee Jay, Rashid, Juri, Kimberly, Lily, JP, Marisa, Manon, Luke, Jamie, A.K.I., Ed, Akuma, Bison, Terry, Mai, Elena |
| 2XKO | Ahri, Braum, Darius, Ekko, Illaoi, Jinx, Yasuo |

---

## ✨ Features

- **Secure Authentication** — Account creation with SHA-512 password hashing and session-based login
- **Game-Themed UI** — Each game's notebook page is styled to match its visual identity
- **Per-Character Notes** — Freeform text area for combos, frame data, matchup notes, strategy, and more
- **Character Switcher** — Switch between characters on the fly without returning to the dashboard
- **JSON-Based Storage** — Notes stored per user, per game, per character with dynamic loading and saving via backend APIs
- **Live Character Counter** — Tracks note length in real time
- **Input Validation** — Password confirmation, minimum length, and duplicate account checks on signup

---

## 🗂️ File Structure

```
Fighting-Game-Notebook/
│
├── fgc.py              # Main Flask app — routes and session management
├── backend.py          # Backend logic — auth, file I/O, notes management
│
├── templates/
│   ├── index.html      # Landing page
│   ├── login.html      # Login page
│   ├── signUp.html     # Sign up page
│   ├── dashboard.html  # Main dashboard with game selection
│   └── notebook.html   # Character notebook page
│
├── user_data/          # Stores user account files (auto-created)
└── data_notes/         # Stores character notes as JSON (auto-created)
```

---

## 🔧 Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Flask |
| Auth | SHA-512 password hashing, Flask sessions |
| Storage | JSON files |
| Frontend | HTML, CSS, JavaScript |
| Routing | Flask URL routing with login decorators |

---

## 🚀 How to Run

**1. Clone the repo**
```bash
git clone https://github.com/ayplusplus/Fighting-GameNoteBook.git
cd Fighting-GameNoteBook
```

**2. Install dependencies**
```bash
pip install flask
```

**3. Run the app**
```bash
python fgc.py
```

**4. Open in your browser**
```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

### Landing Page
Animated pixel-art fighting game stage background with a "Press Start" button and arcade sound effect.

### Dashboard
Displays all three supported games with official artwork and a character selector dropdown for each.

### Notebook Page
Game-themed notebook with a character switcher, freeform notes area, live character counter, and save functionality.

---

## 🧑‍💻 Author

**Sean Austin**
B.S. Applied Computing — Arizona State University
[LinkedIn](https://linkedin.com/in/seanvaustin) • [GitHub](https://github.com/ayplusplus)
