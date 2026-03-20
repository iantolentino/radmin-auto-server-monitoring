"""
Radmin controller for automating Radmin Viewer operations.

Handles connecting to remote machines and sending credentials.
"""

import time
import logging
from typing import Optional
from src.config.settings import COORDINATES, DELAYS, USERNAME, FIRST_PASSWORD, SECOND_PASSWORD
from src.utils.input_helper import InputHelper
from src.utils.window_manager import WindowManager

logger = logging.getLogger(__name__)


class RadminController:
    """Controls Radmin Viewer automation."""
    
    def __init__(self, input_helper: InputHelper, window_manager: WindowManager):
        """
        Initialize the Radmin controller.
        
        Args:
            input_helper: InputHelper instance for keyboard/mouse automation
            window_manager: WindowManager instance for launching applications
        """
        self.input_helper = input_helper
        self.window_manager = window_manager
    
    def connect(self, address: str) -> None:
        """
        Connect to a remote Radmin address.
        
        Args:
            address: IP address or hostname of remote machine
        """
        logger.info(f"Connecting to address: {address}")
        
        self._open_connection_dialog()
        self._enter_address(address)
        self._enter_credentials()
    
    def _open_connection_dialog(self) -> None:
        """Open the connection dialog in Radmin."""
        logger.debug("Opening connection dialog")
        x, y = COORDINATES["connect_button"]
        self.input_helper.click(x, y, delay=DELAYS["connect_delay"])
    
    def _enter_address(self, address: str) -> None:
        """Enter the remote address and submit."""
        logger.debug(f"Entering address: {address}")
        self.input_helper.type_text(address)
        self.input_helper.press_key("enter")
        time.sleep(DELAYS["auth_delay"])
    
    def _enter_credentials(self) -> None:
        """Enter username and first password."""
        logger.debug("Entering credentials")
        self.input_helper.type_text(USERNAME)
        self.input_helper.press_key("tab")
        self.input_helper.type_text(FIRST_PASSWORD)
        self.input_helper.press_key("enter")
    
    def activate_remote_session(self) -> None:
        """Activate the remote session tab."""
        logger.info("Activating remote session tab")
        x, y = COORDINATES["remote_tab"]
        self.input_helper.double_click(x, y, delay=DELAYS["remote_tab_activation"])
    
    def send_windows_password(self) -> None:
        """Send Windows password via Ctrl+Alt+Del button."""
        logger.info("Sending Windows password")
        x, y = COORDINATES["cad_button"]
        self.input_helper.click(x, y, delay=DELAYS["password_delay"])
        self.input_helper.type_text(SECOND_PASSWORD)
        self.input_helper.press_key("enter")