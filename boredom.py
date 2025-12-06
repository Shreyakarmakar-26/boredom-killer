import tkinter as tk
import random
from tkinter import font
# PATTERN 1: SINGLETON
# acts as "internal API" or Database
class ActivityAPI:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ActivityAPI, cls).__new__(cls)
            cls._instance.activities = [
                "Learn how to whistle with your fingers.",
                "Organize your computer desktop icons by color.",
                "Write a letter to your future self (open in 5 years).",
                "Learn the alphabet in Sign Language.",
                "Do 15 pushups right now!",
                "Watch a documentary on Deep Sea creatures.",
                "Try to draw a perfect circle freehand.",
                "Clean your room while listening to 80s music.",
                "Meditate for 5 minutes.",
                "Make a paper airplane and see how far it flies.",
                "Read novels.",
                "Bake a cake."
            ]
        return cls._instance

    def fetch_data(self):
        """Simulates fetching data from an endpoint"""
        return self.activities
# PATTERN 2: FACADE
# Hides the logic of "choosing" from the UI
class BoredomFacade:
    def __init__(self):
        self.api = ActivityAPI()  # Connects to the Singleton API

    def get_random_suggestion(self):
        """Simple interface for the UI to get a string"""
        data = self.api.fetch_data()
        return random.choice(data)
# FRONTEND UI (The "Client")
class BoredomApp:
    def __init__(self, root):
        self.root = root
        self.logic = BoredomFacade() # usage of Facade
        
        self.root.title("Boredom Killer")
        self.root.geometry("500x400")
        self.root.configure(bg="#F4D03F") 

        # Custom Fonts
        self.header_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.text_font = font.Font(family="Verdana", size=14)

        # 1. Header Label
        self.header = tk.Label(
            root, 
            text="ARE YOU BORED?", 
            bg="#F4D03F", 
            fg="#2C3E50",
            font=self.header_font
        )
        self.header.pack(pady=40)

        # 2. Activity Display Area (The text that changes)
        self.activity_label = tk.Label(
            root,
            text="Click the button to kill boredom!",
            bg="#F4D03F",
            fg="#333333",
            wraplength=400,
            font=self.text_font
        )
        self.activity_label.pack(pady=20)

        # 3. Square Button (Playful Interface)
        self.suggest_btn = tk.Button(
            root,
            text="SUGGEST TASK",
            command=self.update_task,
            bg="#E74C3C",    # Bright Red/Orange button
            fg="white",      # White text
            font=("Arial", 12, "bold"),
            relief="flat",   # Flat modern look
            width=20,
            height=3,        # Square-ish shape
            cursor="hand2"
        )
        self.suggest_btn.pack(pady=40)
        
        # Footer
        self.footer = tk.Label(root, text="v1.0 - Frontend Prototype", bg="#F4D03F", font=("Arial", 8))
        self.footer.pack(side="bottom", pady=10)

    def update_task(self):
        # The UI asks the Facade for a task, not caring how it's calculated
        new_task = self.logic.get_random_suggestion()
        self.activity_label.config(text=new_task)


if __name__ == "__main__":
    root = tk.Tk()
    app = BoredomApp(root)
    root.mainloop()