"""
Configuration settings for Radmin Automation.

This module contains all hardcoded configuration values including
credentials, file paths, and screen coordinates.
"""

from typing import List, Tuple

# Credentials
USERNAME: str = "your_username_here"
FIRST_PASSWORD: str = "your_password_here"
SECOND_PASSWORD: str = "your_password_here"

# Radmin installation paths
RADMIN_PATHS: List[str] = [
    r"C:\Program Files\Radmin Viewer 3\radmin.exe",
    r"C:\Program Files (x86)\Radmin Viewer 3\radmin.exe",
]

# Screen coordinates for UI elements
# Format: (x, y)
COORDINATES = {
    "connect_button": (445, 265),        # "Connect to an address"
    "remote_tab": (810, 15),             # Remote session tab
    "cad_button": (225, 35),             # Ctrl+Alt+Del button
    "event_viewer": {
        "windows_logs": (175, 170),      # Windows Logs section
        "system": (245, 245),            # System logs
        "refresh": (1048, 600)           # Refresh button
    }
}

# Timing delays (in seconds)
DELAYS = {
    "radmin_launch": 5,                  # Wait for Radmin to open
    "connect_delay": 1,                  # After clicking connect
    "auth_delay": 2,                     # After entering credentials
    "remote_tab_activation": 5,          # After connecting
    "password_delay": 2,                 # After clicking CAD button
    "event_viewer_launch": 5,            # Wait for Event Viewer
    "run_command_delay": 1,              # After Win+R
    "event_viewer_load": 8,              # Wait for Event Viewer to load
    "click_delay": 1,                    # Between clicks
    "type_interval": 0.05,               # Between keystrokes
    "command_interval": 0.08,            # Between commands
}

# PyAutoGUI settings
FAILSAFE_ENABLED: bool = True
PAUSE_TIME: float = 0.2