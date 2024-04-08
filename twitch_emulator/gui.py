import threading
import tkinter as tk
from tkinter import scrolledtext

from twitch_emulator.__main__ import start_twitch_listener, stop_twitch_listener


class TwitchBotGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EAT Control Panel")
        self.geometry("800x500")

        self.start_button = tk.Button(
            self, text="Start Listener", command=self.start_listener
        )
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(
            self, text="Stop Listener", command=self.stop_listener
        )
        self.stop_button.pack(pady=10)

        self.log_area = scrolledtext.ScrolledText(self, state="disabled", height=100)
        self.log_area.pack(pady=10)

        self.listener_thread = None

    def log_message(self, message):
        self.log_area.configure(state="normal")
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.configure(state="disabled")
        self.log_area.yview(tk.END)

    def start_listener(self):
        if self.listener_thread is None or not self.listener_thread.is_alive():
            self.listener_thread = threading.Thread(
                target=start_twitch_listener, args=()
            )
            self.listener_thread.start()
            self.log_message("Listener started.")

    def stop_listener(self):
        stop_twitch_listener()
        self.log_message("Listener stopped.")


if __name__ == "__main__":
    app = TwitchBotGUI()
    app.mainloop()
