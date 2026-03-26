import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
import hashlib

# ---------- SECURITY ----------
def hash_password(password):
    """Hashes a password using SHA-256 for secure storage."""
    return hashlib.sha256(password.encode()).hexdigest()

# ---------- FILE SETUP ----------
def init_files():
    if not os.path.exists("users.json"):
        with open("users.json", "w") as f:
            json.dump({}, f)

    if not os.path.exists("votes.json"):
        with open("votes.json", "w") as f:
            # You can easily add more candidates here now
            json.dump({"Candidate A": 0, "Candidate B": 0, "Candidate C": 0}, f)

init_files()

def load_json(filename):
    with open(filename, "r") as f:
        return json.load(f)

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4) # Added indent for readable JSON

# ---------- MAIN APP ----------
root = tk.Tk()
root.title("Secure Voting System")
root.geometry("450x550")
root.configure(bg="#1e1e2f")

# Styling using ttk
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", background="#1e1e2f", foreground="white", font=("Arial", 12))
style.configure("Header.TLabel", font=("Arial", 20, "bold"))

current_user = None

# ---------- FUNCTIONS ----------
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

def register_screen():
    clear_screen()

    ttk.Label(root, text="Create Account", style="Header.TLabel").pack(pady=20)

    ttk.Label(root, text="Username:").pack(pady=5)
    username = ttk.Entry(root, font=("Arial", 12))
    username.pack(pady=5)

    ttk.Label(root, text="Password:").pack(pady=5)
    password = ttk.Entry(root, show="*", font=("Arial", 12))
    password.pack(pady=5)

    def register():
        user_val = username.get().strip()
        pass_val = password.get().strip()

        if not user_val or not pass_val:
            messagebox.showwarning("Warning", "Fields cannot be empty!")
            return

        users = load_json("users.json")
        if user_val in users:
            messagebox.showerror("Error", "User already exists!")
        else:
            users[user_val] = {
                "password": hash_password(pass_val), 
                "voted": False
            }
            save_json("users.json", users)
            messagebox.showinfo("Success", "Registered successfully! Please login.")
            main_menu()

    ttk.Button(root, text="Register", command=register).pack(pady=20)
    ttk.Button(root, text="Back to Menu", command=main_menu).pack()

def login_screen():
    clear_screen()

    ttk.Label(root, text="Login to Vote", style="Header.TLabel").pack(pady=20)

    ttk.Label(root, text="Username:").pack(pady=5)
    username = ttk.Entry(root, font=("Arial", 12))
    username.pack(pady=5)

    ttk.Label(root, text="Password:").pack(pady=5)
    password = ttk.Entry(root, show="*", font=("Arial", 12))
    password.pack(pady=5)

    def login():
        global current_user
        user_val = username.get().strip()
        pass_val = password.get().strip()

        users = load_json("users.json")

        if user_val in users and users[user_val]["password"] == hash_password(pass_val):
            current_user = user_val
            vote_screen()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    ttk.Button(root, text="Login", command=login).pack(pady=20)
    ttk.Button(root, text="Back to Menu", command=main_menu).pack()

def vote_screen():
    clear_screen()
    users = load_json("users.json")

    if users[current_user]["voted"]:
        messagebox.showinfo("Info", "You have already cast your vote.")
        main_menu()
        return

    ttk.Label(root, text=f"Welcome, {current_user}!", style="Header.TLabel").pack(pady=20)
    ttk.Label(root, text="Please select your candidate:").pack(pady=10)

    def cast_vote(candidate):
        # Confirm vote
        if messagebox.askyesno("Confirm", f"Are you sure you want to vote for {candidate}?"):
            votes = load_json("votes.json")
            users = load_json("users.json")

            votes[candidate] += 1
            users[current_user]["voted"] = True

            save_json("votes.json", votes)
            save_json("users.json", users)

            messagebox.showinfo("Success", "Your vote has been recorded securely.")
            main_menu()

    # Dynamically generate buttons based on the JSON file
    votes = load_json("votes.json")
    for candidate in votes.keys():
        ttk.Button(root, text=candidate, command=lambda c=candidate: cast_vote(c)).pack(pady=5, fill='x', padx=100)

    ttk.Button(root, text="Logout", command=main_menu).pack(pady=30)

def result_screen():
    clear_screen()
    votes = load_json("votes.json")
    total_votes = sum(votes.values())

    ttk.Label(root, text="Live Results", style="Header.TLabel").pack(pady=20)
    ttk.Label(root, text=f"Total Votes Cast: {total_votes}").pack(pady=10)

    # Frame for progress bars
    results_frame = tk.Frame(root, bg="#1e1e2f")
    results_frame.pack(fill="both", expand=True, padx=40)

    for candidate, count in votes.items():
        # Calculate percentage safely
        percentage = (count / total_votes * 100) if total_votes > 0 else 0

        ttk.Label(results_frame, text=f"{candidate}: {count} votes ({percentage:.1f}%)").pack(anchor="w", pady=(10, 0))
        
        # Visual Progress Bar
        bar = ttk.Progressbar(results_frame, length=300, maximum=100, mode='determinate')
        bar['value'] = percentage
        bar.pack(pady=5)

    ttk.Button(root, text="Back to Menu", command=main_menu).pack(pady=20)

def main_menu():
    global current_user
    current_user = None  # Reset user on menu load
    clear_screen()

    ttk.Label(root, text="Secure Voting System", style="Header.TLabel").pack(pady=40)

    ttk.Button(root, text="Login to Vote", command=login_screen).pack(pady=10, fill='x', padx=120)
    ttk.Button(root, text="Register Account", command=register_screen).pack(pady=10, fill='x', padx=120)
    ttk.Button(root, text="View Live Results", command=result_screen).pack(pady=10, fill='x', padx=120)
    
    ttk.Button(root, text="Exit", command=root.quit).pack(pady=30)

# ---------- START ----------
if __name__ == "__main__":
    main_menu()
    root.mainloop()