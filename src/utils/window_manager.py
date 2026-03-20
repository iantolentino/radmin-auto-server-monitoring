"""
Window management utilities for launching applications.

Handles launching Radmin and other Windows applications.
"""

import os
import time
import subprocess
import logging
from typing import List, Optional
from src.config.settings import RADMIN_PATHS, DELAYS
from src.utils.input_helper import InputHelper

logger = logging.getLogger(__name__)


class WindowManager:
    """Manages application windows and launching."""
    
    def __init__(self, input_helper: InputHelper):
        """
        Initialize the window manager.
        
        Args:
            input_helper: InputHelper instance for keyboard/mouse automation
        """
        self.input_helper = input_helper
    
    def launch_radmin(self) -> None:
        """
        Launch Radmin from known installation paths.
        
        If Radmin is not found in standard paths, uses Windows Search.
        """
        logger.info("Launching Radmin...")
        
        # Try to launch from known paths
        for path in RADMIN_PATHS:
            if os.path.isfile(path):
                logger.debug(f"Found Radmin at: {path}")
                subprocess.Popen([path])
                time.sleep(DELAYS["radmin_launch"])
                return
        
        # Fallback: Use Windows Search
        logger.warning("Radmin not found in standard paths, using Windows Search")
        self.input_helper.hotkey("win")
        time.sleep(0.7)
        self.input_helper.type_text("radmin\n", DELAYS["command_interval"])
        time.sleep(DELAYS["radmin_launch"])
    
    def launch_event_viewer(self) -> None:
        """
        Launch Windows Event Viewer using Win+R run dialog.
        """
        logger.info("Launching Event Viewer...")
        self.input_helper.hotkey("win", "r", delay=DELAYS["run_command_delay"])
        self.input_helper.type_text("eventvwr.msc\n", DELAYS["command_interval"])
        time.sleep(DELAYS["event_viewer_load"])