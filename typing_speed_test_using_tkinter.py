from tkinter import *
import time
import random
import difflib


class TypingSpeedApp:
    def __init__(self, root):
        self.text_samples = [
            "The greatest glory in living lies not in never falling, but in rising every time we fall.",
            "The way to get started is to quit talking and begin doing.",
            "Your time is limited, so don't waste it living someone else's life.",
            "If life were predictable it would cease to be life, and be without flavor.",
            "If you look at what you have in life, you'll always have more.",
            "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.",
            "Life is what happens when you're busy making other plans.",
            "One day the people that don’t even believe in you will tell everyone how they met you.",
            "The true meaning of life is to plant trees, under whose shade you do not expect to sit.",
            "The quick brown fox jumps over the lazy dog."
        ]
        self.speed = 0
        self.accuracy = 0
        self.start_time = 0
        self.end_time = 0

        # Window settings
        root.title("Typing Speed Calculator")
        root.geometry("700x500")
        root.configure(bg="#282C34")

        # Display text label
        self.label_text = Label(
            root, text=random.choice(self.text_samples), wraplength=600, font=("Arial", 16, "bold"), fg="white",
            bg="#3E4451"
        )
        self.label_text.pack(pady=20, padx=20, fill=X)

        # Text input area
        self.user_text = Text(root, height=5, font=("Arial", 14), wrap=WORD, bg="#FFFFFF", fg="#000000")
        self.user_text.pack(pady=10, padx=20, fill=X)

        # Buttons frame
        self.button_frame = Frame(root, bg="#282C34")
        self.button_frame.pack(pady=10)

        self.btn_start = Button(self.button_frame, text="Start/Restart", command=self.start, font=("Arial", 14),
                                bg="#61AFEF", fg="black")
        self.btn_start.grid(row=0, column=0, padx=10, pady=5)

        self.btn_stop = Button(self.button_frame, text="Stop", command=self.stop, font=("Arial", 14), bg="#E06C75",
                               fg="black")
        self.btn_stop.grid(row=0, column=1, padx=10, pady=5)

        self.btn_newtext = Button(self.button_frame, text="New Text", command=self.new_text, font=("Arial", 14),
                                  bg="#98C379", fg="black")
        self.btn_newtext.grid(row=0, column=2, padx=10, pady=5)

        # Speed and accuracy labels
        self.label_speed = Label(root, text=f"Your typing speed: {self.speed} WPM", font=("Arial", 14), fg="#ABB2BF",
                                 bg="#282C34")
        self.label_speed.pack(pady=5)

        self.label_accuracy = Label(root, text=f"Your typing accuracy: {self.accuracy} %", font=("Arial", 14),
                                    fg="#ABB2BF", bg="#282C34")
        self.label_accuracy.pack(pady=5)

    def start(self):
        self.start_time = time.time()
        self.user_text.delete("1.0", END)

    def stop(self):
        self.end_time = time.time()
        words = self.label_text.cget("text").split()
        self.speed = round(len(words) / ((self.end_time - self.start_time) / 60))
        self.accuracy = round(difflib.SequenceMatcher(None, self.label_text.cget("text"),
                                                      self.user_text.get("1.0", 'end-1c')).ratio() * 100)

        self.label_speed.config(text=f"Your typing speed: {self.speed} WPM")
        self.label_accuracy.config(text=f"Your typing accuracy: {self.accuracy} %")

    def new_text(self):
        self.label_text.config(text=random.choice(self.text_samples))
        self.user_text.delete("1.0", END)


if __name__ == "__main__":
    root = Tk()
    app = TypingSpeedApp(root)
    root.mainloop()