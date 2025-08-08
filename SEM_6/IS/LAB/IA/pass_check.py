import tkinter as tk
from tkinter import ttk
import string
import re

class PasswordStrengthCheckerUI:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Password Strength Checker")
        self.master.geometry("400x400")
        self.master.configure(bg="#f0f0f0")

        ttk.Label(self.master, text="Enter Password:").pack(pady=10)
        self.password_entry = ttk.Entry(self.master, show="*", width=30)
        self.password_entry.pack(pady=5)

        check_button = ttk.Button(self.master, text="Check Strength", command=self.check_password)
        check_button.pack(pady=10)

        self.result_label = ttk.Label(self.master, text="Strength: ")
        self.result_label.pack(pady=5)

        self.progress_bar = ttk.Progressbar(self.master, length=300, mode="determinate")
        self.progress_bar.pack(pady=10)

        self.criteria_met_label = ttk.Label(self.master, text="", justify=tk.LEFT)
        self.criteria_met_label.pack(pady=5, padx=10, anchor="w")

        self.criteria_missing_label = ttk.Label(self.master, text="", justify=tk.LEFT)
        self.criteria_missing_label.pack(pady=5, padx=10, anchor="w")

    def check_password(self):
        password = self.password_entry.get()
        strength_level, score, criteria_met, criteria_missing = self.password_strength(password)
        self.update_ui(strength_level, score, criteria_met, criteria_missing)

    def password_strength(self, password):
        score = 0
        length = len(password)
        upper_case = any(c.isupper() for c in password)
        lower_case = any(c.islower() for c in password)
        special = any(c in string.punctuation for c in password)
        digits = any(c.isdigit() for c in password)

        criteria = {
            'Length >= 8': length >= 8,
            'Length >= 12': length >= 12,
            'Length >= 17': length >= 17,
            'Length >= 20': length >= 20,
            'Uppercase': upper_case,
            'Lowercase': lower_case,
            'Special character': special,
            'Digit': digits
        }

        criteria_met = [k for k, v in criteria.items() if v]
        criteria_missing = [k for k, v in criteria.items() if not v]

        score = len(criteria_met)

        if score < 4:
            return "Weak", score, criteria_met, criteria_missing
        elif score == 4:
            return "Okay", score, criteria_met, criteria_missing
        elif 4 < score < 6:
            return "Good", score, criteria_met, criteria_missing
        else:
            return "Strong", score, criteria_met, criteria_missing

    def update_ui(self, strength_level, score, criteria_met, criteria_missing):
        color_map = {"Weak": "red", "Okay": "orange", "Good": "yellow", "Strong": "green"}
        color = color_map.get(strength_level, "black")

        self.result_label.config(text=f"Strength: {strength_level}", foreground=color)

        met_text = "Criteria Met:\n" + "\n".join(f"✓ {c}" for c in criteria_met)
        missing_text = "Criteria Missing:\n" + "\n".join(f"✗ {c}" for c in criteria_missing)

        self.criteria_met_label.config(text=met_text, foreground="green")
        self.criteria_missing_label.config(text=missing_text, foreground="red")

        self.progress_bar["value"] = (score / 8) * 100
        self.progress_bar["style"] = f"{color}.Horizontal.TProgressbar"

def main():
    root = tk.Tk()
    app = PasswordStrengthCheckerUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
