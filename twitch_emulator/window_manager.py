import logging
import subprocess
import sys

import pygetwindow as gw


class WindowManager:
    def __init__(self, window_title):
        self.window_title = window_title

    def focus_on_window(self):
        if sys.platform == "darwin":
            try:
                script = f"""/usr/bin/osascript -e 'tell app "{self.window_title}" to activate' """
                subprocess.run(script, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                logging.error(f"Error focusing on {self.window_title} on macOS: {e}")
        elif sys.platform == "win32":
            try:
                windows = gw.getWindowsWithTitle(self.window_title)
                if windows:
                    windows[0].activate()
                else:
                    logging.info(f"{self.window_title} window not found.")
            except Exception as e:
                logging.error(f"Error focusing on {self.window_title} on Windows: {e}")
