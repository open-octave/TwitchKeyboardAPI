import logging

import pygetwindow as gw


class WindowManager:
    def __init__(self):
         pass

    def focus_on_window(self, window_title):
            try:
                windows = gw.getWindowsWithTitle(window_title)
                if windows:
                    windows[0].activate()
                else:
                    logging.info(f"{window_title} window not found.")
            except Exception as e:
                logging.error(f"Error focusing on {window_title} on Windows: {e}")

    def get_all_open_windows(self):
        windows = gw.getAllWindows()
        return [win.title for win in windows if win.title]
    
    def get_retroarch_window_title(self):
        all_windows = self.get_all_open_windows()

        for window in all_windows:
            if "retroarch" in window.lower():
                return window
            
        return None
    
    def focus_on_retroarch(self):
        retroarch_window_title = self.get_retroarch_window_title()
        if retroarch_window_title:
            self.focus_on_window(retroarch_window_title)
        else:
            logging.info("Retroarch window not found.")
