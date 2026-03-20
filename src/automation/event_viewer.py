"""
Event Viewer automation for remote Windows systems.

Handles opening Event Viewer and navigating to System logs.
"""

import logging
from src.config.settings import COORDINATES, DELAYS
from src.utils.input_helper import InputHelper
from src.utils.window_manager import WindowManager

logger = logging.getLogger(__name__)


class EventViewerAutomation:
    """Automates Event Viewer operations."""
    
    def __init__(self, input_helper: InputHelper, window_manager: WindowManager):
        """
        Initialize the Event Viewer automation.
        
        Args:
            input_helper: InputHelper instance for keyboard/mouse automation
            window_manager: WindowManager instance for launching applications
        """
        self.input_helper = input_helper
        self.window_manager = window_manager
    
    def open_system_logs(self) -> None:
        """
        Open Event Viewer and navigate to System logs.
        
        Performs the following steps:
        1. Launch Event Viewer
        2. Click Windows Logs
        3. Click System logs
        4. Refresh the view
        """
        logger.info("Opening Event Viewer System logs")
        
        self.window_manager.launch_event_viewer()
        self._navigate_to_system_logs()
    
    def _navigate_to_system_logs(self) -> None:
        """Navigate through Event Viewer to System logs and refresh."""
        ev_coords = COORDINATES["event_viewer"]
        
        # Click Windows Logs
        x, y = ev_coords["windows_logs"]
        self.input_helper.click(x, y)
        
        # Click System logs
        x, y = ev_coords["system"]
        self.input_helper.click(x, y)
        
        # Refresh the view
        x, y = ev_coords["refresh"]
        self.input_helper.click(x, y)