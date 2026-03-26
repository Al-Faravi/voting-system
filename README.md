Markdown
# Secure Desktop Voting System 🗳️

A modern, lightweight desktop voting application built with Python and Tkinter. This project demonstrates secure user authentication, state management, and dynamic graphical interfaces using local JSON file storage.

## ✨ Features

* **Modern UI:** Utilizes `tkinter.ttk` for a clean, visually appealing, and modern user interface.
* **Secure Authentication:** User passwords are encrypted using **SHA-256 hashing** (`hashlib`). Plain-text passwords are never saved to the database.
* **Duplicate Vote Prevention:** Tracks user sessions and prevents users from casting more than one vote.
* **Dynamic Polling:** The app dynamically generates candidate buttons based on the `votes.json` file. You can easily add or remove candidates without touching the Python code.
* **Live Visual Results:** Automatically calculates vote percentages and displays them using visual progress bars.
* **Auto-Initializing Database:** Automatically generates the necessary JSON database files (`users.json` and `votes.json`) upon the first run if they don't already exist.

## 🛠️ Prerequisites

To run this application, you will need:
* **Python 3.x** installed on your system.
* Standard Python libraries (`tkinter`, `json`, `hashlib`, `os`) which come pre-installed with Python. No external `pip` installations are required.

## 🚀 Getting Started

Follow these steps to get the project running on your local machine:

**1. Clone the repository:**
```bash
git clone [https://github.com/Al-Faravi/voting-system.git](https://github.com/Al-Faravi/voting-system.git)
cd voting-system
2. Run the application:

Bash
python main.py 
(Note: If your main Python file is named differently, replace main.py with your actual file name.)

💡 How to Use
Register: Launch the app and click "Register Account". Create a new username and password.

Login: Go back to the main menu and click "Login to Vote". Enter your newly created credentials.

Vote: Click on the candidate of your choice. A confirmation box will appear to ensure you don't misclick. Once you vote, you cannot vote again with that account.

View Results: Anyone can click "View Live Results" from the main menu to see the current standings, total vote counts, and visual percentage bars.

📂 Project Structure and Data Storage
This app uses local .json files as a lightweight database.

users.json: Stores registered usernames, their SHA-256 hashed passwords, and a boolean value (true/false) tracking whether they have voted.

votes.json: Stores the candidates and their current vote counts.

Want to add a new candidate? Simply open votes.json in any text editor before running the app and add them to the dictionary. For example:

JSON
{
    "Candidate A": 0,
    "Candidate B": 0,
    "Candidate C": 0,
    "Candidate D": 0
}
The app will automatically detect "Candidate D" and create a voting button and a results progress bar for them.

🔒 Security Note
While this application uses SHA-256 hashing to protect passwords, it stores data in local JSON files. It is designed for educational purposes, local network environments, or small-scale polling.

👨‍💻 Author
Md. Shakawat Hossain Faravi

GitHub: @Al-Faravi


Would you like me to show you how to compile this Python script into a standalone `.exe`
