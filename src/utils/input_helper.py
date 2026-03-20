"""
Input helper utilities for keyboard and mouse automation.

Provides safe wrapper functions for PyAutoGUI operations with
proper error handling and logging.
"""

import time
import logging
import pyautogui
from typing import Tuple, Optional
from src.config.settings import DELAYS, FAILSAFE_ENABLED, PAUSE_TIME

logger = logging.getLogger(__name__)


class InputHelper:
    """Helper class for keyboard and mouse automation."""
    
    def __init__(self):
        """Initialize the input helper with PyAutoGUI settings."""
        pyautogui.FAILSAFE = FAILSAFE_ENABLED
        pyautogui.PAUSE = PAUSE_TIME
    
    def click(self, x: int, y: int, delay: Optional[float] = None) -> None:
        """
        Click at specified coordinates.
        
        Args:
            x: X coordinate
            y: Y coordinate
            delay: Delay after click (default: from DELAYS['click_delay'])
        """
        logger.debug(f"Clicking at ({x}, {y})")
        pyautogui.click(x, y)
        time.sleep(delay or DELAYS["click_delay"])
    
    def double_click(self, x: int, y: int, delay: Optional[float] = None) -> None:
        """
        Double click at specified coordinates.
        
        Args:
            x: X coordinate
            y: Y coordinate
            delay: Delay after double click (default: from DELAYS['click_delay'])
        """
        logger.debug(f"Double clicking at ({x}, {y})")
        pyautogui.doubleClick(x, y)
        time.sleep(delay or DELAYS["click_delay"])
    
    def type_text(self, text: str, interval: Optional[float] = None) -> None:
        """
        Type text with specified interval between keystrokes.
        
        Args:
            text: Text to type
            interval: Time between keystrokes (default: from DELAYS['type_interval'])
        """
        logger.debug(f"Typing text (length: {len(text)})")
        pyautogui.typewrite(text, interval=interval or DELAYS["type_interval"])
    
    def press_key(self, key: str, delay: Optional[float] = None) -> None:
        """
        Press a single key.
        
        Args:
            key: Key to press (e.g., 'enter', 'tab')
            delay: Delay after key press (default: from DELAYS['click_delay'])
        """
        logger.debug(f"Pressing key: {key}")
        pyautogui.press(key)
        time.sleep(delay or DELAYS["click_delay"])
    
    def hotkey(self, *keys: str, delay: Optional[float] = None) -> None:
        """
        Press a hotkey combination.
        
        Args:
            *keys: Keys to press (e.g., 'win', 'r')
            delay: Delay after hotkey (default: from DELAYS['click_delay'])
        """
        logger.debug(f"Pressing hotkey: {'+'.join(keys)}")
        pyautogui.hotkey(*keys)
        time.sleep(delay or DELAYS["click_delay"])