# Python Tkinter App
import tkinter as tk
from tkinter import messagebox

facts = {
    # Religion Questions
    "What religion do most Arabs practice?": "Most Arabs are Muslim, mostly Sunni.",
    "Are all Arabs Muslim?": "No. Not all Arabs are Muslim, and not all Muslims are Arab.",
    "What religion do most Persians practice?": "Shi'a Islam.",
    "What is the holy book of Islam?": "The Quran.",
    "What religion do most Kurds follow?": "Sunni Islam, but they are often less strict.",
    "Name the three major religions in SW Asia.": "Judaism, Christianity, Islam.",
    "What religion uses the Torah?": "Judaism.",
    "What religion follows Jesus Christ?": "Christianity.",
    "Which religion believes in one God (Allah) and follows the Five Pillars?": "Islam.",

    # Ethnic Groups Questions
    "What language do most Arabs speak?": "Arabic.",
    "Where do most Persians live?": "Iran.",
    "What language do Persians speak?": "Farsi (Persian).",
    "Who are the Kurds?": "An ethnic group in Turkey, Syria, Iraq, and Iran.",
    "Do Kurds have a country of their own?": "No, they are the largest group without a country.",
    "What language do Kurds speak?": "Kurdish, related to Farsi.",
    "Who are Arabs descended from?": "Abraham through Ishmael.",

    # U.S. History Questions
    "Why did the U.S. go to war in Iraq in 2003?": "Suspected WMDs & ties to al-Qaeda (Operation Iraqi Freedom).",
    "What was the goal of Operation Desert Storm?": "Free Kuwait from Iraqi invasion.",
    "Who was Osama bin Laden?": "Leader of al-Qaeda, behind 9/11 attacks.",
    "When was bin Laden killed?": "May 2, 2011, in Pakistan.",
    "What group ruled Afghanistan before U.S. invasion?": "The Taliban."
}

class StudyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SW Asia Study Helper")
        self.root.geometry("1920x1080")

        self.label = tk.Label(root, text="Click a question to see the answer:", font=("Arial", 12))
        self.label.pack(pady=10)

        for question in facts:
            btn = tk.Button(root, text=question, wraplength=480,
                            command=lambda q=question: self.show_answer(q))
            btn.pack(pady=3)

    def show_answer(self, question):
        messagebox.showinfo("Answer", facts[question])

if __name__ == "__main__":
    root = tk.Tk()
    app = StudyApp(root)
    root.mainloop()
