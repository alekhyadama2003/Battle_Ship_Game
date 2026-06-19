# 🚢 BattleShip Game

A Python-based Battleship game featuring strategic turn-based gameplay, persistent score tracking, and SQL-powered data management.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![SQL](https://img.shields.io/badge/Database-SQL-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📖 Project Overview

BattleShip Game is a command-line strategy game where players attempt to locate and sink enemy ships hidden on a grid. The project focuses on implementing core game mechanics, object-oriented programming principles, and database-driven score management using Python and SQL.

This project demonstrates practical skills in:

* Object-Oriented Programming (OOP)
* Game Logic Design
* Database Integration
* Data Persistence
* Backend Development Fundamentals
* Problem Solving and Algorithmic Thinking

---

## ✨ Features

* 🚢 Interactive Battleship gameplay
* 🎯 Hit and miss tracking
* 🗺️ Dynamic game board generation
* 👤 Player profile management
* 🏆 Leaderboard system
* 💾 SQL database integration
* 📊 Match history storage
* 🔄 Save and retrieve player statistics

---

## 🛠️ Tech Stack

| Category               | Technology                  |
| ---------------------- | --------------------------- |
| Programming Language   | Python                      |
| Database               | SQL (SQLite/MySQL)          |
| Architecture           | Object-Oriented Programming |
| Version Control        | Git & GitHub                |
| API Support (Future)   | FastAPI                     |
| Documentation (Future) | Swagger UI                  |

---

## 📂 Project Structure

```text
BattleShip-Game/
│
├── main.py
├── game.py
├── player.py
├── board.py
├── ship.py
│
├── database/
│   ├── database.db
│   ├── schema.sql
│   └── db_manager.py
│
├── assets/
│   └── screenshots/
│
├── requirements.txt
└── README.md
```

## 🎮 Gameplay

1. Start a new game
2. Place ships on the board
3. Attack enemy coordinates
4. Track hits and misses
5. Sink all enemy ships
6. Store game statistics in SQL database
7. View leaderboard and match history

---

## 🗄️ Database Design

### Players Table

```sql
CREATE TABLE players (
    player_id INTEGER PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    games_played INTEGER,
    games_won INTEGER
);
```

### Match History Table

```sql
CREATE TABLE match_history (
    game_id INTEGER PRIMARY KEY,
    player_id INTEGER,
    result VARCHAR(20),
    moves_taken INTEGER,
    played_at TIMESTAMP
);
```

---

## 🚀 Getting Started

### Clone Repository

```bash
git clone  https://github.com/alekhyadama2003/BattleShip-Game.git
```

### Navigate to Project

```bash
cd BattleShip-Game
```

### Run Application

```bash
python main.py
```

---

## 📈 Future Enhancements

* REST API using FastAPI
* Swagger UI Documentation
* Multiplayer Support
* Web-based Interface
* AI Opponent
* Docker Deployment
* Analytics Dashboard

---

## 📸 Screenshots

### Main Menu

Add screenshots inside:

```text
assets/screenshots/
```

Example:

```markdown
![Main Menu](assets/screenshots/main-menu.png)
![Game Board](assets/screenshots/game-board.png)
![Leaderboard](assets/screenshots/leaderboard.png)
```

---

## 📚 Learning Outcomes

This project showcases:

* Python Development
* SQL Database Management
* OOP Concepts
* Data Persistence
* Backend Engineering Fundamentals
* Software Design Principles

---

## 📄 License

This project is licensed under the MIT License.
